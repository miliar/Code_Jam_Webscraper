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
	ofstream fout ("A-large-0.out");
	ifstream fin ("A-large-0.in");
	int T;
	fin>>T;
	FOR(num,T){
		bool out=false;
		long long N,pd,pg;
		fin>>N;
		fin>>pd;
		fin>>pg;
		if (pd==pg && (pd==100 || pd==0)) out = true;
		else if(pg==100 || pg==0) {
			out = false;
		}
		else{
			FORR(i,1,min(N+1,(long long)101)){
				FOR(j,i+1){
					if (j*100==i*pd) out=true;
				}
			}
		
		}
		if (out == true) fout<<"Case #"<<num+1<<": Possible"<<endl;
		else fout<<"Case #"<<num+1<<": Broken"<<endl;
	}
	fout.close();
}
