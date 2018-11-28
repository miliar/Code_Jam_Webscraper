#include<cstdio>
#include<map>
#include<vector>
#include<sstream>
#include<algorithm>
#include<string>
#include<cstring>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a;i < b;++i)
#define FORZ(i,t) for(int i = 0;i < t;++i)
#define PB push_back

typedef long long LL;

LL NOI(int X[],int Y[],int n) {
	LL ret = 0;
	for(int i = 0;i < n;++i){
		int x = X[i],y = Y[i];

		for(int j = 0;j < n;++j)
			if(i != j)
			{
				if(X[i] < X[j] && Y[i] > Y[j]) ret ++;
				if(X[i] > X[j] && Y[i] < Y[j]) ret ++;
			}
	}

return ret/2;
}

int main(){
	int test = GI;
	
	FOR(i,1,test+1){

		printf("Case #%d: ",i);
		int N = GI;
		int X[N],Y[N];
		FOR(j,0,N) {
			X[j] = GI; Y[j] = GI;
		}

		printf("%lld\n",NOI(X,Y,N) );
	}

	return 0;
}
