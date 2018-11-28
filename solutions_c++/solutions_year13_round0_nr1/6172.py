#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <fstream>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

//#define SMALL
#define LARGE

int dx,doo,dd,dt,t;


int main() {
int w=0;
#ifdef SMALL
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("A-small2.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
vs ga;
string g;
cin>>t;
int countoc=0,countor=0,countxr=0,countxc=0,countdc=0,countdr=0,counttc=0,counttr=0;
rep(i,t){
	int nodt=0;
	printf("Case #%d: ",(i+1));
	char ga[4][4];
	char g;
	rep(i,4){
	   rep(j,4){
	     cin>>ga[i][j];
	     if(ga[i][j]=='.')
			 nodt+=1;
	   }
	}
     //diagonal check
     dd=doo=dx=dt=0;
     rep(j,4){
			if(ga[j][j]=='X') dx+=1;
			if(ga[j][j]=='O') doo+=1;
			if(ga[j][j]=='T') dt+=1;
			if(ga[j][j]=='.') dd+=1;
		}
		//cout<<dx<<" "<<doo<<" "<<dt<<" "<<dd<<endl;
		if(dx>=3&&dt<=1&&doo==0&&dd==0) {printf("X won\n"); continue;}
		if(doo>=3&&dt<=1&&dx==0&&dd==0) {printf("O won\n"); continue;}
   dd=doo=dx=dt=0;
   for(int j=3;j>=0;j--){
			if(ga[3-j][j]=='X') dx+=1;
			if(ga[3-j][j]=='O') doo+=1;
			if(ga[3-j][j]=='T') dt+=1;
			if(ga[3-j][j]=='.') dd+=1;
		}
		//cout<<dx<<" "<<doo<<" "<<dt<<" "<<dd<<endl;
		if(dx>=3&&dt<=1&&doo==0&&dd==0) {printf("X won\n"); continue;}
		if(doo>=3&&dt<=1&&dx==0&&dd==0) {printf("O won\n"); continue;}


   //rows and column checking
   int nod=0;
   rep(j,4)
   {
     w=0;
    countoc=0,countor=0,countxr=0,countxc=0,countdc=0,countdr=0,counttc=0,counttr=0;                                                                                                                 	 //row check starts
     rep(k,4){
              if(ga[j][k]=='X'){
		        	countxr+=1;

			    }
               if(ga[j][k]=='O'){
                   countor+=1;
                }
               if(ga[j][k]=='T')
				  counttr+=1;
			    if(ga[j][k]=='.')
			       countdr+=1;
			 //column check
	        	if(ga[k][j]=='X'){
		        	countxc+=1;
                }
               if(ga[k][j]=='O'){
                  countoc+=1;
                }
               if(ga[k][j]=='T')
	        		counttc+=1;
	        	if(ga[k][j]=='.')
		     	 countdc+=1;
           }
      //cout<<countxc<<" "<<countxr<<" "<<countoc<<" "<<countor<<" "<<countdc<<" "<<countdr<<" "<<counttr<<" "<<counttc<<endl;
      if((countxc>=3&&counttc<=1&&countdc==0&&countoc==0)||(countxr>=3&&counttr<=1&&countdr==0&&countor==0))
		 {
		 	w=1;
		 	printf("X won\n");
		 	break;
		}
	   if((countoc>=3&&counttc<=1&&countdc==0&&countxc==0)||(countor>=3&&counttr<=1&&countdr==0&&countxr==0))
		 {
		 	w=2;
		 	printf("O won\n");
		 	break;
		 }
	}
    if(nodt>0&&w==0) { nod=1;printf("Game has not completed\n"); continue;}
    if(w==0&&nod==0){
			printf("Draw\n");
			continue;
		 }
}
}

