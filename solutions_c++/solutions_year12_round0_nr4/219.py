#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;

const double pi = acos(-1.0); // 3.1415926535897932384626433832795
const double eps = 1e-8;
const double dinf = 1e8;
const double einf = 1e30;
inline double sqr( double x ) { return x * x ; };							
inline int dcmp( double x ) {
	if( x < -eps ) return -1; return x > eps; 
}
inline double min(double x, double y) { return dcmp(x-y)<0?x:y; };
inline double max(double x, double y) { return dcmp(x-y)>0?x:y; };

struct P {
	double x, y ;
	P(double x0=0,double y0=0):x(x0),y(y0){}
};

double det(const P&a , const P&b , const P&c) { 				
  return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x) ;
}

double dot(const P&a , const P&b , const P&c) { 				
  return (b.x-a.x)*(c.x-a.x)+(b.y-a.y)*(c.y-a.y);
}

bool isPtInLine(P a,P b,P c){
	return !dcmp(det(a,b,c));
}
bool xyCmp(P a,P b,P c){
	return(dcmp((c.x-a.x)*(b.x-a.x))<=0 && dcmp((c.y-a.y)*(b.y-a.y))<=0);
}

bool isPtOnSeg(P a,P b,P c){
	return(isPtInLine(a,b,c) && xyCmp(a,b,c));
}

int segCross(P a,P b,P c,P d,P &p){
	double s1,s2,s3,s4;int d1,d2,d3,d4;
	d1=dcmp(s1=det(a,b,c));
	d2=dcmp(s2=det(a,b,d));
	d3=dcmp(s3=det(c,d,a));
	d4=dcmp(s4=det(c,d,b));
	if(dcmp(s2-s1)==0)return 2;
	p.x=(c.x*s2-d.x*s1)/(s2-s1);
	p.y=(c.y*s2-d.y*s1)/(s2-s1);
	if(xyCmp(p,a,b) && xyCmp(p,c,d))return 1;
	//if((d1^d2)==-2 && (d3^d4)==-2)return 1;
	return 0;
}

int t,H,W,d;
char mp[40][40];
int xx,yy;

double dis( const P&p1, const P&p2 ){
	return sqrt(sqr(p1.x-p2.x)+sqr(p1.y-p2.y));
}

int tes(int x,int y){
	if(x<0 || x>=H || y<0 || y>=W)return -1;
	if(mp[x][y]=='#')return 1;
	return 0;
}


int dx,dy,nx,ny;
P ha,hb,wa,wb,np,tp,cp;
double nl;

void ref(int xy){
	if(xy==0){
		dx=-dx;
		ha.x+=dx;
		hb.x+=dx;
		tp.x-=2*(tp.x-cp.x);
	}else{
		dy=-dy;
		wa.y+=dy;
		wb.y+=dy;
		tp.y-=2*(tp.y-cp.y);
	}
	nl+=dis(np,cp);
	np=cp;
}

void mov(int xy){
	if(xy==0){
		ha.x+=dx;
		hb.x+=dx;
		wa.x+=dx;
		wb.x+=dx;
		nx+=dx;
	}else{
		ha.y+=dy;
		hb.y+=dy;
		wa.y+=dy;
		wb.y+=dy;
		ny+=dy;
	}
	nl+=dis(np,cp);
	np=cp;
}

int gcd(int a,int b){
	if(b==0)return a;
	return gcd(b,a%b);
}

int main(){
	int h,i,j,k,ans;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d%d",&H,&W,&d);
		for(i=0;i<H;i++)
			scanf("%s",mp[i]);
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				if(mp[i][j]=='X'){
					xx=i;yy=j;
				}
			}
		}
		ans=0;
		for(i=-d;i<=d;i++){
			for(j=-d;j<=d;j++){
				if(gcd(abs(i),abs(j))!=1)continue;
				if(i==0 && j==0)continue;
				if(dcmp(dis(P(i,j),P(0,0))-d)>0)continue;
				if(i<0){
					hb.x=ha.x=-0.5;ha.y=-0.5;hb.y=0.5;
					dx=-1;
				}else{
					hb.x=ha.x=0.5;ha.y=-0.5;hb.y=0.5;
					dx=1;
				}
				if(j<0){
					wb.y=wa.y=-0.5;wa.x=-0.5;wb.x=0.5;
					dy=-1;
				}else{
					wb.y=wa.y=0.5;wa.x=-0.5;wb.x=0.5;
					dy=1;
				}
				nx=xx;
				ny=yy;
				np=P(0,0);
				tp=P(i*d,j*d);
				nl=0;
				while(dcmp(d-nl)>0){
					if(segCross(np,tp,ha,hb,cp)==1){
						if(dcmp(nl)!=0 && isPtOnSeg(P(0,0),np,cp)){
							if(dcmp(d-nl-dis(P(0,0),np))>=0)ans++;
							break;
						}
						int tmp=tes(nx+dx,ny);
						if(tmp==-1)break;
						else if(tmp==1){
							if(dcmp(cp.y-ha.y)==0 || dcmp(cp.y-hb.y)==0){
								tmp=tes(nx+dx,ny+dy);
								if(tmp==-1)break;
								else if(tmp==1){
									ref(0);
								}else{
									mov(0);
								}
							}else{
								ref(0);
							}
						}else{
							mov(0);					
						}
					}else if(segCross(np,tp,wa,wb,cp)==1){
						if(dcmp(nl)!=0 && isPtOnSeg(P(0,0),np,cp)){
							if(dcmp(d-nl-dis(P(0,0),np))>=0)ans++;
							break;
						}
						int tmp=tes(nx,ny+dy);
						if(tmp==-1)break;
						else if(tmp==1){
							ref(1);
						}else{
							mov(1);
						}
					}else if(dcmp(nl)!=0 && isPtOnSeg(P(0,0),np,tp)){
						if(dcmp(d-nl-dis(P(0,0),np))>=0)ans++;
						break;
					}else{
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",h,ans);
	}
	return 0;
}
