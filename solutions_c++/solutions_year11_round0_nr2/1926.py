#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;


struct Magic
{
	char qu[111];
	int length;
	int apr[30];
	int opp[30][30];
	char comb[30][30];
	int clearall()
	{		
		memset(opp,0,sizeof(opp));
		memset(comb,0,sizeof(comb));
		clear();
		return 0;
	}
	int clear()
	{
		length=0;
		memset(apr,0,sizeof(apr));
		memset(qu,0,sizeof(qu));
		return 0;
	}
	int add(char ch)
	{
		int i;
		ch-='A'-1;
		if (length==0) 
		{
			qu[length++]=ch;
			apr[ch]++;
			return 0;
		}
		else
			if (comb[qu[length-1]][ch])
			{
				qu[length-1]=comb[qu[length-1]][ch];
			//	if (apr[qu[length-1]]) apr[qu[length-1]]--;
			}
			else
			{
				bool flag=true;
				for (i=0;i<length;i++)
				{
					if (opp[ch][qu[i]])
					{
						clear();
						flag=false;
						break;
					}
				}
				if (flag)
				{
					qu[length++]=ch;
					apr[ch]++;
				}
			}
		return 0;
	}
	void output()
	{
		printf("[");
		if (length>0)
		{
			printf("%c",qu[0]+'A'-1);
			for (int i=1;i<length;i++)
			{
				printf(", %c",qu[i]+'A'-1);
			}
		}
		printf("]\n");
	}
};
const int dd = 'A'-1;
int main()
{
	int T,N,C,D,ti,ci,di;
	int i,j;
	Magic mm;
	char scom[5];
	char str[200];
	freopen("d:\\B-small-attempt1.in","r",stdin);
	freopen("d:\\bout11.txt","w",stdout);
	scanf("%d",&T);
	for (ti=0;ti<T;ti++)
	{
		mm.clearall();
		scanf("%d",&C);
		for (ci=0;ci<C;ci++)
		{
			scanf("%s",scom);
			mm.comb[scom[0]-dd][scom[1]-dd]=mm.comb[scom[1]-dd][scom[0]-dd]=scom[2]-dd;
		}
		scanf("%d",&D);
		for (di=0;di<D;di++)
		{
			scanf("%s",scom);
			mm.opp[scom[0]-dd][scom[1]-dd]=mm.opp[scom[1]-dd][scom[0]-dd]=1;
		}
		scanf("%d",&N);
		scanf("%s",str);
		for (i=0;i<N;i++)
		{
			mm.add(str[i]);
		//	mm.output();
		}
		printf("Case #%d: ",ti+1);
		mm.output();
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}

