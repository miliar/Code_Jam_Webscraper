#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow,ileKart,n,t[10000];

int main(){
	
	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		
		scanf("%d%d",&ileKart,&n);
		
		fu(a,n) scanf("%d",&t[a]);

		int v[10000], gdzie=0, licz=0, score[10000];
		memset(v,-1,sizeof v);
		memset(score,-1,sizeof score);
		
		licz=1;
		fu(a,ileKart){
			while( licz<a+1 ){
				if( gdzie+1 < ileKart ) gdzie++; else gdzie=0;
				if( v[gdzie] == -1 ) licz++;
			}
			v[ gdzie ] = a+1;
			licz=0;
		}

		printf("Case #%d:",q);
		fu(a,n) printf(" %d",v[ t[a]-1 ]);
		printf("\n");
	}

	return 0;
}
