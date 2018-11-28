#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<algorithm>
#include<list>
using namespace std;
inline double len(double x1,double y1,double x2,double y2){
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}
int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout);
	int ttt;
	cin>>ttt;
	int ttti;
	for(ttti=1;ttti<=ttt;++ttti){
		int n;
		cin>>n;
		vector<double> xx(n),yy(n),rr(n);
		int i;
		for(i=0;i<n;i++)
			cin>>xx[i]>>yy[i]>>rr[i];

		int nn=n;
		while(nn>2){
			//vector<vector<double> >d(nn,vector<double>(nn));
			int i1;
			int mi1=-1,mi2=-1;
			double mi=100000000.0;
			double d;
			for(i=0;i<nn;i++){
				for(i1=i+1;i1<nn;i1++){
					d=rr[i]+rr[i1]+len(xx[i],yy[i],xx[i1],yy[i1]);
					if(d<mi){
						mi=d;
						mi1=i;
						mi2=i1;
					}
				}
			}

			double a0=(xx[mi2]-xx[mi1])/len(xx[mi1],yy[mi1],xx[mi2],yy[mi2]);
			double b0=(yy[mi2]-yy[mi1])/len(xx[mi1],yy[mi1],xx[mi2],yy[mi2]);
			double a=a0*(mi*0.5-rr[mi1]);
			double b=b0*(mi*0.5-rr[mi1]);
			xx[mi1]+=a;
			yy[mi1]+=b;
			rr[mi1]=mi*0.5;

			vector<double> nxx(nn-1),nyy(nn-1),nrr(nn-1);
			for(i=0;i<mi2;i++){
				nxx[i]=xx[i];
				nyy[i]=yy[i];
				nrr[i]=rr[i];
			}
			for(i=mi2+1;i<nn;i++){
				nxx[i-1]=xx[i];
				nyy[i-1]=yy[i];
				nrr[i-1]=rr[i];
			}
			nn--;
			xx=nxx;
			yy=nyy;
			rr=nrr;

		}

		double r;
		if(n==1)
			r=rr[0];
		else
			r=max(rr[0],rr[1]);
		cout<<"Case #"<<ttti<<": ";
		printf("%0.6f\n",r);
	}
	return 0;
}