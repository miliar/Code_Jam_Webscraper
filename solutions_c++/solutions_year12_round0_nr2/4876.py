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
#define ABS(x) ((x<0)?(-(x)):(x))
#define equal(a,b) (ABS((a)-(b))<eps)
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pair pair<int,int>

using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		int ret=0;
		vector<int> ns;
		int S,P,N,k;
		scanf("%d%d%d",&N,&S,&P);
		for(int i=0; i<N; i++){
			scanf("%d",&k);
			if(k%3==0 && k/3>=P && k/3>=0) ret++;
			else if(k%3==1 && k/3+1>=P && k/3>=0) ret++;
			else if(k%3==2 && k/3+1>=P && k/3>=0) ret++;
			else ns.pb(k);
		}
		for(int i=0; i<ns.size() && S>0; i++){
			k=ns[i];
			if(k%3==0 && k/3+1>=P && k/3-1>=0) {ret++;S--;}
			else if(k%3==1 && k/3+1>=P && k/3-1>=0) {ret++;S--;}
			else if(k%3==2 && k/3+2>=P && k/3>=0) {ret++;S--;}
		}
		printf("Case #%d: %d\n",t,ret);
	}
	return 0;
}
