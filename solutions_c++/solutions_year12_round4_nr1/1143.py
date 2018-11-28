#include<cstdio>
#include<cstring>

int T;
int n;
int d[20000],l[20000],D;
int x[20000],list[20000],len;
bool now[20000];
bool flag;
int max,t,ll,rr;

int min(int x,int y)
{
    if (x < y) return x; else return y;
}

int abs(int x)
{
    if (x < 0) return -x; else return x;
}

int main()
{
	scanf("%d",&T);
	for(int I = 1;I <= T;I++)
	{
		scanf("%d",&n);
		for(int i = 0;i < n;i++) scanf("%d%d",d+i,l+i);
		scanf("%d",&D);
		memset(x,255,sizeof(x));
		memset(now,0,sizeof(now));
		flag = false;
		x[0] = d[0];
		list[0] = 0;
		now[0] = true;
		len = 1;
		while(len > 0)
		{
		    max = 0;
		    for(int i = 1;i < len;i++)
		    if (x[list[i]] > x[list[max]]) max = i;
		    t = list[max];
		    len--;
		    list[max] = list[len];
		    now[t] = false;
		    ll = t;
		    while(ll > 0 && d[t]-d[ll-1]<=x[t]) ll--;
		    rr = t;
		    while(rr < n-1 && d[rr+1]-d[t]<=x[t]) rr++;
		    for(int i = ll;i <= rr;i++)
		    {
		        int dist = min(l[i],abs(d[i]-d[t]));
		        if (x[i] < dist)
		        {
		            x[i] = dist;
		            if (!now[i])
		            {
		                now[i] = true;
		                list[len] = i;
		                len++;
		            }
		        }
		    }
		}
		for(int i = 0;i < n;i++) if (x[i]+d[i] >= D) flag = true;
		printf("Case #%d: ",I);
		if (flag) puts("YES"); else puts("NO");
	}
	return 0;
}
