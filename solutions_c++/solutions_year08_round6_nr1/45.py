#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int a[1111], b[1111], c[1111], d[1111], n1, n2;
char s[1111];

int n, m;
int T;

int main(void)
{
	int l0, l1, l2, l3;
	int t1, t2;

	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		n1 = n2 = 0;
		scanf("%d",&n);
		for(l1=0;l1<n;l1++)
		{
			scanf("%d %d %s",&t1,&t2,s);
			if(s[0] == 'N')
			{
				scanf("%s",s);
				c[n2] = t1;
				d[n2] = t2;
				n2++;
			}
			else
			{
				a[n1] = t1;
				b[n1] = t2;
				n1++;
			}
		}

		sort(a, a+n1);
		sort(b, b+n1);

		printf("Case #%d:\n",l0);
		scanf("%d",&m);
		for(l1=0;l1<m;l1++)
		{
			scanf("%d %d",&t1,&t2);

			int v1 = 3, v2 = 3;

			if(n1 == 0)
			{
				for(l2=0;l2<n2;l2++){ if(c[l2] == t1 && d[l2] == t2){ v1 = v2 = 0; break; } }
			}
			else
			{
				int mx = min(a[0], t1);
				int Mx = max(a[n1-1], t1);
				int my = min(b[0], t2);
				int My = max(b[n1-1], t2);
				for(l2=0;l2<n2;l2++)
				{
					if(mx <= c[l2] && c[l2] <= Mx && my <= d[l2] && d[l2] <= My)
					{
						v1 = v2 = 0;
						goto maki;
					}
				}
				if(a[0] <= t1 && t1 <= a[n1-1]){ v1 = 1; }
				if(b[0] <= t2 && t2 <= b[n1-1]){ v2 = 1; }
			}
maki:
			if(v1 == 1 && v2 == 1) printf("BIRD\n");
			else if(v1 == 0 || v2 == 0) printf("NOT BIRD\n");
			else printf("UNKNOWN\n");
		}
	}
}