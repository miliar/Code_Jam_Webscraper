#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

class ww {
public:
	int b,e,w;
};
bool operator < (const ww& a, const ww&b) {
	return a.w < b.w;
}
void tc(int tcn) {
int x,n;
double s,r,t;
cin>>x>>s>>r>>t>>n;
vector<ww> v(n);
for (int i=0;i<n;i++) {
cin>>v[i].b >> v[i].e >> v[i].w;
}
sort(v.begin(),v.end());
int freeWay = x;
for (int i=0;i<n;i++) {
	freeWay -= (v[i].e - v[i].b);
}
double time = 0.0;
double runTime = min(t, freeWay / r);
time += runTime;
time += (freeWay - r*runTime)/s;
t -= runTime;
for (int i=0;i<n;i++) {
	runTime = min(t, (v[i].e - v[i].b)/(r+v[i].w));
	time += runTime;
	time += (((v[i].e - v[i].b) - (r+v[i].w)*runTime))/(s+v[i].w);
	t-=runTime;
}
cout << "Case #" << tcn << ": " << time << endl;
}
int main() {
	cout << setprecision(10);
	int t;
	cin>>t;
	for (int i=0;i<t;i++)tc(i+1);
}