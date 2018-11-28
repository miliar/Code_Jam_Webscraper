#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<cstring>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<cmath>
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t, n, k, a[31];
    scanf("%d",&t);
    for(int i=1; i<=t; i++){
        scanf("%d%d",&n,&k);
        int r = (1<<n);
        int t = k/r;
        bool ok = true;
        if( k-t*r==r-1 ) ok = true;
        else ok = false;
        printf("Case #%d: %s\n",i,ok?"ON":"OFF");
    }
    return 0;
}


/*struct Point{ double x, y; };

const double eps = 1e-8, PI = 3.1415926535897932384626433832795;

bool Equal( double s, double t ){ return fabs(s-t)<eps; }
double Slope( double x1, double y1, double x2, double y2 ){
	return ( fabs(x2-x1)<eps ? 1e30:(y2-y1)/(x2-x1) );
}
//bool Between( double x, double l, double r ){ return ( x>=min(l,r)-eps && x<=max(l,r)+eps ); }
bool Equation( double a, double b, double c, double &x1, double &x2 ){
	double dt = b*b-4*a*c;
	if( dt < 0 ) return false;
	x1 = (-b+sqrt( fabs(dt) ))/(2*a);
	x2 = (-b-sqrt( fabs(dt) ))/(2*a);
	return true;
}

class Line{
public:
	double x1, y1, x2, y2;
	Line( double X1=0, double Y1=0, double X2=0, double Y2=0 ){
		x1 = X1; y1 = Y1; x2 = X2; y2 = Y2;
	}
	Line( Point s, Point t ){ x1 = s.x; y1 = s.y; x2 = t.x; y2 = t.y; }
	void Set( double X1, double Y1, double X2, double Y2){
		x1 = X1; y1 = Y1; x2 = X2; y2 = Y2;
	}
	void Set( Point s, Point t ){ x1 = s.x; y1 = s.y; x2 = t.x; y2 = t.y; }
};

class Circle{
public:
    double x, y, z, r;
    void Intersect( Line s, Point &p1, Point &p2 ){
        if( Equal( s.x1, s.x2)){
            p1.x = p2.x = s.x1;
            double tmp = sqrt( r*r-(s.x1-x)*(s.x1-x) );
            p1.y = y+tmp;
            p2.y = y-tmp;
        }
        else{
            double k = Slope( s.x1, s.y1, s.x2, s.y2 );
            double b = s.y1-k*s.x1;
            Equation( 1+k*k, 2*k*(b-y)-2*x, (b-y)*(b-y)+x*x-r*r, p1.x, p2.x );
            p1.y = k*p1.x+b;
            p2.y = k*p2.x+b;
        }
    }
    void Intersect( Circle t, Point &p1, Point &p2 ){
        Line s;
        const double INF = 1e20;
        if( Equal( x, t.x )){
            double Y = ( r*r-t.r*t.r+t.x*t.x-x*x+t.y*t.y-y*y )/(2*t.y-2*y);
            s.Set( -INF, Y, INF, Y );
        }
        else if( Equal( y, t.y )){
            double X = ( r*r-t.r*t.r+t.x*t.x-x*x+t.y*t.y-y*y )/(2*t.x-2*x);
            s.Set( X, -INF, X, INF );
        }
        else{
            double X = ( r*r-t.r*t.r+t.x*t.x-x*x+t.y*t.y-y*y )/(2*t.x-2*x);
            double Y = ( r*r-t.r*t.r+t.x*t.x-x*x+t.y*t.y-y*y )/(2*t.y-2*y);
            if( fabs(X)<eps && fabs(Y)<eps ) s.Set( 0, 0, 1, 1 );
            else s.Set( 0, Y, X, 0 );
        }
        Intersect( s, p1, p2 );
    }
};

double Distance( double x, double y ){ return sqrt(x*x+y*y); }

int main(){
    const int N = 28;
    int t, n; Point p[N*N]; Circle c[N];
    scanf("%d",&t);
    while( t-- ){
        scanf("%d",&n);
        for(int i=0; i<n; i++)
            scanf("%lf%lf%lf",&c[i].x,&c[i].y,&c[i].r);
        int pn = 0;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if( Distance(c[i].x-c[j].x,c[i].y-c[j].y)>c[i].r+c[j].r+eps ) continue;
                c[i].Intersect( c[j], p[pn], p[pn+1] );
                if( Equal(p[pn].x,p[pn+1].x) && Equal(p[pn].y,p[pn+1].y) ) pn+=1;
                else pn+=2;
            }
        }
        for(int i=0; i<pn; i++) printf("%.2f %.2f\n",p[i].x,p[i].y);
    }
    return 0;
}*/


