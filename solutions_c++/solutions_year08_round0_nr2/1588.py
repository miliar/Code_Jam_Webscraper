#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

typedef pair<unsigned int, unsigned int> Int_Pair;

Int_Pair calc(vector<Int_Pair> &atob, vector<Int_Pair> &btoa)
{
	unsigned int atrain = 0, btrain = 0;
	while (!atob.empty() || !btoa.empty())
	{
		int lastitor=0, curitor=0;
		vector<Int_Pair> *lastlane;		
		vector<Int_Pair> *curlane;		
		unsigned int curtime = 0;
		if ( atob.empty() )
		{
			btrain += btoa.size();
			break;
		}
		else if ( btoa.empty() )
		{
			atrain += atob.size();
			break;
		}

		if ( atob.begin()->first > btoa.begin()->first )
		{
			btrain++;
			lastlane = &atob;		
			curlane = &btoa;		
		}
		else
		{
			atrain++;
			lastlane = &btoa;		
			curlane = &atob;		
		}
		for (;curitor != curlane->size();)
			if ((*curlane)[curitor].first >= curtime)
			{
				curtime = (*curlane)[curitor].second;
				curlane->erase(curlane->begin()+curitor);
				swap(curlane, lastlane);	//exchange
				swap(curitor, lastitor);	//exchange
			}
			else  curitor++;
	}
	return make_pair(atrain, btrain);
}

int main (int argc, char *argv[])
{
	if (!argc) return 1;
	ifstream file(argv[1]);
	if (!file) return 2;
	unsigned int num;
	file >> num;
	//	cout << num;
	unsigned int caseNum = 1;
	while ( caseNum <= num )
	{
		cout <<"Case #" <<caseNum <<": ";

		vector<Int_Pair> atob, btoa;
		unsigned int turnaround = 0, an = 0 ,bn = 0;
		file >>turnaround >>an >>bn;
//		cout <<turnaround <<' ' <<an <<' ' <<bn <<endl;
		for (unsigned int i=0; i<an; i++)	//time info a->b
		{
			unsigned int leavet, arrivet;
			unsigned int hh, mm;
			file >>hh;
			file.get();
			file >>mm;
//			cout <<"leave: " <<hh <<':' <<mm <<endl;
			leavet = mm + hh*60;

			file >>hh;
			file.get();
			file >>mm;
//			cout <<"arrive: " <<hh <<':' <<mm <<endl;
			arrivet = mm + hh*60;
			arrivet += turnaround;			//convert to turnaround time == 0

			atob.push_back(Int_Pair(leavet, arrivet));
		}
		sort(atob.begin(), atob.end());

		for (unsigned int i=0; i<bn; i++)	//time info b->a
		{
			unsigned int leavet, arrivet;
			unsigned int hh, mm;
			file >>hh;
			file.get();
			file >>mm;
//			cout <<"leave: " <<hh <<':' <<mm <<endl;
			leavet = mm + hh*60;

			file >>hh;
			file.get();
			file >>mm;
//			cout <<"arrive: " <<hh <<':' <<mm <<endl;
			arrivet = mm + hh*60;
			arrivet += turnaround;			//convert to turnaround time == 0

			btoa.push_back(Int_Pair(leavet, arrivet));
		}
		sort(btoa.begin(), btoa.end());

//		for (unsigned int i=0; i<bn; i++)
//		{
//			cout <<btoa[i].first <<' ' <<btoa[i].second <<endl;
//		}


		Int_Pair trains = calc(atob, btoa);
		cout <<trains.first <<' ' <<trains.second <<endl;
		caseNum++;
	}
	return 0;
}