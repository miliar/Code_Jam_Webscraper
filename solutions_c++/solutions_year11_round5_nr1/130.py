#include <stdio.h>
#include <algorithm>

using namespace std;

#define x first
#define y second

pair<int,int> datl[100];
pair<int,int> datu[100];

int w,l,u,g;

double getarea(double left, double right) {
	double totalarea = 0;
	for(int i = 0;i + 1 < l;i ++){
		if(datl[i+1].x < left) continue;
		if(datl[i].x > right) continue;
		pair<double, double> leftp, rightp;
		if(datl[i].x <= left) {
			leftp.x = left;
			leftp.y = (datl[i].y * (datl[i+1].x-left)+ datl[i+1].y * (left-datl[i].x))
				/ (double)(datl[i+1].x-datl[i].x);
		}else {
			leftp = datl[i];
		}
		if(datl[i+1].x >= right) {
			rightp.x = right;
			rightp.y = (datl[i].y * (datl[i+1].x-right)+ datl[i+1].y * (right-datl[i].x))
				/ (double)(datl[i+1].x-datl[i].x);
		}else {
			rightp = datl[i+1];
		}

		totalarea -= (rightp.x-leftp.x) * (rightp.y + leftp.y) / 2.0;
	}
	for(int i = 0;i + 1 < u;i ++){
		if(datu[i+1].x < left) continue;
		if(datu[i].x > right) continue;
		pair<double, double> leftp, rightp;
		if(datu[i].x <= left) {
			leftp.x = left;
			leftp.y = (datu[i].y * (datu[i+1].x-left)+ datu[i+1].y * (left-datu[i].x))
				/ (double)(datu[i+1].x-datu[i].x);
		}else {
			leftp = datu[i];
		}
		if(datu[i+1].x >= right) {
			rightp.x = right;
			rightp.y = (datu[i].y * (datu[i+1].x-right)+ datu[i+1].y * (right-datu[i].x))
				/ (double)(datu[i+1].x-datu[i].x);
		}else {
			rightp = datu[i+1];
		}

		totalarea += (rightp.x-leftp.x) * (rightp.y + leftp.y) / 2.0;
	}
	return totalarea;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int testcase = 1; testcase <= T; testcase ++){
		scanf("%d%d%d%d",&w,&l,&u,&g);
		for(int i = 0;i < l; i++){
			scanf("%d%d",&datl[i].x,&datl[i].y);
		}
		for(int i = 0;i < u; i++){
			scanf("%d%d",&datu[i].x,&datu[i].y);
		}
		double totalarea = 0;
		for(int i = 0;i + 1 < l;i ++){
			totalarea -= (datl[i+1].x-datl[i].x) * (datl[i+1].y + datl[i].y) / 2.0;
		}
		for(int i = 0;i + 1 < u;i ++){
			totalarea += (datu[i+1].x-datu[i].x) * (datu[i+1].y + datu[i].y) / 2.0;
		}

		printf("Case #%d:\n",testcase);
		double lastpoint = 0;
		for(int i = 0;i < g-1;i ++) {
			double low = lastpoint, high = w;
			for(int magic = 0 ;magic < 100; magic ++) {
				double mid = (low+high)/2;
				if(getarea(lastpoint,mid)*g < totalarea) {
					low = mid;
				}else {
					high = mid;
				}
			}
			lastpoint = (low+high)/2;
			printf("%.9f\n",lastpoint);
		}
	}
	return 0;
}
