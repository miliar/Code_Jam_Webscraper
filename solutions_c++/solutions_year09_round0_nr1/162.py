#include <iostream>

using namespace std;

bool vst[20][256];
char buf[5010][20];
char tmp[100000];
int main()
{
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	int i;
	for(i=0;i<d;i++) scanf("%s",buf[i]);
	for(i=0;i<n;i++)
	{
		memset(vst,0,sizeof(vst));
		scanf("%s",tmp);
		int j;
		int cj=0;
		bool L=false;
		for(j=0;tmp[j];j++)
		{
			if(tmp[j]=='(') 
			{
				L=true;
				continue;
			}
			if(tmp[j]==')')
			{
				cj++;
				L=false;
				continue;
			}
			vst[cj][tmp[j]]=true;
			if(!L) cj++;
		}
		int sum=0;
		for(j=0;j<d;j++)
		{
			int k;
			bool ok=true;
			for(k=0;buf[j][k];k++)
			{
				if(!vst[k][buf[j][k]])
				{
					ok=false;
					break;
				}
			}
			if(ok) sum++;
		}
		printf("Case #%d: %d\n",i+1,sum);
	}
	return 0;
}

