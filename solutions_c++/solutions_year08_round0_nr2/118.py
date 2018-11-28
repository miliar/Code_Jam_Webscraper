#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <sstream>
#include <algorithm>

using namespace std;

int toInt(const string &s){
	stringstream ss(s);
	int ret;
	ss >> ret;
	return ret;
}


vector <string> split(const string & s){
	stringstream ss(s);
	string g;
	vector <string> ret;
	while (ss >> g)
		ret.push_back(g);
	return ret;
}

struct event{
	int Time,A,B;
	event(int T,int A,int B) : Time(T),A(A),B(B) {};
	bool operator<(const event & o) const {return Time == o.Time ? A+B<o.A+o.B : Time < o.Time;}
};

int time(const string &s){
	return toInt(s.substr(0,2)) * 60 + toInt(s.substr(3,2));
}

int main(int argc,const char * argv[]){
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	int TC;
	string line;
	vector <string> lv;
	getline(fin,line);
	TC=toInt(line);
	for (int tc=1;tc<=TC;tc++){
		int Time;
		getline(fin,line);
		Time=toInt(line);
		getline(fin,line);
		lv = split(line);
		int N = toInt(lv[0]),M = toInt(lv[1]);
		vector <event> events;		
		for (int i=0;i<N;i++){
			getline(fin,line);
			lv = split(line);
			events.push_back(event(time(lv[0]),1,0));
			events.push_back(event(time(lv[1])+Time,0,-1));
		}	
		for (int i=0;i<M;i++){
			getline(fin,line);
			lv = split(line);
			events.push_back(event(time(lv[0]),0,1));
			events.push_back(event(time(lv[1])+Time,-1,0));
		}
		sort(events.begin(),events.end());
		int A = 0, B = 0, mA = 0, mB = 0;
		for (int i=0;i<events.size();i++){
			//cout << events[i].Time << " " << events[i].A << " " << events[i].B << endl;
			A+=events[i].A;
			B+=events[i].B;
			mA = max(mA,A);
			mB = max(mB,B);
		}
		cout << endl;

		fout << "Case #" << tc << ": " << mA << " " << mB << endl;
	}

}