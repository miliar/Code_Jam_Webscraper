#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int n, m;

struct tpo
{
	double x,y;
};

tpo co[10];
tpo po[maxn];

double ans[maxn];
double zero = 1e-8;

double dis(tpo a, tpo b){

	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

double get_a(double r1, double r2){
	double res = 0;
	double dd = dis(co[1],co[2]);
	//cout<<dd<<endl;

	if(dd+zero>r1+r2){
		res = 0;
	}
	else
	if(r2>=r1+dd){
		res = r1*r1*M_PI;
	}
	else
	if(r1>=r2+dd){
		res = r2*r2*M_PI;
	}
	else{
		double ang;
		if(r1*r1+dd*dd-r2*r2 >= 0){
			ang = acos((r1*r1+dd*dd-r2*r2)/(2*r1*dd))*2;
			res+=r1*r1*ang*0.5-0.5*r1*r1*sin(ang);
		}
		else{
			ang = acos((r1*r1+dd*dd-r2*r2)/(2*r1*dd))*2;
			res+=r1*r1*ang*0.5+0.5*r1*r1*sin(2*M_PI-ang);
		}
		//cout<<"a "<<res<<endl;

		if(r2*r2+dd*dd-r1*r1 >= 0){
			ang = acos((r2*r2+dd*dd-r1*r1)/(2*r2*dd))*2;
			res+=r2*r2*ang*0.5-0.5*r2*r2*sin(ang);
		}
		else{
			ang = acos((r2*r2+dd*dd-r1*r1)/(2*r2*dd))*2;
			res+=r2*r2*ang*0.5+0.5*r2*r2*sin(2*M_PI-ang);
		}
		//cout<<"b "<<res<<endl;
	}

	return res;
}

void init_deal(){
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		init_deal();
		
		
		printf("Case #%d:",ttt);

		scanf("%d%d", &n, &m);

		for(int i = 1;i<=n;i++){
			scanf("%lf%lf", &co[i].x, &co[i].y);
		}

		for(int i = 1;i<=m;i++){
			scanf("%lf%lf", &po[i].x, &po[i].y);
			double r1,r2;
			r1 = dis(co[1],po[i]);
			r2 = dis(co[2],po[i]);

			ans[i] = get_a(r1,r2);


		}

		for(int i = 1;i<=m;i++){
			printf(" %.6lf", ans[i]);
		}

		printf("\n");
	}
	

	return 0;
};

