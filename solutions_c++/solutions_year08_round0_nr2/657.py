#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define dbg(x) cout << #x << " -> " << x << "\t" << flush;
#define dbge(x) cout << #x << " -> " << x << "\t" << endl;
#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define cs c_str()
#define pb push_back
#define sz size()
#define INF (int)1e9+1

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
//typedef long long LL;
typedef long double LD;

struct time1{
	int dept,arrt, curplace;
};

struct s{
	int curtime,curplace;
};

bool cmp(const time1 & a,const time1 & b){
	if(a.dept!=b.dept)	return (a.dept<b.dept);
	return (a.arrt<b.arrt);
}

vector<time1> timetable;
vector<s> available;

int main(){

	ifstream fin("input2.txt");
	ofstream fout("output2.txt");
	int n;
	fin>>n;
	FOR(i,1,n+1){
		int ansa=0,ansb=0,na,nb,t;
		fin>>t>>na>>nb;fin.get();
		timetable.clear();
		available.clear();
		
		REP(j,na){
			char depart[5],arrive[5];
			fin>>depart;fin.get();
			fin>>arrive;fin.get();
			int dept= ((depart[0]-'0')*10+(depart[1]-'0'))*60+((depart[3]-'0')*10+(depart[4]-'0'));
			int arrt= ((arrive[0]-'0')*10+(arrive[1]-'0'))*60+((arrive[3]-'0')*10+(arrive[4]-'0'));
			time1 z;
			z.dept=dept;
			z.arrt=arrt;
			z.curplace= 1;
			timetable.pb(z);
		}	 
		REP(j,nb){
			char depart[5],arrive[5];
			fin>>depart;fin.get();
			fin>>arrive;fin.get();
			int dept= ((depart[0]-'0')*10+(depart[1]-'0'))*60+((depart[3]-'0')*10+(depart[4]-'0'));
			int arrt= ((arrive[0]-'0')*10+(arrive[1]-'0'))*60+((arrive[3]-'0')*10+(arrive[4]-'0'));
			time1 z;
			z.dept=dept;
			z.arrt=arrt;
			z.curplace= 2;
			timetable.pb(z);
		}	 	    
		sort(timetable.begin(),timetable.end(),cmp);
		
		REP(j,timetable.sz){
			bool c=0;
			REP(k,available.sz){
				if(available[k].curplace==timetable[j].curplace && available[k].curtime<=timetable[j].dept && !c){
					available[k].curplace= (available[k].curplace%2)+1;
					available[k].curtime= timetable[j].arrt+t;
					c=1;
				}
			}
			if(!c){
				s z;
				z.curplace= (timetable[j].curplace%2)+1;
				z.curtime= timetable[j].arrt+t;
				available.pb(z);
				if(timetable[j].curplace==1)	ansa++;
				else	ansb++;
			}
			
		}
	
		fout<<"Case #"<<i<<": "<<ansa<<" "<<ansb<<endl;	   
	}
	return 0;
}

