#include<stdio.h>

const int maxn = 10000;

typedef char sir[500];

sir S[maxn];
int L,N,D;


bool ver(sir &a,sir &b)
{
	int poz = 0;
//	printf("%s %s\n",a,b);
	for(int i = 0;i < L; ++i)
	{
		if (b[poz] == '(')
		{
			int ver = 0;
			while(b[poz] != ')')
			{
				++poz;
				if (b[poz] == a[i]) ver = 1;
			}
			if (!ver) return 0;
		}
		else if (a[i] != b[poz]) return 0;
		
		++poz;
	}
	return 1;
}


int main()
{
	freopen("alien.in","r",stdin);
	freopen("alien.out","w",stdout);
	scanf("%d %d %d\n",&L,&D,&N);
	for(int i = 1;i <= D; ++i)
			scanf("%s",S[i]);
	for(int i = 1;i <= N; ++i)
	{
			sir s;
			scanf("%s",s);
			int nr = 0;
			for(int j = 1;j <= D; ++j) nr += ver(S[j],s);
			printf("Case #%d: %d\n",i,nr);
	}
	return 0;
}



