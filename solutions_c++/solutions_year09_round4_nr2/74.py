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
#define c first
#define cav second.first
#define y second.second.first
#define x second.second.second
#define INF 1000000

typedef pair<int,int> PII;
typedef pair<vector<vector<char> >,PII> PVII;
typedef pair<int,PVII> PIVII;
	
int main(){
	int Tc;
	cin >> Tc;
	for(int tc=1;tc<=Tc;tc++){
		int R,C,F;
		cin >> R >> C >> F;
		vector<vector<char> > T(R,vector<char>(C));
		for(int i=0;i<R;i++) for(int j=0;j<C;j++) cin >> T[i][j];

		priority_queue<PIVII> pq;
		pq.push(PIVII(-0,PVII(T,PII(0,0))));

		PIVII a;
		vector<vector<map<vector<vector<char> >, int> > >D(R,vector<map<vector<vector<char> >,int> >(C));
		while(!pq.empty()){
			a = pq.top();
			pq.pop();
			a.c = -a.c;
			if(a.cav.size()==1) break;

			if(!D[a.y][a.x].count(a.cav)){
			//	cout << a.y << " " << a.x << " " << a.c << endl;
				
				D[a.y][a.x][a.cav] = a.c;
				vector<vector<char> > T = a.cav;
				vector<vector<char> > vT = T;
				if(a.x != C-1 && T[0][a.x+1]=='.'){
					int caida = 0;
					for(;1 != T.size() && T[1][a.x+1]=='.';caida++) T.erase(T.begin());
					if(caida <= F){
						pq.push(PIVII(-a.c,PVII(T,PII(a.y,a.x+1))));
					}
					T = vT;
				}
				if(a.x != C-1 && T[0][a.x+1]=='.' && T[1][a.x+1]=='#'){
					T[1][a.x+1]='.';
					pq.push(PIVII(-a.c-1,PVII(T,PII(a.y,a.x))));
					T = vT;
				}


				if(a.x != 0 && T[0][a.x-1]=='.'){
					int caida = 0;
					for(;1 != T.size() && T[1][a.x-1]=='.';caida++) T.erase(T.begin());
					if(caida <= F){
						pq.push(PIVII(-a.c,PVII(T,PII(a.y,a.x-1))));
					}
					T = vT;
				}
				if(a.x != 0 && T[0][a.x-1]=='.' && T[1][a.x-1]=='#'){
					T[1][a.x-1]='.';
					pq.push(PIVII(-a.c-1,PVII(T,PII(a.y,a.x))));
					T = vT;
				}

			}
		}




//		for(int i=0;i<R;i++){ for(int j=0;j<C;j++) cout << D[i][j] << " "; cout << endl; }



		cout << "Case #" << tc << ": ";
		if(a.cav.size() == 1) cout << "Yes " << a.c << endl;
		else cout << "No" << endl;
	}
}


















