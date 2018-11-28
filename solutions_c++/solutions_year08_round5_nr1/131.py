#include<stdio.h>
#include<string.h>

#define rint(x) scanf("%d",&x)
#define clr(x,y) memset(x, y, sizeof(x))
#define myabs(x) (((x)<0)?-(x):(x))
#define mymax(x, y) ((x)<(y)?(y):(x))
#define mymin(x, y) ((x)<(y)?(x):(y))

const int maxside = 6006;
const int dir[4][2]={-1,0,0,1,1,0,0,-1};
int L;
struct point {
	int x, y;
};
point p[maxside*maxside];
int n;
int x1[maxside], x2[maxside];
int y1[maxside], y2[maxside];

int main() {
	int cs, step;
	int i,j,k,t,x,y,d;
	char s[100];
	rint(cs);
	for(step=1;step<=cs;step++)
	{
		rint(L);
		x = y = 0;
		d = 1;
		n = 0;
		for(i=0;i<L;i++)
		{
			scanf("%s%d",&s,&t);
			while(t>0)
			{
				t--;
				for(j=0;s[j];j++)
				{
					if(s[j]=='F')
					{
						x += dir[d][0];
						y += dir[d][1];
						p[n].x = x;
						p[n].y = y;
						n++;
					} else if(s[j]=='L')
					{
						d = (d-1+4) % 4;
					}else {
						d = (d+1) % 4;
					}
				}
			}
		}
		__int64 s1 = 0;
		p[n].x = p[0].x; p[n].y = p[0].y;
		for(i=0;i<n;i++)
		{
			s1 += (p[i].x)*p[i+1].y - p[i].y*p[i+1].x;
		}
		s1 /= 2;
		s1 = myabs(s1);

		//printf("%d\n", s1);
		int minx=p[0].x, miny=p[0].y;
		for(i=0;i<n;i++){
			if(p[i].x<minx) minx=p[i].x;
			if(p[i].y<miny) miny=p[i].y;
		}
		for(i=0;i<maxside;i++)
		{
			x1[i] = 1000000;
			y1[i] = 1000000;
			x2[i] = -1000000;
			y2[i] = -1000000;
		}
		int maxx = 0; int maxy1=0;
		for(i=0;i<n;i++){
			p[i].x-=minx;
			p[i].y-=miny;
			if(p[i].y<x1[p[i].x]) x1[p[i].x] = p[i].y;
			if(p[i].y>x2[p[i].x]) x2[p[i].x] = p[i].y;
			if(p[i].x<y1[p[i].y]) y1[p[i].y] = p[i].x;
			if(p[i].x>y2[p[i].y]) y2[p[i].y] = p[i].x;
			if(p[i].x>maxx) maxx=p[i].x;
			if(p[i].y>maxy1) maxy1=p[i].y;
		}
		int s2 = 0;
/*			int y1 = x1[i];
			int y2 = x2[i];
			int y3 = x1[i+1];
			int y4 = x2[i+1];
*/
		int y1 = x1[0];
		for(i=1;i<=maxx;i++)
		{
			s2 += y1;			
			if(x1[i]<y1) y1 = x1[i];
		}
		y1 = x1[maxx];
		for(i=maxx-1;i>=0;i--)
		{
			s2 += y1;			
			if(x1[i]<y1) y1 = x1[i];
		}

		int y2 = x2[0];
		for(i=1;i<=maxx;i++)
		{
			s2 += (maxy1 - y2);
			if(x2[i]>y2) y2 = x2[i];
		}
		y2 = x2[maxx];
		for(i=maxx-1;i>=0;i--)
		{
			s2 += (maxy1 - y2);
			if(x2[i]>y2) y2 = x2[i];
		}

		s2 = maxx*maxy1 - s2;

		double ans = 0;
		printf("Case #%d: %d\n", step, ((int)(s2-s1)));
	}
	return 0;
}