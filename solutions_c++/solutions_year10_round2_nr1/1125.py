#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <set>
#include <bitset>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define PB(A,B) A.push_back(B);
#define SORT(A) sort( A.begin(),A.end() )
#define ALL(A) A.begin(),A.end()
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define VB vector<bool>
#define SZ(A) int(A.size())
#define LL long long

using namespace std;

int cntDir(VS &disk)
{
	int cnt=0;
	FOR(sr,0,SZ(disk)){
		string sub="";

		FOR(pos,0,SZ(disk[sr])){

			string sub=disk[sr].substr(0,pos+1);
			if(disk[sr][pos]==' '){
				bool found=false;

				FOR(fnd,0,sr)
					if(fnd!=sr){
						string chk=disk[fnd].substr(0,SZ(sub));
						if(chk==sub){
							found=true;
							break;
						}
					}

				if(!found)
					++cnt;
				}
			}
		}

	return cnt;
}

int main()
{
	freopen("A-large.txt","r",stdin);
	freopen("A-large Output.txt","w",stdout);

	int T;
	cin>>T;

	EFOR(cases,1,T){
		int N,M;
		cin>>N>>M;

		VS pres;
		string tmp;

		FOR(inp,0,N){
			cin>>tmp;
			tmp.erase(0,1);
			tmp+=" ";
			replace(tmp.begin(),tmp.end(),'/',' ');
			PB(pres,tmp);
		}
		int init=cntDir(pres);

		FOR(inp,0,M){
			cin>>tmp;
			tmp.erase(0,1);
			tmp+=" ";
			replace(tmp.begin(),tmp.end(),'/',' ');
			PB(pres,tmp);
		}
		int fin=cntDir(pres);
		cout<<"Case #"<<cases<<": "<<fin-init<<"\n";
	}

	return 0;
}
