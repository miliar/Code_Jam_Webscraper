#include <iostream>
#include <cstring>
#include <cstdio>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>

#define F first
#define S second

using namespace std;
typedef long long int ll;

string board[110];

double wp[110];
double owp[110];
double oowp[110];
int n;

double Wp(int i, int thrown) {
	double total = 0 , won= 0;
	for(int j = 0; j < n; j++) if(board[i][j]!='.')
	if(j!=thrown) {
		total+=1.;
		if(board[i][j] == '1') won+=1.;
	}
	return won/total;
}

int main () {
	int t;
	cin >> t;
	for(int caso = 1; caso <= t; caso++) {
		cin >> n;
		string s;

		for(int i = 0 ; i < n; i++) 
		{
			cin >> board[i];
		}
		
		for(int i = 0; i < n; i++)
		{
			wp[i] = Wp(i,-1);
		}

		for(int i = 0; i < n; i++)
		{
			double total = 0., acc = 0.;
			for(int j = 0; j<n; j++) if(board[i][j]!='.')
			{
				total+=1.;
				acc+=Wp(j,i);
			}
			owp[i] = acc/total;
		}

		for(int i = 0; i < n; i++)
		{
			double total = 0., acc = 0.;
			for(int j = 0; j<n; j++) if(board[i][j]!='.')
			{
				total+=1.;
				acc+=owp[j];
			}
			oowp[i] = acc/total;
		}
		printf("Case #%d:\n", caso);
		for(int i = 0; i < n; i++)
		{
			printf("%.12lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
