#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
typedef __int64 ll;
const int N=110000;
int n,k,t,tests;
double WP[200],OWP[200],OOWP[200],RPI[200],wpBez[200][200];
string s[200];
int main () {
#ifndef ONLINE_JUDGE
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#endif
	cin>>tests;
	for (t=1; t<=tests; t++) {
		cout<<"Case #"<<t<<":"<<endl;
		cin>>n;
		for (int i=0; i<n; i++) {
			cin>>s[i];
			int all=0,win=0;
			for (int j=0; j<n; j++)
				if (s[i][j]!='.') {
					all++;
					if (s[i][j]=='1') win++;
				}
			WP[i]=((double)win)/all;
			for (int j=0; j<n; j++)
				if (s[i][j]!='.') {
					if (s[i][j]=='1') {
						wpBez[i][j]=(double(win-1))/(all-1);
					} else {
						wpBez[i][j]=(double(win))/(all-1);
					}
				}
		}
		for (int i=0; i<n; i++) {
			double sum=0,cnt=0;
			for (int j=0; j<n; j++) 
				if (s[i][j]!='.') sum+=wpBez[j][i], cnt++;
			OWP[i]=sum/cnt;
		}
		for (int i=0; i<n; i++) {
			double sum=0;
			int cnt=0;
			for (int j=0; j<n; j++) 
				if (s[i][j]!='.') sum+=OWP[j], cnt++;
			OOWP[i]=sum/cnt;
			RPI[i]= 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			printf("%.19lf\n",RPI[i]);
		}
	}
}