#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

int N;
char num[333];
void test()
{
	scanf("%s",num);
	N=strlen(num);
	int i,j,mj;
	for(i=N-2;i>=0;i--) if(num[i]<num[i+1]) break;

	if(i>=0)
	{
		mj=N-1;
		for(j=N-2;j>i;j--) if(num[j]>num[i]&&(num[j]<num[mj]||num[mj]<=num[i])) mj=j;
		swap(num[i],num[mj]);
		sort(num+i+1,num+N);
	}
	else 
	{
		i=N-1;
		while(num[i]=='0') i--;
		swap(num[i],num[0]);
		num[N]='0';
		num[N+1]=0;
		N++;
		sort(num+1,num+N);
	}
	printf("%s\n",num);
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int t=0,T;

	scanf("%d",&T);

	for(t=0;t<T;t++)
	{
		printf("Case #%d: ",t+1);
		test();
	}
}