#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <strstream>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define gold 1.61803398874989484820458683436564

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int i,j,k,l,m,n,ri,repeat,a1,a2,b1,b2;
int check(int a,int b){
	int flag=1,t;
	if(a<b){t=a;a=b;b=t;}
	while(1){
		if(a-b>=b)return flag;
		flag=-flag;
		t=a-b;
		a=b;
		b=t;
	}
}
		
int main()
{
        freopen("C-large.in","r",stdin);
        //freopen("x.txt","r",stdin);
        freopen("w.txt","w",stdout);
        scanf("%d",&repeat);
        for(ri=1;ri<=repeat;ri++){
			printf("Case #%d: ",ri);
			scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
			long long total=0;
			for(i=a1;i<=a2;i++){
				m=gold*i;
				m++;
				m=max(b1,m);
				//printf("%d,\n",m);
				if(b2-m+1>0)total+=b2-m+1;
			}
			for(i=b1;i<=b2;i++){
				m=gold*i;
				m++;
				m=max(a1,m);
				if(a2-m+1>0)total+=a2-m+1;
			}
			printf("%lld\n",total);
		}
}

