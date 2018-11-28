#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <list>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>
#include <algorithm>

using namespace std;

int N;
int T;


struct Case{
	int T;
	vector< vector<pair<int,int> > > TIME;
	vector<int>COUNT;
};

class sortFunc
{
public:
  bool operator()(const pair<int,int>& x, const pair<int,int>& y) const {
		if(x.first != y.first)
		{
			return x.first < y.first;
		}else{
			return x.second < y.second;
		}
  }
};

vector<Case> cases;

int getMinutes(string s)
{
	boost::trim(s);
	int hour = boost::lexical_cast<int>(s.substr(0,2));
	int min = boost::lexical_cast<int>(s.substr(3,2));
	return hour*60+min;
}

vector<pair<int,int> >::iterator findNextTrain(int now, vector<pair<int,int> >& times)
{
	for(vector<pair<int,int> >::iterator i=times.begin(); i!=times.end(); i++)
	{
		if(i->first >= now)return i;
	}
	return times.end();
}

bool traceAndCutTrain(Case& ca, int index, int now)
{
	//cout << "called: " << index << "," << (int)(now/60) << ":" << (now%60) << endl;
	vector<pair<int,int> >::iterator next = findNextTrain(now, ca.TIME[index]);
	if(next == ca.TIME[index].end())return false;
	//cout << "find: " << (int)(next->first / 60) << ":" << (int)(next->first % 60) << endl;

	//cout << "cut:" << index << ":" << (int)(next->first / 60) << ":" << (int)(next->first % 60) << endl;

	int t = next->second + ca.T;
	ca.TIME[index].erase(next);
	traceAndCutTrain(ca, (index+1)%2, t);

	return true;
}


int main(int argc, char **argv){
	string buff;
	ifstream ifs(argv[1]);
	
	getline(ifs, buff);
	N = boost::lexical_cast<int>(buff);
	cases.resize(N);

	for(int n=0; n<N; n++)
	{
		cases[n].COUNT.resize(2);
		cases[n].TIME.resize(2);

		cases[n].COUNT[0]=0;
		cases[n].COUNT[1]=0;

		getline(ifs, buff);
		cases[n].T = boost::lexical_cast<int>(buff);

		vector<string> nodes;
		getline(ifs, buff);
		boost::algorithm::split( nodes, buff, boost::is_any_of("\t ") );
		int ab = boost::lexical_cast<int>(nodes[0]);
		int ba = boost::lexical_cast<int>(nodes[1]);
		cases[n].TIME[0].resize(ab);
		cases[n].TIME[1].resize(ba);
		for(int i=0; i<ab; i++)
		{
			vector<string> times;
			getline(ifs, buff);
			boost::algorithm::split( times, buff, boost::is_any_of("\t ") );
			int departure = getMinutes(times[0]);
			int arrival = getMinutes(times[1]);
			cases[n].TIME[0][i] = pair<int,int>(departure, arrival);
		}

		for(int i=0; i<ba; i++)
		{
			vector<string> times;
			getline(ifs, buff);
			boost::algorithm::split( times, buff, boost::is_any_of("\t ") );
			int departure = getMinutes(times[0]);
			int arrival = getMinutes(times[1]);
			cases[n].TIME[1][i] = pair<int,int>(departure, arrival);
		}

		// sort by departure time
		sort( cases[n].TIME[0].begin(), cases[n].TIME[0].end(), sortFunc() );
		sort( cases[n].TIME[1].begin(), cases[n].TIME[1].end(), sortFunc() );
	}		

// START
	for(int n=0; n<N; n++)
	{
		//cout << "==AB==" << endl;
		//for(int i=0; i<cases[n].TIME[0].size(); i++)cout << (int)(cases[n].TIME[0][i].first/60) << ":" << (int)(cases[n].TIME[0][i].first%60) << endl;
		//cout << "==BA==" << endl;
		//for(int i=0; i<cases[n].TIME[1].size(); i++)cout << (int)(cases[n].TIME[1][i].first/60) << ":" << (int)(cases[n].TIME[1][i].first%60) << endl;


		while(cases[n].TIME[0].size() != 0 || cases[n].TIME[1].size())
		{
			int t1 = 100*60;
			int t2 = 100*60;
			if(cases[n].TIME[0].size() != 0)t1 = cases[n].TIME[0][0].first;
			if(cases[n].TIME[1].size() != 0)t2 = cases[n].TIME[1][0].first;
			//cout << "TRY" << endl;
			if(t1 < t2)
			{
				//cout << "start 0" << endl;
				//cout << "time=" << (int)(t1/60) << ":" << (int)(t1%60) << endl;
				traceAndCutTrain(cases[n], 0 , t1);
				cases[n].COUNT[0]++;
			}else{
				//cout << "start 1" << endl;
				//cout << "time=" << (int)(t2/60) << ":" << (int)(t2%60) << endl;
				traceAndCutTrain(cases[n], 1 , t2);
				cases[n].COUNT[1]++;
			}
		}
		cout << "Case #" << n+1 << ": " << cases[n].COUNT[0] << " " << cases[n].COUNT[1] << endl;
	}

	return 0;
}
