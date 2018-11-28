#include <iostream>
#include <cstdio>
#include <vector>
#include <string>


#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)

using namespace std;

int main(){
	int T;cin>>T;
	REP(tt,T){
		int R,C;
		cin>>R>>C;


		vector<string> field;
		field.resize(R);
		REP(i,R)cin>>field[i];

		bool res = true;
		vector<vector<int> > used(R,vector<int>(C,0));

		const int DY[4] = {0,0,1,1};
		const int DX[4] = {0,1,1,0};
		REP(y,R)REP(x,C){
			if(field[y][x]=='#'){
				REP(i,4){
					int ny = y+DY[i];
					int nx = x+DX[i];
					if(ny>=R||nx>=C||field[ny][nx]=='.'){
						res = false;
						continue;
					}
					if(i%2==0)field[ny][nx] = '/';
					else field[ny][nx] = '\\';
				}
			}
		}
		printf("Case #%d:\n",tt+1);
		if(res){
			REP(y,R)printf("%s\n",field[y].c_str());
		}
		else{
			printf("Impossible\n");
		}
	}

	return 0;
}