/*#include<iostream>
using namespace std;
#define N 200008
const int INF=0x7FFFFFF;
//#define Min(a,b) (a<b?(a):(b))
//#define Max(a,b) (a>b?(a):(b))

typedef struct{
	int v,w,next;
}Link;
Link  V[3*N];
int p[N],dis[N],x[N];
int head,tail,q[8*N];

class tree{
private:
	int n,end;
	bool vis[N];
public:
	bool init();
	void insert(int,int,int);
	void bfs(int);
	void treeup(int);
	void treedown(int);
	void dfs();
	void ans();
};
bool tree::init()
{
	if(scanf("%d",&n)==EOF) return false;
	int i,j,k,r;
	for(i=0;i<=n;i++) V[i].next=0;
	for(end=n,i=1;i<n;i++){
		scanf("%d%d%d",&j,&k,&r);
		insert(j,k,r);
		insert(k,j,r);
	}
	return true;
}
void tree::insert(int u,int v,int w)
{
	end++;
	V[end].v=v;
	V[end].w=w;
	V[end].next=V[u].next;
	V[u].next=end;
}
void tree::bfs(int s)
{
	int i,j,k;
	for(i=0;i<=n;p[i]=0,i++) dis[i]=INF;
	for(head=tail=dis[s]=0,q[tail++]=s;head<tail;){
		j=q[head++];
		for(i=V[j].next;i!=0;i=V[i].next){
			k=V[i].v;
			if(dis[j]+V[i].w<dis[k]){
				dis[k]=dis[j]+V[i].w;
				p[j]++;
				q[tail++]=k;
			}
		}
	}
}
void tree::treeup(int u)
{
	int i,j,k,v; bool ok;
	for(i=0;i<=n;vis[i]=false,i++) x[i]=-1;
	for(tail=0,q[++tail]=u;tail>0;){
		v=q[tail]; ok=false;
		for(i=V[v].next;i!=0;i=V[i].next){
			k=V[i].v;
			if(dis[v]>=dis[k]||vis[k]) continue;
			q[++tail]=k; vis[k]=true; ok=true;
		}
		if(ok==true) continue;
		for(i=V[v].next;i!=0;i=V[i].next){
			k=V[i].v;
			if(dis[v]>=dis[k]) continue;
			if(x[v]==-1) x[v]=0;
			if(x[k]==-1) x[v]+=V[i].w;
			else x[v]+=min(V[i].w,x[k]);
		}
		tail--;
	}
}
void tree::treedown(int u)
{
	int i,j,k,v;
	head=tail=0;
	for(i=V[u].next;i!=0;i=V[i].next){
		k=V[i].v;
		if(dis[u]>=dis[k]) continue;
		if(x[k]==-1) x[k]=0;
		if(p[u]==1) x[k]+=V[i].w;
		else x[k]+=min(max(x[u]-V[i].w,x[u]-x[k]),V[i].w);
		q[tail++]=k;
	}
	while(head<tail){
		v=q[head++];
		for(i=V[v].next;i!=0;i=V[i].next){
			k=V[i].v;
			if(dis[v]>=dis[k]) continue;
			if(x[k]==-1) x[k]=0;
			//printf("%d %d ",k,x[k]);
			x[k]+=min(max(x[v]-V[i].w,x[v]-x[k]),V[i].w);
			q[tail++]=k;
			//printf("%d %d\n",k,x[k]);
		}
	}
}
void tree::ans()
{
	bfs(1);
	treeup(1);
	int i;
	//for(i=1;i<=n;i++) printf("%d ",x[i]); printf("\n");
	treedown(1);
	int res=0;
	for(i=1;i<=n;i++) res=max(res,x[i]);
	printf("%d\n",res);
}
int main()
{
	int t;
	scanf("%d",&t);
	tree s;
	while(s.init()){
		s.ans();
	}
	return 0;
}*/
