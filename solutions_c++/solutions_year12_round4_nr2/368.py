#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<complex>
using namespace std;
#define x real()
#define y imag()
typedef complex<double> Point;
const double eps = 1e-4;
const int ROUND = 20, RESIZE = 10;

struct Circle{
	Point c;
	double r;
	Point wlk;
	int sta;
}ans[1010];
int cas,n,w,l;
int adj[1010][1010], ads[1010];
double size;
inline double squ(double xx){
	return xx*xx;
}
inline bool rough_correct(){
	for(int i=0;i<n;i++)
		for(int j=0;j<ads[i];j++){
			double dif = norm(ans[i].c-ans[adj[i][j]].c) - squ(ans[i].r+ans[adj[i][j]].r);
			if(dif < eps) {
				//fprintf(stderr, "%d %d %lf (%lf, %lf), (%lf, %lf)\n", i, adj[i][j] , dif, ans[i].c.x, ans[i].c.y, ans[adj[i][j]].c.x, ans[adj[i][j]].c.y);
				return false;
			}
		}
	return true;
}
inline bool correct(){
	if(!rough_correct()) return false; 
	
	memset(ads, 0, sizeof(ads));
	bool ret = true;
	for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++){
			double dif = abs(ans[i].c-ans[j].c) - ans[i].r - ans[j].r;
			
			if(dif < eps) {
				//fprintf(stderr, "%d %d %lf\n", i, j , dif);
				ret = false;
			}
			
			if(dif < size*ROUND){
				adj[i][ads[i]++]=j;
				adj[j][ads[j]++]=i;
			}
		}
	return ret;
}
inline double getRand(){
	return (rand()&32767) / 32768.0;
}
inline void calc_wlk(){
	for(int i=0;i<n;i++)ans[i].wlk = Point(0.0, 0.0), ans[i].sta = 0;
	
	for(int i=0;i<n;i++){
				
		for(int j=0;j<ads[i];j++){
			double dif = norm(ans[i].c-ans[adj[i][j]].c) - squ(ans[i].r+ans[adj[i][j]].r);
			if(dif < eps){
				Point vec =  ans[i].c-ans[adj[i][j]].c + Point(getRand()*size, getRand()*size);
				double ori = abs(vec);
				double dis =  ans[i].r+ans[adj[i][j]].r - ori;
				ans[i].sta ++;
				ans[i].wlk += vec * dis / ori;
				//if(i==25)fprintf(stderr, "%lf %lf %lf %lf\n",dif, ori, ans[i].wlk.x, ans[i].wlk.y);
			}
		}
		
		if(ans[i].sta){
			//ans[i].wlk /= sqrt(ans[i].sta);
		}
	}	
}
inline void clip(double& xx, double a, double b){
	if(xx<a)xx=a;
	if(xx>b)xx=b;
}
inline void walk(){
	for(int i=0;i<n;i++){
		ans[i].c+=ans[i].wlk*size;
		clip(ans[i].c.x, 0, w);
		clip(ans[i].c.y, 0, l);
	}
}
int main(){
	scanf("%d",&cas);
	srand(514);
	for(int iii=0;iii<cas;iii++){
		fprintf(stderr, "Case %d\n", iii+1);
		scanf("%d%d%d",&n,&w,&l);
		for(int i=0;i<n;i++)scanf("%lf",&ans[i].r);
		
		int rounds=0, succeed=0;
		while(1){
			fprintf(stderr, "RND %d\n", ++rounds);
			for(int i=0;i<n;i++)ans[i].c=Point(getRand()*w, getRand()*l);
			
			memset(ads, 0, sizeof(ads));
			for(int i=0;i<n;i++)for(int j=0;j<n;j++){
				if(i==j)continue;
				adj[i][ads[i]++]=j;
			}
			size=1.0;
			
			for(int rsz=0;rsz<RESIZE;rsz++){
				fprintf(stderr, "RSZ %d\n", rsz);
				for(int ron=0;ron<ROUND;ron++){
					calc_wlk();
					walk();								
					if(correct()){
						 fprintf(stderr, "%d %d\n", rsz, ron);
						 goto CORRECT;
					}
				}	
				size/=1.2;				
			}
		}
	CORRECT:;
		printf("Case #%d:", iii+1);
		for(int i=0;i<n;i++)printf(" %.9lf %.9lf", ans[i].c.x, ans[i].c.y);
		puts("");
	}
	return 0;
}
		

