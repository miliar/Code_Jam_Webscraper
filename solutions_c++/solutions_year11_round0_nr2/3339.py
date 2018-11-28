#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
#include <cstring>
using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define REP(i,a,b)   	for(int (i)=(a);(i)<=(b);(i)++)
typedef long long 		bint;

#define PB           	push_back
#define INF          	1e10
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(i,1,___v.S)cout<<","<<___v[i];cout<<"]\n";}

map<string, string> com;
map<string, bool> opp;

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B.out", "w", stdout);
	
	
	int T, C, D , N;
	string in, st, ns, mukit;
	
	cin >> T;
	
	FOR(t, 0 ,T) {
		
		com.clear();
		opp.clear();
		
		cin >> C ;
		FOR(i,0,C) {
			
			cin >> ns;
			st = ns.substr(0,2);
			com[st] = ns[2];
			
			swap(st[0], st[1]);
			com[st] = ns[2];	
		}
		cin >> D;
		FOR(i,0,D) {
			
			cin >> ns;
			st = ns.substr(0,2);
			opp[st] = true;
			
			swap(st[0], st[1]);
			opp[st] = true;	   
		}
		cin >> N;
		cin >> in;
		
		
		mukit = "";
		FOR(i,0,N) {
			
			bool change = false;
			mukit += in[i];
			int lm = mukit.S;
			if(lm > 1 && com.count(mukit.substr(lm-2, 2)) ) {
				
				change = true;
				string si = com[mukit.substr(lm-2, 2)];
				mukit = mukit.substr(0, lm-2);
				mukit += si;
			}
			if(change==false) {
				
				FOR(j,0,lm) {
					
					FOR(k,j+1, lm) {
						
						char ca = mukit[j];
						char cb = mukit[k];
						string ot = "";
						ot += ca;
						ot += cb;
						if(opp.count(ot) ) {
							
							change = true;
							mukit = "";
							break;
						}
					}
					if(change)break;
				}
			}
		}
		
		
		printf("Case #%d: [", t+1);
		if(mukit.S > 0) {
			
			printf("%c",mukit[0]);
			if(mukit.S > 1)printf(",");
		}
		FOR(i,1,mukit.S) {
			
			if(i < mukit.S-1)printf(" %c,",mukit[i]);
			else printf(" %c",mukit[i]);
		}
		printf("]\n");
	}
	
	return 0;
}

