#include <iostream>
using namespace std;

char w[5000][20];
bool can[100][500];
char buf[10000];

int main()
{
	int L,D,N;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d%d%d\n",&L,&D,&N);
	for (int i=0;i<D;i++)
		gets(w[i]);
	
	for (int i=0;i<N;i++)
	{
		int res=0;
		gets(buf);
		char* c=buf;
		memset(can,0,sizeof(can));
		for (int j=0;j<L;j++)
		{
			if (*c=='(')
			{
				++c;
				while (*c!=')')
				{
					can[j][*c]=true;
					++c;
				}
				++c;
			}
			else
			{
				can[j][*c]=true;
				++c;
			}
		}

		for (int j=0;j<D;j++)
		{
			++res;
			for (int k=0;k<L;k++)
			{
				if (!can[k][w[j][k]])
				{
					--res;
					break;
				}
			}
		}

		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}