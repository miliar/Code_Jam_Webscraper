#include<stdio.h>
#include<string.h>

const int maxn = 1000010;
__int64 a, b, p;
char isp[maxn];
int len;
int seg[maxn][2], m;

int fa[maxn];

int getfa(int a)
{
	int b = a, c;
	while(a!=fa[a])
	{
		a = fa[a];
	}
	while(b!=a)
	{
		c = fa[b];
		fa[b] = a;
		b = c;
	}
	return a;
}

void merge(int a, int b)
{
	a = getfa(a);
	b = getfa(b);
	fa[a] = b;
}
int main() {
	__int64 i,j,k;
	__int64 i1,j1;
	memset(isp, 1, sizeof(isp));
	for(i1=2;i1<maxn;i1++)if(isp[i1])
	{
		for(j1=i1*i1;j1<maxn; j1+=i1) isp[j1] = 0;
	}	
	int cs;
	scanf("%d",&cs);
	int step = 1;
	while(cs--)
	{		
		scanf("%I64d%I64d%I64d",&a,&b,&p);		
		len = b - a + 1;
		m = 0;
		for(i=p;i<=len && i<=b;i++) if(isp[i])			
		{
			i1 = i;
			if(i<a) i1 = ((a+i-1)/i)*i;
			if((i1+i)>b) continue;
			seg[m][0] = i1 - a;  //start
			seg[m][1] = i;  //step
			m++;
		}	
		//printf("%d\n", m);
		int ans = 0;
		for(i=0;i<len;i++)
		{
			fa[i] = i;
		}
		for(i=0;i<m;i++)
		{
			for(j=seg[i][0]+seg[i][1]; j<len; j+=seg[i][1])
			{
				merge(seg[i][0], j);
			}
		}
		for(i=0;i<len;i++) if(fa[i]==i) ans++;
		printf("Case #%d: %d\n", step++, ans);
	}
	return 0;
}
