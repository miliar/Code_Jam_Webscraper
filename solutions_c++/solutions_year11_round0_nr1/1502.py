#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define abs(x) ((x<0)?(-(x)):(x))
#define equal(a,b) (ABS((a)-(b))<eps)
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pair pair<int,int>

using namespace std;

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};
char s[500];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	gets(s);
	sscanf(s,"%d",&T);
	for(int i=1; i<=T; i++){
		int ap=1;
		int bp=1;
		int tt=0;
		int ta=0;
		int tb=0;
		int fa=0;
		int fb=0;
		int nes;
		int et;
		gets(s);
		stringstream ss(*new string(s));
		string t;
		int b;
		int n;
		ss>>n;
		for(int j=0; j<n; j++){
			ss>>t>>b;
			if(t[0]=='O'){
				nes=abs(b-ap);
				et = tb-ta;
				if(et>=0)
				tt+=max(nes-et,0)+1;
				else 
				tt+=nes+1;
				ta=tt;
				ap=b;
			} else if(t[0]=='B'){
				nes=abs(b-bp);
				et = ta-tb;
				if(et>=0)
				tt+=max(nes-et,0)+1;
				else 
				tt+=nes+1;
				tb=tt;
				bp=b;
			}
		}
		printf("Case #%d: %d\n",i,tt);
	}
	//system("pause");
	return 0;
}
