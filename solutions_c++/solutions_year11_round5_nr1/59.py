#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

#define lint long long

#define sz size()
#define pb push_back
#define mp make_pair

#define FOR(i,n) SFOR(i,0,n)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int XL[1010],YL[1010],XU[1000],YU[1000];
vector<double> X,Y;

int main() {
	int i,j,n;
	FILE* fp = fopen("A.in","r");
	FILE* fp1 = fopen("A.out","w");
	int t,tt;
	fscanf(fp,"%d",&tt);
	int W,L,U,G;
	FOR(t,tt) {
		fprintf(fp1,"Case #%d:\n",t+1);
//		printf("Case #%d:\n",t+1);
		fscanf(fp,"%d%d%d%d",&W,&L,&U,&G);
		FOR(i,L) fscanf(fp,"%d%d",&XL[i],&YL[i]);
		FOR(i,U) fscanf(fp,"%d%d",&XU[i],&YU[i]);
		i = j = 0;
		X.clear();
		Y.clear();
		while ((i < U) && (j < L)) {
			if (XU[i] == XL[j]) {
				X.pb(XU[i]);
				Y.pb(YU[i]-YL[j]);
				i++; j++; continue;
			}
			if (XU[i] < XL[j]) {
				X.pb(XU[i]);
				Y.pb(YU[i]-(YL[j-1] + (XU[i]-XL[j-1])*(YL[j]-YL[j-1])*1.0/(XL[j]-XL[j-1])));
				i++; continue;
			}
			if (XU[i] > XL[j]) {
				X.pb(XL[j]);
				Y.pb(-YL[j]+(YU[i-1] + (XL[j]-XU[i-1])*(YU[i]-YU[i-1])*1.0/(XU[i]-XU[i-1])));
				j++; continue;
			}
		}
		if (t == 3) {
			printf("%d\n",G);
			FOR(i,X.sz) printf("%.7lf %.7lf\n",X[i],Y[i]);
		}
		double S, S1;
		S = S1 = 0;
		double l,r,m;
		FOR(i,X.sz-1) S += (X[i+1]-X[i])*(Y[i+1]+Y[i])/2;
		int k1 = 0;
		FOR(i,X.sz-1) {
			if (S1 + (X[i+1]-X[i])*(Y[i+1]+Y[i])/2 > S/G) {
				r = X[i+1];
				l = X[i];
				while (r-l > 0.000000001) {
					m = (l+r)/2;
					if (S1 + (m-X[i])*((Y[i+1]-Y[i])*(m-X[i])/(X[i+1]-X[i])+2*Y[i])/2 > S/G) r = m; else l = m;
				}
//				printf("%.7lf\n",l);
				if (k1 < G-1)	fprintf(fp1,"%.7lf\n",l); k1++;
				S1 = 0;
				Y[i] += (Y[i+1]-Y[i])*(l-X[i])/(X[i+1]-X[i]);
				X[i] = l;
				i--; continue;
			}
			S1 += (X[i+1]-X[i])*(Y[i+1]+Y[i])/2;
		}
	}
	fclose(fp);
	fclose(fp1);
    return 0;
}