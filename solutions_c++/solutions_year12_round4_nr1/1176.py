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
#include <climits>
using namespace std;

#define iter(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define FOR(i,a) for (int (i)=0;(i)<(a);++(i))
#define FORR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define sz(a) int((a).size()) 
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end() 


int main(){
//	ofstream fout ("A-small-0.out");
//	ifstream fin ("A-small-0.in");
	ofstream fout ("A-large.out");
	ifstream fin ("A-large.in");
	int T;
	fin>>T;
	FOR(num,T){
		long long N,D;
		fin>>N;
		vector<long long> dp(N,0);
		vector<long long> d(N);
		vector<long long> l(N);
		FOR(i,N){
			long long pomd,poml;
			fin>>pomd>>poml;
			d[i]=pomd;
			l[i]=poml;
		}
		fin>>D;
		dp[0]=d[0];
		FOR(i,N){
				for(int j=i+1;j<N;j++){
						if (d[j]-d[i]<=dp[i]){
								dp[j]=max(dp[j],min(l[j],d[j]-d[i]));
						}
				}
/*				int new_i=-1;
				for(int j=i-1;j>=0;j--){
						if (d[i]-d[j]<=dp[i]){
								if (min(l[j],d[i]-d[j]) > dp[j]){
									dp[j]=min(l[j],d[i]-d[j]);
									new_i=j;
								}
						}
				}
				if (new_i>0) i=new_i;
*/		}
		FOR(i,N){
				cout<<dp[i]<<endl;
		}
		cout<<"-----"<<endl;
		fout<<"Case #"<<num+1<<": ";
		bool ok=false;
		FOR(i,N){
			if (dp[i]>=D-d[i]) ok=true;
		}
		if (ok)
			fout<<"YES"<<endl;
		else
			fout<<"NO"<<endl;
	}
	fout.close();
}
