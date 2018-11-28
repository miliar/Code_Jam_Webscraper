#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define DIST(x1, y1, x2, y2) (float)((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
#define SORT(x) sort(x.begin(),x.end());

ifstream fin("d:\\gcj\\q.in");
ofstream fout("d:\\gcj\\sol.out");
#define cin fin
#define cout fout

class TTEntry
{
public:
	int depHr;
	int depMin;
	int arrHr;
	int arrMin;
	int station;
	TTEntry(const char* times, int s)
	{
		sscanf(times, "%d:%d %d:%d", &depHr, &depMin, &arrHr, &arrMin);
		station = s;
	}
	TTEntry():depHr(0),arrHr(0),depMin(0),arrMin(0){}
	
	bool operator<(const TTEntry& rhs) const
	{
		return ((depHr == rhs.depHr)?(depMin>(rhs.depMin)):(depHr>(rhs.depHr)));
	}

	void Increment(int T)
	{
		depMin+=T;
		if(depMin>=60)
		{
			depMin = depMin%60;
			depHr++;// Dont wrap around
		}

		arrMin += T;
		if(arrMin>=60)
		{
			arrMin %= 60;
			arrMin++;
		}
	}

	void UpdateTimes()
	{
		int dif = (depHr*60 + depMin)-(arrHr*60+arrMin);

		depHr = arrHr;
		depMin = arrMin;

		arrHr = ((depHr*60+depMin)+dif)/60;
		arrMin = ((depHr*60+depMin)+dif)%60;
	}
};

// Sort the time table entries based on departure times. (earliest first)
// for(each time table entry)
// {
//    if(No trains are available at the station at this time in the Availability Q)
//    {
//      Measure when the train will be available on the other side
//      Add this to the Availability Q
//      Increment train count for the station
//    }
//    else
//    {
//      Remove the earliest matching train available from the Availability Q 
//    } 
// }
void Solution()
{
	priority_queue<TTEntry> availabilityQs[2];
	priority_queue<TTEntry> ttentries;

	int T = 0;
	cin >> T;

	int NA = 0, NB = 0;
	cin >> NA;
	cin >> NB;

	char buf[51];
	cin.getline(buf,50);
	for(int i=0;i<NA;++i)
	{
		cin.getline(buf,50);
		ttentries.push(TTEntry(buf,0));
	}

	for(int j=0;j<NB;++j)
	{
		cin.getline(buf,50);
		ttentries.push(TTEntry(buf,1));
	}

	int nab[2];
	memset(&nab, 0, sizeof(nab));
	TTEntry tmp;
	while(ttentries.size()!=0)
	{		
		tmp = ttentries.top();
		int destStation = tmp.station?0:1;
		if(availabilityQs[tmp.station].size() != 0)
		{
			TTEntry av = availabilityQs[tmp.station].top();
			if((av.depHr == tmp.depHr)?(av.depMin<=tmp.depMin):(av.depHr<=tmp.depHr))
			{
				availabilityQs[tmp.station].pop();

				av.depHr = tmp.arrHr;
				av.depMin = tmp.arrMin;
				av.Increment(T);
				if(av.depHr <= 23)
					availabilityQs[destStation].push(av);
			}
			else
			{
				tmp.UpdateTimes();
				tmp.Increment(T);
				if(tmp.depHr <= 23)
				{
					availabilityQs[destStation].push(tmp);
				}
				nab[tmp.station]++;				
			}
		}
		else
		{
			tmp.UpdateTimes();
			tmp.Increment(T);
			if(tmp.depHr <= 23)
			{
				availabilityQs[destStation].push(tmp);
			}
			nab[tmp.station]++;
		}

		ttentries.pop();
	}

	cout << nab[0] << " " << nab[1];
}

int main(int argc, TCHAR* argv[])
{
    int N = 0;
	cin >> N;

	vector<float> len(3,0);
	
	for(int i=0;i<N;++i)
	{
		cout << "Case #" << i+1 << ": ";
		Solution();
		cout << endl;
	}

	return 0;
}
