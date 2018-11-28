//#pragma comment(linker, "/STACK:100000000")
#include <iostream>   
#include <sstream>   
#include <cstdio>   
#include <cstdlib>   
#include <cmath>   
#include <memory>   
#include <cctype>   
#include <string>   
#include <vector>   
#include <list>   
#include <queue>   
#include <deque>   
#include <stack>   
#include <map>   
#include <set>   
#include <algorithm>   
using namespace std;  
   
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))  
#define RFOR(i,a,b) for(int (i) = (a)-1; (i) >= (b); --(i))  
#define CLEAR(a) memset((a),0,sizeof(a))  
#define INF 1000000000  
#define PB push_back  
#define ALL(c) (c).begin(), (c).end()  
#define pi 2*acos(0.0)  
#define SQR(a) (a)*(a)  
#define MP make_pair  
#define CONST 1000
#define MAX 2300
#define mod 1000000007
#define X                       first
#define Y                       second.first
#define Z                       second.second
   
typedef long long LL; 
typedef long long i64; 
typedef pair<LL,LL>           PII;
typedef vector<LL>             VI;

int dl(int n){
	int r=0;
	while (n){
		r++;
		n/=10;
	}
	return r;
}
int pr(string s){
	int n=0;
	FOR(i,0,s.size()){
		n*=10;
		n+=(s[i]-48);
	}
	return n;
}
string prs(int n){
	string s="";
	while (n){
		s=char(n%10+48)+s;
		n/=10;
	}
	return s;
}
string ls(string s){
	string d="";
	d+=s[s.size()-1];
	FOR(i,0,s.size()-1)
		d+=s[i];
	return d;
}

int g[3000000][10];
int d[3000000];
map<pair<int,int>,bool> M;
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int x;
	FOR(j,1,2000001){
			int n=j;
			//cin>>n;
			d[j]=dl(n);
			string s=prs(n);
			FOR(i,0,d[j]){
				s=ls(s);
				x=pr(s);
				if (x>j && x<2000001 && !M[MP(j,x)]){
					g[j][i]=x;
					M[MP(j,x)]=1;
				}
				//cout<<pr(s)<<endl;
			}
	}
	//cout<<"--"<<endl;
	int t;
	cin>>t;
	FOR(tt,1,t+1){
		int a,b;
		a=1; b=2000000;
		cin>>a>>b;
		int ans=0;
		FOR(i,a,b)
			FOR(j,0,d[i])
			if (g[i][j]>i && g[i][j]<=b)
				ans++;
		cout<<"Case #"<<tt<<": "<<ans<<endl;		
	}
	
    return 0;
}