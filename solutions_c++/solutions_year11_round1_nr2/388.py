#include <cstdio>
#include <cassert>
#include <cstring>

const int MAXL=125,MAXN=125,MAXM=125;

int N,M,T;
char str[MAXN][MAXL];
char ord[512];
int L[MAXN];
int contain[MAXN][512];
int used[512];
bool possible[MAXN];
bool have[MAXL];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d:",tt);
		scanf("%d%d",&N,&M);
		memset(str,0,sizeof(str));
		for(int i=0;i<N;i++)
			scanf(" %s",str[i]);
		memset(contain,0,sizeof(contain));
		memset(L,0,sizeof(L));
		for(int i=0;i<N;i++)
		{
			L[i]=strlen(str[i]);
			for(int j=0;j<L[i];j++)
				contain[i][str[i][j]]++;
		}
		for(int i=0;i<M;i++)
		{
			scanf(" %s",ord);
			assert(strlen(ord)==26);
			int ans=-1,rj;
			int now,left;
			for(int j=0;j<N;j++)
			{
				now=0,left=L[j];
				int *in=contain[j];
				memset(possible,false,sizeof(possible));
				memset(used,0,sizeof(used));
				for(int k=0;k<N;k++)
					if (L[k]==L[j])
					{
						possible[k]=true;
						for(int p=0;p<L[k];p++)
							used[str[k][p]]++;
					}
				for(int k=0;k<26;k++)
					if (used[ord[k]])
					{
						if (in[ord[k]])
						{
							left-=in[ord[k]];
							if (left==0)
								break;
							int ttt=0;
							memset(have,0,sizeof(have));
							for(int s=0;s<L[j];s++)
								if (str[j][s]==ord[k])
								{
									have[s]=true;
									ttt++;
									for(int p=0;p<N;p++)
										if (possible[p] && str[p][s]!=ord[k])
										{
											possible[p]=false;
											for(int q=0;q<L[p];q++)
												used[str[p][q]]--;
										}
								}
							for(int p=0;p<N;p++)
								if (possible[p])
									for(int q=0;q<L[q];q++)
										if (str[p][q]==ord[k] && !have[q])
										{
											possible[p]=false;
											for(int q=0;q<L[p];q++)
												used[str[p][q]]--;
											break;
										}
							assert(ttt==in[ord[k]]);
						}
						else
						{
							now++;
							for(int p=0;p<N;p++)
								if (possible[p] && contain[p][ord[k]])
								{
									possible[p]=false;
									for(int q=0;q<L[p];q++)
										used[str[p][q]]--;
								}
						}
					}
				if (now>ans)
				{
					ans=now,rj=j;
				}
			}
			printf(" %s",str[rj]);
		}
		printf("\n");
	}
	return 0;
}
