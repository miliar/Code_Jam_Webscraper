#include<math.h>
#include<ctype.h>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
#include<sstream>
#include<iostream>
using namespace std;

#define memo(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define max(a,b) (a)>(b)?(a):(b)
#define min(a,b) (a)<(b)?(a):(b)
#define eps 1e-8
#define i64 __int64

i64 power(int a,int k){
	if(k==0) return 1;
	if(k==1) return a;
	i64 tmp = power(a,k/2);
	tmp = tmp * tmp;
	if(k & 1) tmp = tmp * a;
	return tmp;
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.ans","w",stdout);
	int t,cs,i,j,k,b[100];
	char a[100];
	i64 ans;
	scanf("%d",&t);
	for(cs=1;cs<=t;cs++){
		scanf("%s",a);
		memo(b,-1);
		b[0]=1;
		for(i=1;a[i];i++){
			if(a[i]==a[0]) b[i]=1;
		}
		for(i=1,k=0;a[i];i++){
			if(b[i]!=-1) continue;
			if(k==1) k++;
			b[i]=k;
			for(j=i+1;a[j];j++){
				if(a[j]==a[i]) b[j]=k;
			}
			k++;
		}
		k = max(k,2);
		for(j=0,ans=0;j<i;j++){
			ans += b[j]*power(k,i-j-1);
		}
		printf("Case #%d: %I64d\n",cs,ans);
	}
	return 0;
}