#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char map[100][101];
int win[100];
int all[100];
double wp[100];
double owp[100];
double oowp[100];
int main(){
	int tcase;
	cin>>tcase;
	for(int itcase=1; itcase<=tcase; ++itcase){
		memset(map, 0, sizeof(map));
		memset(win, 0, sizeof(all));
		memset(all, 0, sizeof(all));
		int n;
		cin>>n;
		for(int i=0; i<n; ++i)
			cin>>map[i];
		for(int i=0; i<n; ++i){
			for(int j=0; j<n; ++j){
				if(map[i][j]=='1')
					++all[i], ++win[i];
				if(map[i][j]=='0')
					++all[i];
			}
			wp[i] = double(win[i]) / all[i];
		}
		//OWP
		for(int i=0; i<n; ++i){
			double sum_wp=0.0;
			for(int j=0; j<n; ++j)
				if(map[i][j]=='1' || map[i][j]=='0')
					sum_wp += double(win[j]-(map[j][i]=='1')) / (all[j]-1);
			owp[i] = sum_wp / all[i];
		}
		//OOWP
		for(int i=0; i<n; ++i){
			double sum_owp=0.0;
			for(int j=0; j<n; ++j)
				if(map[i][j]=='1' || map[i][j]=='0')
					sum_owp += owp[j];
			oowp[i] = sum_owp / all[i];
		}
		printf("Case #%d:\n", itcase);
		for(int i=0; i<n; ++i){
			printf("%.6lf\n", wp[i]*0.25 + owp[i]*0.5 + oowp[i]*0.25);
		}
	}
	return 0;
}
