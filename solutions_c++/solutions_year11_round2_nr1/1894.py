#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

double get_wp(vector<vector<char> > maj,int n){
	int zero = 0, one = 0;
	for(int i=0;i<maj.size();i++){
		if(maj[n][i] == '1') one++;
		if(maj[n][i] == '0') zero++;
	}
	return one/(one+zero+0.0);
}

double wp_without(vector<vector<char> > maj,int n,int k){
	int zero = 0, one = 0;
	for(int i=0;i<maj.size();i++){
		if(k == i) continue;
		if(maj[n][i] == '1') one++;
		if(maj[n][i] == '0') zero++;
	}
	return one/(one+zero+0.0);
}


double get_owp(vector<vector<char> > maj,int n){
	int cnt = 0;
	double tmp = 0;
	
	for(int i=0;i<maj.size();i++)
		if(i != n && maj[n][i] != '.'){
			tmp+=wp_without(maj, i, n);
			cnt++;
		}

	return (cnt ==0)?1:tmp/(cnt);
}


double get_oowp(vector<vector<char> > maj,vector<double> a,int n){
	double tmp = 0;
	int cnt =0;
	for(int i=0;i<a.size();i++)
		if(i != n && maj[n][i] != '.'){ tmp+=a[i]; cnt++;}

	return tmp/(cnt);
}
int main()
{
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int testcase = 1;testcase <=t;testcase++)
	{
		printf("Case #%d:\n",testcase);
		char c;
		int n;
		scanf("%d",&n);

		vector<vector<char> > a(n,vector<char> (n) );
		//getchar();

		for(int i = 0;i<n;i++){
			getchar();
			for(int j=0;j<n;j++)
				a[i][j] = getchar();
		}
		vector<double> WP(n), OWP(n), OOWP(n);

		for(int i=0;i<n;i++)
			WP[i] = get_wp(a,i);

		for(int i=0;i<n;i++)
			OWP[i] = get_owp(a,i);

		for(int i=0;i<n;i++)
			OOWP[i] = get_oowp(a,OWP,i);


		for(int i=0;i<n;i++)
			printf("%.9lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
	}
	return 0;
} 