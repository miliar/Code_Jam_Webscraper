#include <stdio.h>
#define N 200
char s[N];
int p[N], m[N], u[N];
int main()
{
	int i, j, b, t, l, ts;
	__int64 r;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(i=0; i<N; m[i]=0, p[i]=-1, u[i]=0, i++);
		for(scanf("%s", s), l=0; s[l]; s[l]=(s[l]>='0' && s[l]<='9')?s[l]-'0':s[l]+10-'a', l++);
		for(b=0, i=0; i<l; i++)
		{
			if(p[s[i]]!=-1) m[i]=p[s[i]];
			else
			{
				for(j=i==0; j<N && u[j]; j++);
				p[s[i]]=j;
				u[j]=1;
				m[i]=j;
				b++;
			}
		}
		if(b==1) b=2;
		for(r=0, i=0; i<l; r=r*b+m[i], i++);
		printf("Case #%d: %I64d\n", t+1, r);
	}
	return 0;
}