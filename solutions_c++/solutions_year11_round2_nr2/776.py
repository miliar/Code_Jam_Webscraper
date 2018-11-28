#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
typedef __int64 ll;
const int N=110000;
int n,k,t,all,tests,p[300],cnt[300],ans,coor[300],D,C;
double ans2;
int ok () {
	for (int i=1; i<all; i++)
		if (coor[i]-coor[i-1]<D) return 0;
	return 1;
}	
void doProc () {
	coor[0]--;
	for (int i=1; i<all; i++)
		if (coor[i]-coor[i-1]>D) coor[i]--;
		else if (coor[i]-coor[i-1]<D) coor[i]++;
}
int main () {
#ifndef ONLINE_JUDGE
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#endif
	cin>>tests;
	for (t=1; t<=tests; t++) {
		ans=0;
		ans2=0;
		D=0;
		C=0;
		all=0;
		cin>>C>>D;
		D*=2;
		for (int i=0; i<C; i++) {
			cin>>p[i]>>cnt[i];
			p[i]*=2;
			for (int j=0; j<cnt[i]; j++)  coor[all++]=p[i];
		}
		while (!ok()) {
			doProc();
			ans++;
		}
		cout<<"Case #"<<t<<": ";
		ans2=double(ans)/2;
		printf("%.19lf",ans2);
		cout<<endl;
	}
}