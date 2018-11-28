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

int comb[100][100];
int opp[100][100];
int main(){
	freopen("b-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++){
		memset(comb,-1,sizeof(comb));
		memset(opp,-1,sizeof(opp));
		int n;
		scanf("%d",&n);
		while(n--){
			string s;
			cin>>s;
			comb[s[0]][s[1]]=comb[s[1]][s[0]]=(int)s[2];
		}
		scanf("%d",&n);
		while(n--){
			string s;
			cin>>s;
			opp[s[0]][s[1]]=opp[s[1]][s[0]]=1;
		}
		scanf("%d",&n);
		string s,t;
		cin>>s;
		for (int i=0;i<s.size();i++){
			t+=s[i];
			int k=t.size();
			if (k>=2){
				//combine
				if (comb[t[k-2]][t[k-1]]!=-1){
					t+=(char)comb[t[k-2]][t[k-1]];
					t.erase(k-2,2);
					continue;
				}
				//clear
				for (int j=0;j<t.size()-1;j++)
					if (opp[t[j]][t[k-1]]!=-1) { t=""; break; }
			}
			
		}
		printf("Case #%d: [",test);
		for (int i=0;i<t.size();i++){
			cout<<t[i];
			if (i!=t.size()-1) printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
