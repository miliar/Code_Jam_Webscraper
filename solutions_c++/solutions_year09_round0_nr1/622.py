#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int L,D,N;

char str[5005][16];
char mymap[16][32];

void init()
{
	int i,j;
	for (i=0;i<D;i++)
	{
		scanf("%s",str[i]);
	}
}

void process(int nCase)
{
	int i,j;
	char mystr[1000];
	scanf("%s",mystr);
	memset(mymap,0,sizeof(mymap));
	int pos=0;
	for(i=0;i<L;i++)
	{
		if (mystr[pos]=='(')
		{
			pos++;
			while (mystr[pos]!=')')
			{
				mymap[i][mystr[pos]-'a']=1;
				pos++;
			}
			pos++;
		}
		else
		{
			mymap[i][mystr[pos]-'a']=1;
			pos++;
		}
	}
	int ans=0;
	for (i=0;i<D;i++)
	{
		int flag=1;
		for (j=0;j<L;j++)
		{
			if (mymap[j][str[i][j]-'a']==0)
			{
				flag=0;
				break;
			}
			else
			{
			}
		}
		ans+=flag;
	}
	printf("Case #%d: %d\n",nCase,ans);
}

int main()
{
	int i,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d %d %d\n",&L,&D,&N);
	init();
	for(i=1;i<=N;i++)
	{
		process(i);
	}
	return 0;
}