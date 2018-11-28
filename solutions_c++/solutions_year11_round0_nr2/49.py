#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<numeric>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;
#define pb push_back
#define mp make_pair

int main(){
	int runs;
	scanf("%d",&runs);
	for(int r = 1; r <= runs; r++){
		int c;
		cin>>c;
		map< pair<char,char>, char> M;
		string tmp;
		for(int j=0; j<c;j++){
			cin>>tmp;
			M[mp(tmp[0],tmp[1])] = tmp[2];
			M[mp(tmp[1],tmp[0])] = tmp[2];
		}
   
		int d;cin>>d;set<pair<char,char> > Sx;
		for(int j = 0; j < d;j++){
			cin>>tmp;
			Sx.insert(mp(tmp[0],tmp[1])); Sx.insert(mp(tmp[1],tmp[0]));
		}
   
		int n; string Q;  
		cin>>n>>Q; string RES="";
		for(int j=0; j < n; j++){
			if(!RES.size()) RES += Q[j];
			else{
				if(M.count(mp(RES[RES.size()-1],Q[j]))){
				RES[RES.size()-1] = M[mp(RES[RES.size()-1],Q[j])];
				continue;
			}
			else if(M.count(mp(Q[j],RES[RES.size()-1]))){
				RES[RES.size()-1] = M[mp(Q[j],RES[RES.size()-1])];
				continue;
			}
			else{
				int _p = -1;
				for(int k = RES.size()-1; k >= 0; k--){
					if(Sx.count(mp(RES[k],Q[j])) || Sx.count(mp(Q[j],RES[k]))){
						_p = k; break;
					}
				}
				if(_p != -1){ RES=""; continue; }
			}
			RES += Q[j];
			}

		}
		printf("Case #%d: [",r);
		for(int j = 0; j<RES.size(); j++){
			if(!j) cout<<RES[j];
			else cout<<", "<<RES[j];
		}
		printf("]\n");
	}
 
	return 0;
}
