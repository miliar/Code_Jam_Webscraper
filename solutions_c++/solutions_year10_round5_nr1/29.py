#include <stdio.h>
#include <set>
using namespace std;
#define N 1000010
#define K 20
#define I __int64
int p[N], h[K];
I a[K][3];
I pw(I n, I m, int p)
{
	I r;
	for(r=1; p; n=(n*n)%m, p/=2)
		if(p&1) r=(r*n)%m;
	return r;
}
I inv(I n, I m)
{
	return pw(n, m, m-2);
}
set <int> s;
int main()
{
	int i, j, k, n, t, ts, q, l, r, f, e;
	I m, x, A, B;
	for(i=2; i*i<N; i++)
		if(!p[i])
			for(j=i*i; j<N; p[j]=1, j+=i);
	for(j=0, i=2; i<N; i++)
		if(!p[i]) p[j++]=i;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d", &j, &n), i=0; i<n; scanf("%d", &h[i]), i++);
		if(n>=2 && h[0]==h[1])
		{
			printf("Case #%d: %d\n", t+1, h[0]);
			continue;
		}
		for(q=1; j; q*=10, j--);
		s.clear();
		for(f=0, e=0; p[e]<=q; e++)
		{
			m=p[e];
			for(j=0; j<n && h[j]<m; j++);
			if(j<n) continue;
			for(i=0; i<n-1; a[i][0]=h[i], a[i][1]=1, a[i][2]=h[i+1], i++);
			for(r=0, i=0; i<n-1; i++)
			{
				for(j=0; j<2 && !a[i][j]; j++);
				if(j==2)
					if(a[i][j]) break;
					else continue;
				r++;
				for(k=i+1; k<n-1; k++)
					if(a[k][j])
						for(x=a[k][j]*inv(a[i][j], m)%m, l=0; l<3; a[k][l]=((a[k][l]-x*a[i][l])%m+m)%m, l++);
			}
			if(i<n-1) continue;
			if(r<2) { f=2; break; }
			for(i=n-2; i>=0; i--)
			{
				for(j=0; j<2 && !a[i][j]; j++);
				if(j==2) continue;
				if(j==0) A=inv(a[i][j], m)*a[i][2]%m;
				else B=inv(a[i][j], m)*a[i][2]%m;
				for(k=i-1; k>=0; k--)
					if(a[k][j])
						for(x=a[k][j]*inv(a[i][j], m)%m, l=0; l<3; a[k][l]=((a[k][l]-x*a[i][l])%m+m)%m, l++);
			}
			s.insert((A*h[n-1]+B)%m);
		}
		printf("Case #%d: ", t+1);
		if(f==2 || s.size()>1) printf("I don't know.\n");
		else printf("%d\n", *s.begin());
	}
	return 0;
}