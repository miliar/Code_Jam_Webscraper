#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
	char input[100][101];
	int n;
	scanf("%d ", &n);
	debug(n);
	for(int i=0; i<n; i++)
		scanf("%s", input[i]);
	int wins[100]={0};
	int games[100]={0};
	for(int i=0; i<n; i++)
	for(int j=0; j<n; j++){
		if(input[i][j]=='1')
			wins[i]++;
		if(input[i][j]!='.')
			games[i]++;
	}
	double wp[100], owp[100], oowp[100];
	for(int i=0; i<n; i++){
		wp[i]=(double)wins[i]/games[i];
	}
	for(int i=0; i<n; i++){
		int opponents=0;
		double sum=0;
		for(int j=0; j<n; j++)
			if(input[i][j]!='.'){
				opponents++;
				int owins=wins[j]-(input[i][j]=='0');
				sum+=(double)owins/(games[j]-1);
			}
		owp[i]=sum/opponents;
	}
	for(int i=0; i<n; i++){
		int opponents=0;
		double sum=0;
		for(int j=0; j<n; j++)
			if(input[i][j]!='.'){
				opponents++;
				sum+=owp[j];
			}
		oowp[i]=sum/opponents;
	}
	for(int i=0; i<n; i++){
		printf("%.10lf\n", wp[i]/4+owp[i]/2+oowp[i]/4);
	}
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": "<<endl;
		eval();
	}
	return 0;
}
