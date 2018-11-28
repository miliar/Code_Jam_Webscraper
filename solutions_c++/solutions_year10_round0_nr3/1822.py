#include <algorithm> 
#include <numeric>
#include <cmath> 

#include <string> 
#include <string.h>
#include <vector> 
#include <queue> 
#include <stack> 
#include <set> 
#include <map> 

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cassert> 

using namespace std;
#pragma comment(linker, "/STACK:20000000")

// useful defines
#define sz(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define Rep(i,n) for (int i=0;i<(n);++i)
#define RepV(i,v) for (int i=0;i<sz(v);++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(a) (a).begin(),(a).end()   
typedef long long LL;
typedef pair <int,int> PI;
typedef pair <double,double> PD;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;

int tt;
int r,k,n;
int x[1010];
pair<LL,int> q[1010];
int v[1010];
int c;

int main() {
	freopen("in.in","rt",stdin);
	freopen("cbig.out","wt",stdout);


	cin>>tt;

	Rep(t,tt){
		cout<<"Case #"<<t+1<<": ";
		cin>>r>>k>>n;

		Rep(i,n) cin>>x[i];

		LL s=0;
		int nn=0;
		int j=0;

		v[0]=t+1;
		q[0]=make_pair(0,0);

		int st=0;

		c=-1;

		while(1){
			LL w=0;
			j=st;
			while(w+x[j]<=k){
				w+=x[j];
				j++;
				j%=n;
				if(j==st) break;
			}
			s+=w;
			nn++;
			if(v[j]==t+1){
				q[j].first = s-q[j].first;
				q[j].second = nn-q[j].second;
				c=j;
				break;
			}
			v[j]=t+1;
			q[j]=make_pair(s,nn);
			st=j;
		}


		LL res=0;

		int p=0;

		while(r){
			LL w=0;
			int pp=p;

			if(p==c){
				res+=q[c].first*(r/q[c].second);
				r%=q[c].second;
				if(r==0) break;
			}

			while(w+x[pp]<=k){
				w+=x[pp];
				pp++;
				pp%=n;
				if(pp==p) break;
			}

			res+=w;
			r--;
			p=pp;
			w=0;
		}



		cout<<res<<endl;

	}




	
	return 0;
}