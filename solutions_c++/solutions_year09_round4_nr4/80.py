#include<cstdio>
#include<cmath>
const int N=50;
const int M=N*N*N;
int T,n,m;
double x[N],y[N],r[N],inf,sup,px[M],py[M];
long long c[M],stdd;
double Abs(double x){
	return x>0?x:-x;
}
bool can(double R){
	m=n;
	for (int i=0;i<n;i++){
		px[i]=x[i];py[i]=y[i];
	}
	for (int i=0;i<n;i++)
		for (int j=i+1;j<n;j++){
			double dist=sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])),ri=R-r[i],rj=R-r[j];
			if (dist<ri+rj+1e-6 && dist>Abs(ri-rj)-1e-6 && (Abs(x[i]-x[j])>1e-6 || Abs(y[i]-y[j])>1e-6)){

			double k,a,b,d,aa,bb,cc,c,drt,ax,ay,bx,by;
			k=ri;
			a=x[j]-x[i];
			b=y[j]-y[i];
			c=rj;
			d=c*c-k*k-a*a-b*b;
			aa = 4 * a*a + 4 * b*b;
			bb = 4 * b * d;
			cc = d*d - 4* a*a * k*k;
			drt = bb*bb - 4 * aa * cc;
			drt = sqrt (drt);
			ay = (-bb + drt) / 2 / aa;
			by = (-bb - drt) / 2 / aa;
			if (Abs (a) < 1e-6)
			{
				ax = sqrt (k*k -ay*ay);
				bx = -ax;
			}
			else
			{
				ax = (2 * b * ay + d) / -2 / a;
				bx = (2 * b * by + d) / -2 / a;
			}
			ax += x[i];
			ay += y[i];
			bx += x[i];
			by += y[i];
			px[m]=ax;
			py[m]=ay;
			m++;
			px[m]=bx;
			py[m]=by;
			m++;

			}
		}
	for (int i=0;i<m;i++){
		c[i]=0;
		for (int j=0;j<n;j++)
			if ((px[i]-x[j])*(px[i]-x[j])+(py[i]-y[j])*(py[i]-y[j])<(R-r[j])*(R-r[j])+1e-6)
				c[i]|=1LL<<j;
	}
	stdd=0;
	for (int i=0;i<n;i++)
		stdd|=1LL<<i;
	for (int i=0;i<m;i++)
		for (int j=i;j<m;j++)
			if ((c[i]|c[j])==stdd)
				return 1;
	return 0;
}
int main(){
//	freopen("D.in","r",stdin);
//	freopen("D.out","w",stdout);
//	freopen("D-small-attempt0.in","r",stdin);
//	freopen("D-small-attempt0.out","w",stdout);
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++){
		scanf("%d",&n);
		inf=0;sup=1e10;
		for (int i=0;i<n;i++){
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
			if (r[i]>inf)
				inf=r[i];
		}
		while (sup-inf>1e-7){
			double mid=(sup+inf)/2;
			if (can(mid))
				sup=mid;
			else
				inf=mid;
		}
		printf("Case #%d: %0.7lf\n",t,(sup+inf)/2);
	}
	return 0;
}
