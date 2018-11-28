
#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t,k,i,j,g,q;
	char com[38][4],clear[30][3];
	char ans[105];
	int c,d,n;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{

		scanf("%d",&c);
		for(i=1;i<=c;i++)
		{
			scanf("%s",com[i]);
		}
		scanf("%d",&d);
		for(i=1;i<=d;i++)
		{
			scanf("%s",clear[i]);
		}
		scanf("%d",&n);
		scanf("%s",ans);
		for(i=0;i<n;i++)
		{
			for(j=1;j<=c;j++)
			{
				if(i==0) break;
				if((ans[i-1]==com[j][0]&&ans[i]==com[j][1])||(ans[i-1]==com[j][1]&&ans[i]==com[j][0]))
				{
					ans[i-1]=com[j][2];
					ans[i]=' ';
					goto ll;
				}
			}
			
			for(j=1;j<=d;j++)
			{
				for(g=0;g<=i-1;g++)
				{
					if(ans[g]==' ') continue;
					if((ans[g]==clear[j][0]&&ans[i]==clear[j][1])||(ans[g]==clear[j][1]&&ans[i]==clear[j][0]))
					{
						for(q=0;q<=i;q++) ans[q]=' ';
						goto ll;
					}
				}
			}	
ll:;
		}
		printf("Case #%d: [",k);
		int size=0;
		for(i=0;i<n;i++)
		{
			if(size==0&&ans[i]!=' ') {cout<<ans[i];size=1;}
			else if(ans[i]!=' ') cout<<", "<<ans[i];
		}
		cout<<"]"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}


