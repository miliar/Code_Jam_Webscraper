#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<utility>
#include<set>
#include<string.h>
#include<stack>
#include<queue>
#define FOR(a,b) for(int a=0;a<b;a++)
#define RFOR(a,b) for(int a=b-1;a>=0;a--)
#define PI pair<int,int>
#define PB(a) push_back(a)
#define SEP(a,b) (0<=a && a<m && 0<=b && b<n)
using namespace std;

int ttt, n, aa, bb, sol;

vector< PI  > v;

int main(){
	cin >> ttt;
	for(int tt=1;tt<=ttt;tt++){
		v.clear();
		cin >> n;
		sol = 0;
		FOR(i,n){
			cin >> aa >> bb;
			v.PB( PI(aa,bb) );
		}
			
		FOR(i,n){
			for(int j=i+1;j<n;j++){
				if(v[i].first < v[j].first){
					if(v[i].second > v[j].second){
						sol++;
					}
				}
				else if(v[i].first > v[j].first)
					if(v[i].second < v[j].second)
						sol++;
			}
		}

		cout << "Case #" << tt << ": " << sol << endl;
	}
}
