#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <stdio.h>
#include <cstring>

using namespace std;

template<class T>
string tostring(T a){stringstream ss; ss<<a; return ss.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])


const int til[]={0,1,1,1,0,-1,-1,-1},
		  tjl[]={1,1,0,-1,-1,-1,0,1};

int main(){
	ifstream be("A-large.in");
	ofstream ki("ki.txt");
	int T; be>>T;
	FOR(tt,T){
		vector<vector<char> > b(4,vector<char>(4));
		FOR(i,4)
			FOR(j,4)
				be>>b[i][j];

		bool vanfree=false;
		FOR(i,4)
			FOR(j,4)
				if(b[i][j]=='.')
					vanfree=true;
		
		char winner=' ';
		FOR(i,4)
			FOR(j,4){
				if(b[i][j]=='X' || b[i][j]=='O'){
					int pi,pj;
					FOR(k,8){
						pi=i, pj=j;
						int il=til[k], jl=tjl[k];
						int c=0;
						while(pi>=0 && pi<4 && pj>=0 && pj<4 && (b[pi][pj]==b[i][j] || b[pi][pj]=='T')){
							pi+=il;
							pj+=jl;
							c++;
						}
						if(c==4)
							winner=b[i][j];
					}
				}
			}
		ki<<"Case #"<<tt+1<<": ";
		if(winner!=' ')
			ki<<winner<<" won"<<endl;
		else
			if(vanfree)
				ki<<"Game has not completed"<<endl;
			else
				ki<<"Draw"<<endl;
	}

	ki.close();
	return 0;
}