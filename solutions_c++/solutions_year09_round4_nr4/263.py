#include<iostream>
#include<cmath>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const double zero=1e-8;
const int maxn=42;
const int maxm=100051;
const double limit=1000000;
double x[maxn],y[maxn],r[maxn],a[maxm],b[maxm],c[maxm],scale,d,ans,t0,t1,t2;
int i,j,k,ti,ca,n,tot;
double dis(double x0,double y0,double x1,double y1){
	return sqrt((x0-x1)*(x0-x1)+(y0-y1)*(y0-y1));
}
bool ok(int c0,int c1){
	int i;
	fr(i,1,n)
		if(!(dis(x[i],y[i],a[c0],b[c0])+r[i]<c[c0]+zero)&&!(dis(x[i],y[i],a[c1],b[c1])+r[i]<c[c1]+zero))
			return false;
	return true;
}
bool get(int p0,int p1,int p2,double radius,double &a,double &b,double &c){
	double d=dis(x[p0],y[p0],x[p1],y[p1]),d1=radius-r[p0],d2=radius-r[p1],cosa,sina,xx=x[p1]-x[p0],yy=y[p1]-y[p0];
	if(d1<0||d2<0||d>d1+d2||d1>d+d2||d2>d+d1)
		return false;
	cosa=(d*d+d1*d1-d2*d2)/(2*d*d1);
	sina=sqrt(1-cosa*cosa);
	a=(cosa*xx-sina*yy)/d*d1+x[p0];
	b=(sina*xx+cosa*yy)/d*d1+y[p0];
	c=radius;
	if(dis(x[p2],y[p2],a,b)+r[p2]<c+zero)
		return true;
	sina=-sina;
	a=(cosa*xx-sina*yy)/d*d1+x[p0];
	b=(sina*xx+cosa*yy)/d*d1+y[p0];
	c=radius;
	if(dis(x[p2],y[p2],a,b)+r[p2]<c+zero)
		return true;
	return false;
}
void find(int p0,int p1,int p2,double left,double right){
	if(right-left<zero){
		if(right>limit-1)
			return;
		++tot;
		get(p0,p1,p2,right,a[tot],b[tot],c[tot]);
/*		cout<<dis(a[tot],b[tot],x[p0],y[p0])+r[p0]<<" "<<c[tot]<<endl;
		cout<<dis(a[tot],b[tot],x[p1],y[p1])+r[p1]<<" "<<c[tot]<<endl;
		cout<<dis(a[tot],b[tot],x[p2],y[p2])+r[p2]<<" "<<c[tot]<<endl;*/
	}
	else{
		double m=(left+right)/2;
		if(get(p0,p1,p2,m,t0,t1,t2))
			find(p0,p1,p2,left,m);
		else
			find(p0,p1,p2,m,right);
	}
}
int main(){
	freopen("d2.in","r",stdin);
	freopen("d2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n;
		ans=1<<30;
		tot=0;
		fr(i,1,n){
			cin>>x[i]>>y[i]>>r[i];
			a[++tot]=x[i];
			b[tot]=y[i];
			c[tot]=r[i];
		}
		fr(i,1,n)
			fr(j,i+1,n){
				c[++tot]=((d=dis(x[i],y[i],x[j],y[j]))+r[i]+r[j])/2;
				scale=(c[tot]-r[i])/d;
				a[tot]=(x[j]-x[i])*scale+x[i];
				b[tot]=(y[j]-y[i])*scale+y[i];
			}
//		cout<<tot<<endl;
		fr(i,1,n)
			fr(j,i+1,n)
				fr(k,j+1,n)
					find(i,j,k,0,limit);
//		cout<<tot<<endl;
		fr(i,1,tot)
			fr(j,i+1,tot)
				if(c[i]>c[j]){
					swap(a[i],a[j]);
					swap(b[i],b[j]);
					swap(c[i],c[j]);
				}
//		fr(i,1,tot)
//			cout<<i<<" "<<a[i]<<" "<<b[i]<<" "<<c[i]<<endl;
//		cout<<ok(18,19)<<endl;

		ans=-1;
//		cout<<ok(3,4)<<endl;
		fr(i,1,tot){
			fr(j,1,i)
				if(ok(i,j)){
					ans=c[i];
//						cout<<a[i]<<" "<<b[i]<<" "<<c[i]<<endl;
//						cout<<a[j]<<" "<<b[j]<<" "<<c[j]<<endl;
					break;
				}
			if(ans>0)
				break;
		}
		printf("Case #%d: %.7lf\n",ti,ans);
	}
}
