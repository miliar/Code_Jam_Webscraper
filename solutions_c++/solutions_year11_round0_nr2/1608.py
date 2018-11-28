#include<iostream>
using namespace std;

int g[30][30];
bool flag[30][30];

void Update(char s[],int &j)
{
	if(j<2) return;

	int ii=s[j-2]-'A',jj=s[j-1]-'A';
	if(g[ii][jj]!=-1)
	{
		j--;
		s[j-1]=g[ii][jj]+'A';
		Update(s,j);
	}
	else
	{
		for(ii=0;ii<j-1;ii++)
			if(flag[s[ii]-'A'][jj])
				break;
		if(ii<j-1)
			j=0;
	}
}
int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("out.txt","w+",stdout);

	int t,test=1,c,d,n,i,j;
	char ch1,ch2,ch3,s[110];
	scanf("%d",&t);
	while(t--)
	{
		memset(g,-1,sizeof(g));
		memset(flag,false,sizeof(flag));
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			getchar();
			scanf("%c%c%c",&ch1,&ch2,&ch3);
			g[ch1-'A'][ch2-'A']=g[ch2-'A'][ch1-'A']=ch3-'A';
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			getchar();
			scanf("%c%c",&ch1,&ch2);
			flag[ch1-'A'][ch2-'A']=flag[ch2-'A'][ch1-'A']=true;
		}
		scanf("%d",&n);
		getchar();
		for(j=0,i=0;i<n;i++)
		{
			scanf("%c",&ch1);
			s[j++]=ch1;
			Update(s,j);
		}
		printf("Case #%d: [",test++);
		for(i=0;i<j-1;i++)
			printf("%c, ",s[i]);
		if(j) printf("%c",s[j-1]);
		printf("]\n");
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}