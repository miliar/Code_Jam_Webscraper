#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
int main(int argc, char *argv[])
{

	ifstream  ifs("input");
	ofstream ofs("output");

	int N;
	ifs >> N;

	for (int cas = 0; cas < N; ++cas)
	{
//		cout << "Case " <<cas << endl;
		int count;
		ifs >> count;
		vector<pair<bool, int> > vr(count);
		for (int i =0; i< count; ++i)
		{
			char c;
			int pos;
			ifs >> c >> pos;
			vr[i].first = c == 'O';
			vr[i].second = pos;
		}

		int posA = 1;
		int posB = 1;
		int timeA = 0;
		int timeB = 0;
		int cur_time = 0;
		for (int i =0; i< vr.size(); ++i)
		{
//			cout << cur_time << endl;
			if (vr[i].first)
			{
				timeA += abs(posA - vr[i].second);
				if (timeA < cur_time)
					timeA = cur_time;
				timeA++;
				cur_time = timeA;
				posA=vr[i].second;
			}
			else
			{
				timeB += abs(posB - vr[i].second);
				if (timeB < cur_time)
					timeB = cur_time;
				timeB++;
				cur_time = timeB;
				posB=vr[i].second;
			}
		}

		ofs << "Case #" << cas +1 << ": "<< cur_time <<endl;

//		for (int i =0; i< vr.size(); ++i)
//			cout << vr[i].first << " "<< vr[i].second << endl;
	}


}
