#include <stdio.h>
#include <string.h>

char hashTable[1100][110];
int visited[1100]={0};
int Hash(char *a)
{
	int sum=0;
	for(int i=0;i<strlen(a);i++)
		sum+=a[i]*a[i]*(2*i+1);
	sum=sum%1001;
	while(hashTable[sum][0]!=0&&strcmp(a,hashTable[sum])!=0)
		sum=(sum+1)%1001;
	if(hashTable[sum][0]==0)
		strcpy(hashTable[sum],a);
	return sum;
}
int main()
{
	int aCase,k;
	char a[110][1010],b[1100][1100];
	int cA,cB;
	scanf("%d",&aCase);
	getchar();
	for(int k=1;k<=aCase;k++)
	{
		scanf("%d",&cA);
		getchar();
		for(int i=0;i<cA;i++)
			gets(a[i]);
		scanf("%d",&cB);
		getchar();
		for(int i=0;i<cB;i++)
			gets(b[i]);
		memset(hashTable,0,sizeof(hashTable));
		memset(visited,0,sizeof(visited));
		int count=0;
		int pB;
		int v[1100]={0};
		int cnt=0;
		for(int i=0;i<cB;i++)
		{
			pB=Hash(b[i]);
			if(v[pB]==0)
				count++;
			v[pB]++;
			if(count==cA)
			{
				memset(v,0,sizeof(v));
				count=0;
				cnt++;	
				v[pB]++;
				count=1;
			}		
		}
		printf("Case #%d: %d\n",k,cnt);
	}
	return 0;
}
