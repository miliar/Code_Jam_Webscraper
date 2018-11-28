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

bool p1[40][40];
bool p2[40][40];
int a[200];
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	FOR(s,0,31)
	{
		FOR(i,0,11)
			FOR(j,0,11)
			FOR(k,0,11){
				if(i+j+k==s && max(max(i,j),k)-min(min(i,j),k)<=1){
					int x=max(max(i,j),k);
					FOR(q,0,x+1)
						p1[s][q]=1;
				}
				if(i+j+k==s && max(max(i,j),k)-min(min(i,j),k)==2){
					int x=max(max(i,j),k);
					FOR(q,0,x+1)
						p2[s][q]=1;
				}
		}
	}
	int t;
	cin>>t;
	FOR(tt,1,t+1){
		int n,s,p;
		cin>>n>>s>>p;
		int k1=0,k2=0,k3=0;
		FOR(i,0,n){
			int t;
			cin>>t;
			if (p1[t][p] && p2[t][p])
				k1++;
			if (p1[t][p] && !p2[t][p])
				k2++;
			if (!p1[t][p] && p2[t][p])
				k3++;
		}
		
		//cout<<k1<<" "<<k2<<" "<<k3<<endl;
		if (k3>s)
			k3=s;
		cout<<"Case #"<<tt<<": "<<k1+k2+k3<<endl;
	}

	
    return 0;
}