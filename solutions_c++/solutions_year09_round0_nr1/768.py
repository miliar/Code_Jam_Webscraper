#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;
int N,L,D;
char s[6000][18];
char t[10000];
vector<char> var[18];

int main()
{
    scanf("%d%d%d",&L,&D,&N);
    Repi(D)
     {
			scanf("%s",s[i]);
			//cout<<"						"<<s[i]<<"\n";
	 }
	
	Repi(N)
	 {
			scanf("%s",t);
			
			//cout<<"\n\n case "<<i<<" : "<<t<<"\n";
			
			Repj(L) var[j].clear();
			int at=0;
			bool in=0;
			for (int j=0;t[j];j++)
			 {
					if (t[j]=='(') in=1;
					else if (t[j]==')') { in=0; at++; }
					else
					 {
						var[at].PB(t[j]);
						if (!in) at++;
					 }
			 }
			
			//Repj(L)			 {			    cout<<"			"<<j<<" : "; Repk(var[j].SZ) cout<<var[j][k]; cout<<"\n";			 }
			int cnt=0;
			Repi(D)
			 {
						bool ok=1;
						Repj(L)
						 {
									bool thislet=0;
									Repk(var[j].SZ)
									 if (var[j][k]==s[i][j]) {thislet=1; break; }
									if (!thislet) { ok=0; break; }
						 }
						if (ok)
						 {
						 	cnt++;
						 	//cout<<"		match "<<s[i]<<"\n";
						 }
			 }
			cout<<"Case #"<<i+1<<": "<<cnt<<"\n";
	 }
    return 0;
}
