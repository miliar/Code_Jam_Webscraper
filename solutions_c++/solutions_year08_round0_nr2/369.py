#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

//Compiled using MS VC++ 2005

struct sched {
	int dep;
	char station;
	int arr;
	bool operator<(const struct sched& s){
		return dep<s.dep;
	}
};

struct train {
	vector<sched> times;
	bool IsAvail(sched s,int T){
		if (times.empty())
			return true;
		sched last=times.back();
		if (last.station!=s.station && s.dep>=(last.arr+T))
			return true;
		else
			return false;
	}
	void AddSched(sched s){
		times.push_back(s);
	}
};

int ConvertTime(char* c){
	return (c[0]-'0')*10*60+(c[1]-'0')*60+(c[3]-'0')*10+(c[4]-'0');
}

//Takes the input file as only argument and spits to cout
int main (int argc,char* argv[]) {	
	int cs=0;	//# of cases
	ifstream infile;
	infile.open (argv[1], ifstream::in);
	infile>>cs;
	for (int c=0;c<cs;c++){
		vector<sched> AllRuns;
		vector<train> trains;
		int T;
		int Aruns;
		int Bruns;
		infile>>T;
		infile>>Aruns;
		infile>>Bruns;
		for (int i=0;i<Aruns;i++){
			char buffer[10];
			int dep;
			int arr;
			sched s;
			infile>>buffer;
			dep=ConvertTime(buffer);
			infile>>buffer;
			arr=ConvertTime(buffer);
			s.dep=dep;
			s.station='A';
			s.arr=arr;
			AllRuns.push_back(s);
		}
		for (int i=0;i<Bruns;i++){
			char buffer[10];
			int dep;
			int arr;
			sched s;
			infile>>buffer;
			dep=ConvertTime(buffer);
			infile>>buffer;
			arr=ConvertTime(buffer);
			s.dep=dep;
			s.station='B';
			s.arr=arr;
			AllRuns.push_back(s);
		}
		std::sort(AllRuns.begin(),AllRuns.end());
		for (vector<sched>::iterator itrun=AllRuns.begin();itrun!=AllRuns.end();itrun++){
			bool blNeedTrain=true;
			for (vector<train>::iterator ittrain=trains.begin();ittrain!=trains.end();ittrain++){
				if (ittrain->IsAvail(*itrun,T)){
					ittrain->AddSched(*itrun);
					blNeedTrain=false;
					break;
				}
			}
			if (blNeedTrain){
				train t;
				t.AddSched(*itrun);
				trains.push_back(t);
			}
		}
		int FromA=0;
		int FromB=0;
		for (vector<train>::iterator ittrain=trains.begin();ittrain!=trains.end();ittrain++){
			if (ittrain->times.begin()->station=='A')
				FromA++;
			else
				FromB++;
		}
		cout<<"Case #"<<(c+1)<<": "<<FromA<<" "<<FromB<<endl;
	}

	//clean up
	infile.close();
	return 0;
}

