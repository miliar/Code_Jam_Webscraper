#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<utility>
#include<set>
#include<string.h>
#include<stack>
#include<queue>
#include<cmath>
#define FOR(a,b) for(int a=0;a<b;a++)
#define RFOR(a,b) for(int a=b-1;a>=0;a--)
#define PI pair<int,int>
#define PB(a) push_back(a)
#define SEP(a,b) (0<=a && a<m && 0<=b && b<n)
using namespace std;

int ttt;

long long l, p, c;
double tot,sol;

int main(){
	cin >> ttt;
	for(int tt=1;tt<=ttt;tt++){
		cin >> l >> p >> c;
		tot = 0;
		l*=c;
		while(l<p){
			tot++;
			l*=c;
		}
		if(tot==0){
			sol = 0.0;
		}
		else {
			sol = 1.0 + (floor(log(tot)/log(2.0)));
		}
	
		cout << "Case #" << tt << ": " << (long long)sol << endl;
	}
}
