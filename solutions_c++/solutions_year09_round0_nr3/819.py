#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <sstream>
#include <iomanip>

using namespace std;
#define st first
#define fin second.first
#define c second.second
#define INF 2000000000

typedef long long ll;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;


int main(){
	int N;
	cin >> N;
	string s;
	getline(cin,s);
	for(int n=1;n<=N;n++){
		getline(cin,s);
		string wel = "welcome to code jam";
		vector<vector<int> > T(s.size(),vector<int>(wel.size(),0));
		for(int i=0;i<s.size();i++) for(int j=0;j<wel.size();j++){
			if(j==0 && i==0) T[i][j] = ((s[i]=='w')?1:0);
			else if(j==0) T[i][j] = T[i-1][j] + ((s[i]=='w')?1:0);
			else if(i==0) T[i][j] = 0;
			else T[i][j] = T[i-1][j] + ((s[i]==wel[j])?T[i-1][j-1]:0);
			T[i][j] = T[i][j]%10000;
		}
		cout << "Case #" << n << ": ";
		if(T[s.size()-1][wel.size()-1]==0) cout << "0000" << endl;
		else {
			double i = log10(T[s.size()-1][wel.size()-1]);
			while(i < 3){ cout << "0"; i += 1; }
			cout << T[s.size()-1][wel.size()-1] << endl;
		}
	}
}
