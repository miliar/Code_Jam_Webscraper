#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<vector>
#include<cstring>
#include<stack>
#include<climits>

using namespace std;

int main(){
	char M[5][5];
	string s;
	char win;
	int i,j,test,flag,num,O,X,T,blank;
	cin >> test;
	for(num=1;num<=test;num++){
		flag = 0;
		blank = 0;
		for(i=1;i<=4;i++){
			cin >> s;
			for(j=0;j<4;j++){
				M[i][j+1] = s[j];
				if(s[j] == '.')
					blank++;
			}
		}
		for(i=1;i<=4;i++){
			O = X = T = 0;
			for(j=1;j<=4;j++){
				if(M[i][j] == 'O')
					O++;
				else if(M[i][j] == 'X')
					X++;
				else if(M[i][j] == 'T')
					T++;
			}
			if(O == 4 || (O == 3 && T == 1)){
				win = 'O';
				flag = 1;
				break;
			}
			if(X == 4 || (X == 3 && T == 1)){
				win = 'X';
				flag = 1;
				break;
			}
		}
		if(flag){
			printf("Case #%d: %c won\n",num,win);
			continue;
		}
		for(i=1;i<=4;i++){
			O = X = T = 0;
			for(j=1;j<=4;j++){
				if(M[j][i] == 'O')
					O++;
				else if(M[j][i] == 'X')
					X++;
				else if(M[j][i] == 'T')
					T++;
			}
			if(O == 4 || (O == 3 && T == 1)){
				win = 'O';
				flag = 1;
				break;
			}
			if(X == 4 || (X == 3 && T == 1)){
				win = 'X';
				flag = 1;
				break;
			}
		}
		if(flag){
			printf("Case #%d: %c won\n",num,win);
			continue;
		}
		O = X = T = 0;
		for(i=1;i<=4;i++){
			if(M[i][i] == 'O')
				O++;
			else if(M[i][i] == 'X')
				X++;
			else if(M[i][i] == 'T')
				T++;
		}
		if(O == 4 || (O == 3 && T == 1)){
			win = 'O';
			printf("Case #%d: %c won\n",num,win);
			continue;
		}
		if(X == 4 || (X == 3 && T == 1)){
			win = 'X';
			printf("Case #%d: %c won\n",num,win);
			continue;
		}
		O = X = T = 0;
		for(i=1;i<=4;i++){
			if(M[i][5-i] == 'O')
				O++;
			else if(M[i][5-i] == 'X')
				X++;
			else if(M[i][5-i] == 'T')
				T++;
		}
		if(O == 4 || (O == 3 && T == 1)){
			win = 'O';
			printf("Case #%d: %c won\n",num,win);
			continue;
		}
		if(X == 4 || (X == 3 && T == 1)){
			win = 'X';
			printf("Case #%d: %c won\n",num,win);
			continue;
		}
		if(!blank)
			printf("Case #%d: Draw\n",num);
		else
			printf("Case #%d: Game has not completed\n",num);
	}
	return 0;
}
