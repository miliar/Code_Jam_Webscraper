#include<stdio.h>
#include<vector>
using namespace std;

#define MAX 3005

#define INF 1000000000

#define left(x)		((x+1)%4)
#define right(x)	((x-1+4)%4)

#define _min(a,b)	(((a)<(b))?(a):(b))
#define _max(a,b)	(((a)>(b))?(a):(b))

struct Point{
	int x,y;
	Point(int _x=0,int _y=0){
		x=_x;
		y=_y;
	}
};

int x1,x2;

vector<Point> q,p;

int xmin[2*MAX],xmax[2*MAX];
int ymin[2*MAX],ymax[2*MAX];

int yy1[2*MAX],yy2[2*MAX];
int yy3[2*MAX],yy4[2*MAX];

//>>>>>>>>>>>  L L L L >>>
////////////N  W  S E
int _x[] = {0,-1, 0,1};
int _y[] = {1, 0,-1,0};

int a;

void draw(){
	char s[33];
	int rep;
	int x,y,i,n,k,j,l,m;
	int dir;

	q.clear();
	scanf("%d",&n);

	x = 0;
	y = 0;
	dir = 0;

	q.push_back(Point(0,0));

	while(n--){
		scanf("%s%d",s,&rep);
		
		while(rep--){

			for(i=0;s[i];i++){
				if(s[i]=='L')
					dir = left(dir);
				else if(s[i]=='R')
					dir = right(dir);
				else{
					x += _x[dir];
					y += _y[dir];

					if(xmax[MAX+y] < x)	xmax[MAX+y] = x;
					if(xmin[MAX+y] > x) xmin[MAX+y] = x;

					if(x2 < x) x2 = x;
					if(x1 > x) x1 = x;

					if(ymax[MAX+x] < y)	ymax[MAX+x] = y;
					if(ymin[MAX+x] > y) ymin[MAX+x] = y;

					q.push_back(Point(x,y));
				}
			}
		}
	}

	q.pop_back();

	k = -1;
	for(i=0;i<q.size();i++){
		if(k==-1 || (q[i].y < q[k].y) || (q[i].y==q[k].y && q[i].x < q[k].x) )
			k = i;
	}
	
	p.clear();

	n = q.size();

	for(i=0;i<n;i++){
		j = (i+k)%n;
		l = (j+1)%n;
		m = (l+1)%n;

		if(q[j].x == q[l].x && q[l].x == q[m].x)
			continue;
		if(q[j].y == q[l].y && q[l].y == q[m].y)
			continue;

		p.push_back(q[l]);
	}

//	for(i=0;i<p.size();i++)
//		printf(">> %d %d\n",p[i].x,p[i].y);

	a = 0;
	for(i=0;i<p.size();i++){
		j= (i+1)%p.size();
		a += p[i].x*p[j].y - p[j].x*p[i].y;
	}
	if(a < 0)a=-a;
	a/=2;
}

int main(){
	int T,N;
	int x;
	int maxy,x0;
	int ry1,ry2;

	int b;

	scanf("%d",&T);

	for(N=1;N<=T;N++){

		for(x=0;x<=2*MAX;x++){
			xmax[x] = -INF;
			xmin[x] = INF;
			ymax[x] = -INF;
			ymin[x] = INF;
		}

		x1 = INF;
		x2 = -INF;

		draw();

		maxy = INF;
		x0 = -1;
		
		for(x=x1;x<=x2;x++){
//			printf(">>> %d %d\n",ymax[MAX+x],ymin[MAX+x]);
			if(ymax[MAX+x]-ymin[MAX+x] > maxy){
				x0 = x;
				maxy = ymax[MAX+x]-ymin[MAX+x];
			}
		}

		b = 0;

		ry1 = ymin[MAX+x1];
		ry2 = ymax[MAX+x1];

		for(x=x1;x<=x2;x++){
			if(ymin[MAX+x] < ry1)
				ry1 = ymin[MAX+x];
			if(ymax[MAX+x] > ry2)
				ry2 = ymax[MAX+x];
			
			yy1[MAX+x] = ry1;
			yy2[MAX+x] = ry2;
		}

		ry1 = ymin[MAX+x2];
		ry2 = ymax[MAX+x2];

		for(x=x2;x>=x1;x--){
			if(ymin[MAX+x] < ry1)
				ry1 = ymin[MAX+x];
			if(ymax[MAX+x] > ry2)
				ry2 = ymax[MAX+x];
			
			yy3[MAX+x] = ry1;
			yy4[MAX+x] = ry2;
		}

		b = 0;
		for(x=x1;x<x2;x++){
			b += _min(yy2[MAX+x] , 	yy4[MAX+x+1]) - _max(yy1[MAX+x],yy3[MAX+x+1]);

//			printf(">>> %d %d %d %d\n",
		}

//		printf(">>> %d\n",a);

		printf("Case #%d: %d\n",N,b-a);
		
	}
	return 0;
}