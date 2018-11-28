#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define memo(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 __int64

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,cs,mask,nmask,i,n;
	i64 k,x;
	scanf("%d",&t);
	for(cs=1;cs<=t;cs++){
		scanf("%d %I64d",&n,&k);
		
		x = 1<<n;
		k++;
		printf("Case #%d: ",cs);
		if(k % x == 0) puts("ON");
		else puts("OFF");
	}
	return 0;
}