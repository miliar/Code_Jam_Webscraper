#include<iostream>
#include<string.h>
using namespace std;
char ch[55000][20];
bool cal[10000][27];
int L,D,N;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i,j,k,t;
	scanf("%d%d%d", &L, &D, &N);
	for(i=0; i<D; i++)
		scanf("%s", ch[i]);
	char a[10000];
	for(int ca=1; ca<=N; ca++)
	{
		scanf("%s", a);
		int ls = 0;
		memset(cal, 0, sizeof(cal));
		
		for(i=0;a[i]; )
		{
			if( a[i]=='(' )
			{
				for(k=0,j=i+1;a[j]!=')'; j++, k++)
				{
					cal[ls][a[j]-'a' ] = true;
				}
				i = j+1;
			}
			else
			{
				cal[ls][a[i] - 'a' ] = true;
				i++;
			}
			ls++;
		}
		k = 0;
		for(j=0; j<D; j++)
		{
			for(t =0; t<L; t++)
				if( !cal[t][ch[j][t]-'a'] ) break;
			if( t == L) k++;
		}
		printf("Case #%d: %d\n", ca, k);
	}
	return 0;
}
