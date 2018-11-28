#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
using namespace std;

#define FOR(i,a) for (int (i)=0;(i)<(a);++(i))
#define FORR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define sz(a) int((a).size()) 
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end() 


main(){
	ofstream fout ("B-large-0.out");
	ifstream fin ("B-large-0.in");
	int T;
	fin>>T;
	FOR(num,T){
		vector<vector<int> > change('z'-'a'+2, vector<int> ('z'-'a'+1,-1));
		vector<vector<int> > op('z'-'a'+2, vector<int> ('z'-'a'+1,0));
		int C;
		fin>>C;
		FOR(i,C){
			string st;
			fin>>st;
			change[st[0]-'A'][st[1]-'A']=st[2]-'A';
			change[st[1]-'A'][st[0]-'A']=st[2]-'A';
		}
		int D;
		fin>>D;
		FOR(i,D){
			string st;
			fin>>st;
			op[st[0]-'A'][st[1]-'A']=1;
			op[st[1]-'A'][st[0]-'A']=1;
		}
		string out="";
		int N;
		fin>>N;
		string word;
		fin>>word;
		int last='z'-'a'+1; //neutral with everything
		FOR(i,N){
//			cout<<" *"<<last<<" *"<<out<<endl;
			if (change[last][word[i]-'A']!=-1){
				out[sz(out)-1]=change[last][word[i]-'A']+'A';
				last=out[sz(out)-1]-'A';
			}
			else{
				out=out+word[i];

				last=out[sz(out)-1]-'A';
				FOR(j,sz(out)){
					if (op[out[j]-'A'][word[i]-'A']){
						out="";
						last='z'-'a'+1;
					}
				}
			}
		}
		
		fout<<"Case #"<<num+1<<": ";
		cout<<out<<endl;
		fout<<"[";
		FOR(i,sz(out)){
			if (i!=0) fout<<", ";
			fout<<out[i];
		}
		fout<<"]";
		fout<<endl;
	}
	fout.close();
}
