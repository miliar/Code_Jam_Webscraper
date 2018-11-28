#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define RREPEAT(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) RREPEAT(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll unsigned long long int
#define uli unsigned long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("C-small-attempt10.in");
#define cin fin
ofstream fout ("C-small10.out");
#define cout fout
int n,m;
int a[513][513],B[513][513];
void parse(int i, int j, char c) {
	int choice=0;
	if(c>='0' && c<='9') choice=(int)(c-'0');
	else choice = (int) (c-'A'+10);
	string s[16]={"0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"};
	REP(k,4) a[i][j*4+k]=s[choice][k]-'0';
	return;
}
bool go(int i, int j, int k) {
	bool flag=true;
	REP(ii,k)
	 REP(jj,k) 
	  if(a[i+ii][j+jj]!=B[ii][jj] || a[i+ii][j+jj]>1) flag=false;
	if(flag) return true;
	flag=true;
	REP(ii,k)
	 REP(jj,k) 
	  if(a[i+ii][j+jj]==B[ii][jj]  || a[i+ii][j+jj]>1) flag=false;
	if(flag) return true;
	return false;
}
void process(int i, int j, int k) {
	REP(ii,k) REP(jj,k) a[ii+i][jj+j]=2;
	return;
}
int main() {
    int t;
    cin>>t;
    REP(i,512) REP(j,512) {
		if(i%2) B[i][j]=j%2;
		else B[i][j]=(j+1)%2;
	}
    REP(T,t) {
		cin>>m>>n;
		char c;
		REP(i,m) {
			REP(j,n/4) {
				cin>>c;
				parse(i,j,c);
			}
		}
		int mx = min(n,m),cnt=0;
		vi v(mx+1,0);
		RREPEAT(k,mx,1) {
		//	cerr<<k<<endl;
			REP(i,m-k+1) REP(j,n-k+1) if(go(i,j,k)) process(i,j,k),v[k]++;
			cnt+=(v[k]>0);
		}
		cerr<<T+1<<endl;
		cout<<"Case #"<<T+1<<": "<<cnt<<endl;
		REP(i,v.size()) if(v[mx-i]>0) cout<<(mx-i)<<" "<<v[mx-i]<<endl;
    }
    system("pause");
    return 0;
}
