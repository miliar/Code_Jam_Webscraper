#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;

int tc;
int rig,a,b,n;
int x1[105],x2[105],y3[105],y4[105];
set<int> s;
int sc[500];
double sh[500];

double solve (double t1,double t2,double t3) {
	if (abs(t1)<1e-9) {
		if (abs(t2)<1e-9) return 0;
		return -t3/t2;
	}
	return (-t2+sqrt(t2*t2-4*t1*t3))/2.0/t1;
}

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		s.clear();
		scanf("%d%d%d%d",&rig,&a,&b,&n);
		for (int i=0; i<a; i++) {
			scanf("%d%d",&x1[i],&y3[i]);
			s.insert(x1[i]);
		}
		for (int i=0; i<b; i++) {
			scanf("%d%d",&x2[i],&y4[i]);
			s.insert(x2[i]);
		}
		set<int>::iterator it;
		int i1=0,i2=0;
		double prev=0,ya,yb;
		int cnt=0;
		cnt=1;
		sc[0]=0;
		sh[0]=0;
		for (it=s.begin(); it!=s.end(); it++) {
			while (i1<a && (*it)>x1[i1]) i1++;
			if ((*it)==x1[i1]) ya=y3[i1];
			else {
				ya=(y3[i1]-y3[i1-1])*1.0/(x1[i1]-x1[i1-1])*((*it)-x1[i1-1])+y3[i1-1];
			}
			while (i2<b && (*it)>x2[i2]) i2++;
			if ((*it)==x2[i2]) yb=y4[i2];
			else {
				yb=(y4[i2]-y4[i2-1])*1.0/(x2[i2]-x2[i2-1])*((*it)-x2[i2-1])+y4[i2-1];
			}
			//printf("%d: %d %d %f %f\n",(*it),i1,i2,ya,yb);
			sc[cnt]=(*it);
			sh[cnt]=yb-ya;
			cnt++;
		}
		double area=0;
		for (int i=1; i<cnt; i++) {
			area+=(sh[i]+sh[i-1])*(sc[i]-sc[i-1])/2.0;
		//	printf("%d: %f %f %d %d %f\n",i,sh[i],sh[i-1],sc[i],sc[i-1],area);
		}
		area/=n;
		printf("Case #%d:\n",T);
		//printf("area %f\n",area);
		double cura=0,rat,ans;
		prev=0;
		int ind=0;
		for (int i=0; i<n-1; i++) {
			while (cura<area) {
				ind++;
				prev=sc[ind-1];
				cura+=(sh[ind]+sh[ind-1])*(sc[ind]-sc[ind-1])/2.0;
			}
			//printf("%d %f\n",ind,cura);
			double mi=prev,mx=sc[ind],mid,h;
			//printf("%f %f\n",mi,mx);
			while (mi+1e-9<mx) {
				mid=(mi+mx)/2;
				//printf("%f\n",mid);
				h=(mid-sc[ind-1])/(sc[ind]-sc[ind-1])*(sh[ind]-sh[ind-1])+sh[ind-1];
				if (cura-(sh[ind]+h)*(sc[ind]-mid)/2>area) mx=mid;
				else mi=mid;
			}
			printf("%.8f\n",mi);
			prev=mi+1e-6;
			cura-=area;
		}
					
	}
}
