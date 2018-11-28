#include <map>
#include <set>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define xx first
#define yy second
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++){
		int n;
		scanf("%d",&n);
		vector<pair<int,char> > v;
		for (int i=0;i<n;i++){
			char s[3];
			int c;
			scanf("%s%d",s,&c);
			v.pb(mp(s[0],c));
		}
		int o=1,b=1,time=0;
		for (int i=0;i<n;i++){
			if (v[i].xx=='B'){
				int cur=ABS(v[i].yy-b)+1;
				b=v[i].yy;
				time+=cur;
				for (int j=i+1;j<n;j++)
					if (v[j].xx=='O'){
						int dist=v[j].yy-o;
						if (ABS(dist)<=cur) o=v[j].yy;
						else if (dist>0) o+=cur;
						else o-=cur;
						break;
					}
			}
			else{
				int cur=ABS(v[i].yy-o)+1;
				o=v[i].yy;
				time+=cur;
				for (int j=i+1;j<n;j++)
					if (v[j].xx=='B'){
						int dist=v[j].yy-b;
						if (ABS(dist)<=cur) b=v[j].yy;
						else if (dist>0) b+=cur;
						else b-=cur;
						break;
					}
			}
		}
		printf("Case #%d: %d\n",test,time);
	}
//	system("pause");
	return 0;
}
