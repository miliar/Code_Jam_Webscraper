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
	ofstream fout ("C-small-0.out");
	ifstream fin ("C-small-0.in");
	int T;
	fin>>T;
	FOR(temp,T){
		int N;
		fin>>N;
		vector<int> a;
		FOR(i,N){
			int pom;
			fin>>pom;
			a.pb(pom);
		}
		int best=-1;
		int spolu=0;
		FOR(i,sz(a)) spolu+=a[i];
		FOR(i,32768){
			int sum_a=0;
			int sum_b=0;
			int suma=0;
			FOR(j,sz(a)){
				if ((i & 1 << j) != 0){
					sum_a=sum_a^a[j];
					suma+=a[j];
				}
				else{
					sum_b=sum_b^a[j];
				}
			}
			if (sum_a==sum_b && suma!=0 && suma!=spolu){
				best=max(best,suma);
			}
		}
		if (best==-1) 		fout<<"Case #"<<temp+1<<": "<<"NO"<<endl;
		else	fout<<"Case #"<<temp+1<<": "<<best<<endl;
	}
	fout.close();
}
