#include <cstdio>
#include <cstring>
#define oo 5005
#define ll 17
char s[oo][ll];
char tmp[ll*26];
bool mk[ll][26];
int L,D,N;

inline void Readin()
{
	scanf("%d%d%d",&L,&D,&N);
	for (int i=1;i<=D;++i)
		scanf("%s",s[i]);
}

inline void Solve()
{
	for (int i=1;i<=N;++i)
	{
		memset(mk,0,sizeof mk);
		scanf("%s",tmp);
		char *ch=tmp;
		int cnt=0;
		
		while (*ch)
		{
			if (*ch!='(' && *ch!=')')
				mk[cnt][*ch-'a']=true;
			else{
				++ch;
				while (*ch!=')')
				{
					mk[cnt][*ch-'a']=true;
					++ch;
				}
			}
			
			++ch,++cnt;
		}
		
		cnt=0;
		for (int j=1;j<=D;++j)
		{
			bool flag=true;
			for (int k=0;k<L;++k)
				flag&=mk[k][s[j][k]-'a'];
			cnt+=flag;
		}
		
		printf("Case #%d: %d\n",i,cnt);
	}
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	Readin();
	Solve();
	
	return 0;
}
