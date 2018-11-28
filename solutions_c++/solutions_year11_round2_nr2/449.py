#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;

double step = 0.000001;

bool poss(vector<double> v, double time, int n, double d) 
{
v[0]-=time;
double last = v[0];
int i;
for(i =1; i < n;i++) {
if(v[i] >= last) {
	if(last + d <= v[i]) {
		v[i] = max(last+d, v[i]-time);
	} else {
		if(last + d > v[i] + time)
		return false;
		v[i] = last + d;
	}
} else {
	if(v[i] + time < last + d)
	return false;
	v[i] = last + d;
}
last = v[i];
}
return true;
}

int main() 
{

int t,number=1;
scanf("%d", &t);

vector<double> v(1000000);

while(t--) {
           int c,n,i,j;
           double d;
scanf("%d %lf", &c, &d);
n = 0;
int no, p;
for(i=0;i<c;i++)  {
scanf("%d %d", &p, &no);
for(j=0;j<no;j++) {
v[n++] = p;
}
}
double mintime = 0;
double maxtime = (n*d);
bool done = false;
double time = (mintime + maxtime) / 2;
double ltime = 0;
while(maxtime >= mintime) {
if(ltime == time) {
break;
}
done = poss(v, time,n,d);
if(done == false) {
mintime = time + step;
} else {
maxtime = time - step;
}
ltime = time;
time = (mintime + maxtime) / 2;
}
printf("Case #%d: %lf\n", number++, time);
}
}
