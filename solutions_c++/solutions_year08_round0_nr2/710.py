#include <cstdio>
#include <vector>
#include <sstream>
#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FRR(i,a,b) for(int i=b-1;i>=0;i--)
#define VI vector<int>
#define VVI vector< VI >
#define VS vector<string>
#define INF 2000000000
#define sz size()
#define pb push_back
#define mp make_pair
#define ll long long int
#define print(v,n) {FOR(i,0,n)cout<<v[i]<<" ";}cout<<endl;
#define pii pair<int, int> 


int getTime(string s){
	int hh, mm;
	sscanf(s.c_str(),"%d:%d", &hh, &mm);
	return hh*60 + mm;
}

int arrA[3000], arrB[3000];
int depA[3000], depB[3000];

int main(){
	int cases; cin >> cases;
	FOR(test, 1 , cases + 1){
		int NA, NB, T;
		cin >> T >> NA >> NB;
		memset(arrA, 0 , sizeof(arrA));
		memset(arrB, 0 , sizeof(arrB));
		memset(depA, 0 , sizeof(depA));
		memset(depB, 0 , sizeof(depB));
		FOR(i,0,NA){
			string x,y; cin >> x >> y;
			depA[getTime(x)]++;
			arrB[getTime(y) + T]++;
			
		}
		FOR(i,0,NB){
			string x,y; cin >> x >> y;
			depB[getTime(x)]++;
			arrA[getTime(y) + T]++;
		}
		int reqa = 0, reqb = 0, ava = 0, avb = 0;
		FOR(t,0,3001){
			ava+= arrA[t]; avb += arrB[t];
			if(ava >= depA[t])ava -= depA[t];
			else {
				reqa += depA[t] - ava;
				ava = 0;
			}
			if(avb >= depB[t])avb -= depB[t];
			else {
				reqb += depB[t] - avb;
				avb = 0;
			}
		}
		cout << "Case #" << test<< ": " << reqa << " " << reqb << endl;
		
	}
}


