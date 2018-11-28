#include <stdio.h>
#define N 55
char m[N][N];
int n, k;
bool is(char c)
{
	int i, j, s, l, r=0;
	for(i=0; i<n; i++)
		for(l=0, j=0; j<n; r=l>r?l:r, j++)
			if(m[i][j]==c) l++;
			else l=0;
	for(j=0; j<n; j++)
		for(l=0, i=0; i<n; r=l>r?l:r, i++)
			if(m[i][j]==c) l++;
			else l=0;
	for(s=0; s<=2*n; s++)
		for(l=0, i=0; i<n; r=l>r?l:r, i++)
		{
			j=s-i;
			if(j>=0 && j<n && m[i][j]==c) l++;
			else l=0;
		}
	for(s=-n; s<=n; s++)
		for(l=0, i=0; i<n; r=l>r?l:r, i++)
		{
			j=s+i;
			if(j>=0 && j<n && m[i][j]==c) l++;
			else l=0;
		}
	return r>=k;
}
int main()
{
	int i, j, l, t, ts, r, b;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d", &n, &k), i=0; i<n; scanf("%s", m[i]), i++);
		for(i=0; i<n; i++)
		{
			for(j=n-1, l=n-1; j>=0; j--)
				if(m[i][j]!='.') m[i][l--]=m[i][j];
			for(; l>=0; m[i][l]='.', l--);
		}
		r=is('R');
		b=is('B');
		printf("Case #%d: ", t+1);
		if(r && b) printf("Both\n");
		else if(r && !b) printf("Red\n");
		else if(!r && b) printf("Blue\n");
		else printf("Neither\n");
	}
	return 0;
}