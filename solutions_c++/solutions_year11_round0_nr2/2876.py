#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T,C,D,N;
	int i,j,k;
	int ans[200];
	int m[27][27];
	bool e[27][27];
	int cnt;
	char str[200];

	freopen("D:\\VC2005\\google\\2011\\P2\\p2.in","r",stdin);
	freopen("D:\\VC2005\\google\\2011\\P2\\p2.out","w",stdout);

	scanf("%d\n", &T);
	
	for(i=1;i<=T;i++)
	{
		for(j=0;j<=26;j++)
			for(k=0;k<=26;k++)
			{
				m[j][k] = -99;
				e[j][k] = false;
			}
		scanf("%d", &C);
		if(C>0)
		{
			scanf("%s", str);
			for(j=0;j<C*3;j=j+3)
			{
				m[str[j]-'A'][str[j+1]-'A'] = str[j+2]-'A';
				m[str[j+1]-'A'][str[j]-'A'] = str[j+2]-'A';
			}
		}

		scanf("%d", &D);
		if(D>0)
		{
			scanf("%s", str);
			for(j=0;j<D*2;j=j+2)
			{
				e[str[j]-'A'][str[j+1]-'A'] = true;
				e[str[j+1]-'A'][str[j]-'A'] = true;
			}
		}

		cnt = 0;
		scanf("%d %s\n", &N, str);
		//printf("%d %s\n", N, str);
		for(j=0;j<N;j++)
		{
			if(cnt==0) ans[cnt++] = str[j] - 'A';
			else if(m[ans[cnt-1]][str[j]-'A'] >= 0) ans[cnt-1] = m[ans[cnt-1]][str[j]-'A'];
			else
			{
				bool clear = false;
				for(k=0;k<cnt;k++)
				{
					if(e[ans[k]][str[j]-'A'])
					{
						cnt =0;
						clear = true;
						break;
					}
				}
				if(!clear) ans[cnt++] = str[j] - 'A';
			}
		}

		//printf("cnt=%d\n", cnt);
		printf("Case #%d: [", i);
		for(j=0;j<cnt;j++)
		{
			if(j > 0) printf(", ");
			printf("%c", 'A'+ans[j]);
		}
		printf("]\n");
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
