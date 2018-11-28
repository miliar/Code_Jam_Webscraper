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
typedef pair<int,int> Pair;
typedef std::vector<Pair> VecP;
typedef VecP::iterator ItP;

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

int main(void) {
	freopen("squaretiles.in","r",stdin);
	freopen("squaretiles.out","w",stdout);
    int i,j,k,n,R,C,T,test=0;
	for(scanf("%d",&T);T--;) {
        printf("Case #%d:\n",++test);
        scanf("%d %d",&R,&C);
        //fprintf(stderr,"%d %d\n",R,C);
        int Pic[R][C];
        fill(Pic,0);
        int BlueNr;
        bool ans=true;
        FOR(i,R) {
            char s[C];
            scanf("%s",s);
            BlueNr=0;
            FOR(j,C) if(s[j]=='#') { Pic[i][j]=1; BlueNr+=1; }
            //FOR(j,C) fprintf(stderr,"%d",Pic[i][j]);
            //fprintf(stderr,"\n");
            if(BlueNr%2) { ans=false; } 
        }
        if(!ans){
            printf("Impossible\n");
            //fprintf(stderr,"Impossible\n");
            continue;
        }

        FOR(j,C) {
            BlueNr=0;
            FOR(i,R) BlueNr+=Pic[i][j];
            if(BlueNr%2) { ans=false; break; }
        }
        if(!ans){
            printf("Impossible\n");
            //fprintf(stderr,"Impossible\n");
            continue;
        }

        int NewPic[R][C];
        fill(NewPic,46);
        FOR(i,R) {
            j=0;
            while(j<C) {
                if(Pic[i][j]==1) {
                    NewPic[i][j]=47;
                    NewPic[i][j+1]=92;
                    NewPic[i+1][j]=92;
                    NewPic[i+1][j+1]=47;
                    Pic[i][j]=0;
                    Pic[i][j+1]=0;
                    Pic[i+1][j]=0;
                    Pic[i+1][j+1]=0;
                    j+=2;
                } else j++;
            }
        }
        FOR(i,R) {
                FOR(j,C) printf("%c",NewPic[i][j]);
                printf("\n");
                //fprintf(stderr,"%s\n",s);
        }               
    }
	fprintf(stderr,"time=%.3lfsec\n",0.000001*(clock()-start));
	return 0;
}
