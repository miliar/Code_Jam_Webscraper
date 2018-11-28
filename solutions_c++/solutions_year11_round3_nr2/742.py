#include<stdio.h>
#include<algorithm>
using namespace std;
#define MAXN 1000099
__int64 list1[MAXN],list2[MAXN],cc[MAXN];
__int64 cmp(__int64 a,__int64 b)
{
	return a>b;
}
int main()
{
	__int64 sum,t,t1,l,c,n,i,j,k,ca=1;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B1.txt","w",stdout);
	scanf("%I64d",&t);
	while(t--){
		sum=0;
		scanf("%I64d%I64d%I64d%I64d",&l,&t1,&n,&c);
		for(i=0;i<c;i++)
			scanf("%I64d",&cc[i]);

		for(i=0;i<n;i++){
			list2[i]=list1[i]=cc[i%c];
			sum+=list1[i]*2;
		}
		__int64 tmp=t1/2,s1=0;
		for(i=0;i<n;i++){
			s1+=list1[i];
			if(s1==tmp)
				break;
			else if(s1>tmp){
				list2[i]=s1-tmp;
				break;
			}
		}
		sort(list2+i,list2+n,cmp);
		__int64 s2=0;
		for(j=i;j<l+i;j++)
			s2+=list2[j];
		printf("Case #%I64d: %I64d\n",ca++,sum-s2);
	}
	return 0;
}