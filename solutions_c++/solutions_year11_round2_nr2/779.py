#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;
#define min 0.000001
double d;
int x;
bool ispossible(vector<double> pos, double time) {
pos[0]-=time;
double last = pos[0];
//cout<<pos[0]<<" ";
for(int i =1; i < x;i++) {
	if(pos[i] < last) {
		if(pos[i] + time < last + d)
			return false;
		pos[i] = last + d;
	} else {
		if(last + d <= pos[i]) {
			pos[i] = max(last+d, pos[i]-time);
		} else {
			if(last + d > pos[i] + time)
				return false;
			pos[i] = last + d;
		}
	}
	last = pos[i];
//	cout<<pos[i]<<" ";
}
return true;
}
int main() {
int t;
int c, cas = 1;
vector<double> pos(100);
scanf("%d", &t);
while(t--) {
	scanf("%d %lf", &c, &d);
	x = 0;
	int no, p;
	for(int i =0;i<c;i++)  {
		scanf("%d %d", &p, &no);
		for(int j =0;j<no;j++) {
			pos[x++] = p;
		}
	}
	if(cas==39) {
	cout<<"Input"<<endl;
	for(int i =0;i<x;i++) {
		cout<<pos[i];
	}
	cout<<endl;
	}
	double mintime = 0;
	double maxtime = (x*d);
	bool done = false;
	double time = (mintime + maxtime) / 2;
	while(maxtime >= mintime) {
		done = ispossible(pos, time);
//		cout<<endl<<"Pos or not in time "<<time<<": "<<done<<endl;
		if(done == false) {
			mintime = time + min;
		} else {
			maxtime = time - min;
		}
		time = (mintime + maxtime) / 2;
	}
	printf("Case #%d: ", cas++);
	cout<<time<<endl;
}
}
