#include<stdio.h>

int L, N, M;

char a[16];
int A[5000][16];
char b[10000];
int pat[16][26];

int main(void)
{
	int l1, l2, l3;

	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);

	scanf("%d %d %d",&L,&N,&M);
	for(l1=0;l1<N;l1++)
	{
		scanf("%s",a);
		for(l2=0;l2<L;l2++)
		{
			A[l1][l2] = a[l2] - 'a';
		}
	}

	for(l1=0;l1<M;l1++)
	{
		printf("Case #%d: ",l1+1);

		for(l2=0;l2<L;l2++) for(l3=0;l3<26;l3++) pat[l2][l3] = 0;

		scanf("%s",b);
		l3 = 0;
		for(l2=0;l2<L;l2++,l3++)
		{
			if(b[l3] == '(')
			{
				l3++;
				while(1)
				{
					if(b[l3] == ')') break;
					pat[l2][b[l3]-'a'] = 1;
					l3++;
				}
			}
			else
			{
				pat[l2][b[l3]-'a']=1;
			}
		}

		int ret = 0;
		for(l2=0;l2<N;l2++)
		{
			for(l3=0;l3<L;l3++)
			{
				if(pat[l3][A[l2][l3]] == 0) break;
			}
			if(l3 == L) ret++;
		}
		printf("%d\n",ret);
	}
	return 0;
}