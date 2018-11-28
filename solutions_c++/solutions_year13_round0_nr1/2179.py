#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>

using namespace std;

bool X=false,O=false,Dot=false;

void check(char &a,char &b,char &c,char &d){
	if(a=='.'||b=='.'||c=='.'||d=='.'){
		Dot=true;
		return;
	}
	if((a=='X'||a=='T')&&(b=='X'||b=='T')&&(c=='X'||c=='T')&&(d=='X'||d=='T')){
		X=true;
		return;
	}
	if((a=='O'||a=='T')&&(b=='O'||b=='T')&&(c=='O'||c=='T')&&(d=='O'||d=='T')){
		O=true;
		return;
	}
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		X=O=Dot=false;
		vector<string>v;
		string tmp;
		for (int j = 0; j < 4; j++)
		{
			cin>>tmp;
			v.push_back(tmp);
		}

		for (int j = 0; j < 4; j++)
		{
			tmp=v[j];
			check(tmp[0],tmp[1],tmp[2],tmp[3]);
		}

		for (int j = 0; j < 4; j++)
		{
			check(v[0][j],v[1][j],v[2][j],v[3][j]);
		}
		check(v[0][0],v[1][1],v[2][2],v[3][3]);
		check(v[3][0],v[2][1],v[1][2],v[0][3]);
		if(X&&O){
			printf("Case #%d: Draw\n",i+1);
		}
		else if(X){
			printf("Case #%d: X won\n",i+1);
		}
		else if(O){
			printf("Case #%d: O won\n",i+1);
		}
		else if(Dot){
			printf("Case #%d: Game has not completed\n",i+1);
		}
		else{
			printf("Case #%d: Draw\n",i+1);
		}
	}

}
