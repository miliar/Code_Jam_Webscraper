#include <stdio.h>
#include <assert.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef std::vector<int> Vec;
typedef Vec::iterator It;
typedef std::vector<Vec> VVec;
typedef VVec::iterator ItV;
typedef pair<int,int> Pair;

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define FORS(i,m,n) for((i)=m;(i)<(int)(n);(i)++)
#define tr(container,it) for(typeof(container.begin())it=container.begin();it!=container.end();it++)
#define bit(n) (1<<(n))
#define bit64(n) ((ll(1))<<(n))
#define inf 1000000000
#define eps 1e-9
#define PI 3.1415926535897932385
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) a.begin(),a.end()
#define fill(container,val) memset(container,val,sizeof container)
#define square(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>=(b)?(a):(b))

clock_t start=clock();

double rpi(double wp, double owp, double oowp) {
    return 0.25*wp+0.50*owp+0.25*oowp;    
}

int main(void) {
	freopen("rpi.in","r",stdin);
	freopen("rpi.out","w",stdout);
    int i,j,k,n,N,T,test=0;
	for(scanf("%d",&T);T--;) {
	    scanf("%d",&N);
        printf("Case #%d:\n",++test);
        int R[N][N]; fill(R,0);
        double RPI[N]; fill(RPI,0.0);
        double WP[N]; fill(WP,0.0);
        double OWP[N]; fill(OWP,0.0);
        double OOWP[N]; fill(OOWP,0.0);
        FOR(i,N) {
            char str[N];
            scanf("%s",str);
            FOR(j,N) {
                if(str[j]=='1')R[i][j]=1;
                else if(str[j]=='0')R[i][j]=0;
                else R[i][j]=-1;
	            //fprintf(stderr,"%d",R[i][j]);
            }
	        //fprintf(stderr,"\n");
        }
        
        VVec Opp;
        FOR(i,N) {
            double wp=0.0,owp=0.0,nm=0.0;
            Vec opp;
            FOR(j,N) {
                if(R[i][j]<0) continue;
                wp+=(double)R[i][j];
                nm+=1.0;
                opp.pb(j);
            }
            Opp.pb(opp);
            WP[i]=wp/nm;
            It it;
            tr(opp,it) {
                double wo=0, no=0;
                FOR(k,N) {
                    if(R[*it][k]<0)continue;
                    if(k==i)continue;
                    no+=1.0;
                    wo+=(double)R[*it][k];
                }
                if(no>0) owp+=wo/no;
            }
            //OWP[i]=(nm/(double)N)*owp;
            OWP[i]=owp/nm;
            //fprintf(stderr,"%d %f %f\n",i,WP[i],OWP[i]);
        }
        FOR(i,N) {
            double oowp=0.0;
            It it;
            tr(Opp[i],it) oowp+=OWP[*it];
            //OOWP[i]=oowp*((double)Opp[i].sz/(double(N)));
            OOWP[i]=oowp/(double)Opp[i].sz;
        }
        FOR(i,N) RPI[i]=rpi(WP[i],OWP[i],OOWP[i]);
        FOR(i,N) printf("%.7f\n",RPI[i]);
        //FOR(i,N) fprintf(stderr,"%f\n",RPI[i]);
    }
	fprintf(stderr,"time=%.3lfsec\n",0.000001*(clock()-start));
	return 0;
}
