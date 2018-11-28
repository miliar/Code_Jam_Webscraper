									/*ba yade oo */
//Mehrdad AP

#include <iostream>
#include <string>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <sstream>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>



using namespace std;

#define PI 3.14159265358997
#define absol(x) ((x)>(0) ? (x):(-1)*(x))
#define pow2(x) ((x)*(x))
#define EPS 1e-7
#define INF 100000000
#define MAX 10000
#define MODE 1000000007
#define Left(x) (2*x)
#define Right(x) ((2*(x)+1)
//#define inRange(x,y) (x>=0 && x<N && y>=0 && y<M)

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
typedef long long int lli;

int X,O;
char board[5][5];

void countXO()
{
	X=O=0;
	bool can=true;
	for (int i=0;i<4;i++){

		for (int j=1;j<4 && can;j++){
			if (board[i][j]!=board[i][j-1]) can=false;
		}
		if (can){
			if (board[i][0]=='X') X++;
			else if (board[i][0]=='O') O++;
		}
		can=true;
		for (int j=1;j<4 && can;j++){
			if (board[j][i]!=board[j-1][i]) can=false;
		}
		if (can){
			if (board[0][i]=='X') X++;
			else if (board[0][i]=='O') O++;
		}

	}
	can=true;
	for (int i=1;i<4;i++)
		if (board[i][i]!=board[i-1][i-1]) can=false;
	if (can){
			if (board[0][0]=='X') X++;
			else if (board[0][0]=='O') O++;
		}

	can=true;
	for (int i=1;i<4;i++){
		if (board[i][3-i]!=board[0][3]) can=false;
	}
	if (can){
			if (board[0][3]=='X') X++;
			else if (board[0][3]=='O') O++;
		}
}


int main ()
{

	int tc,TC=0;
	cin>>tc;
	while (tc--){

		int tx=-1,ty=-1;
		bool hasDot=false;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++){
				cin>>board[i][j];
				if (board[i][j]=='T') tx=i,ty=j;
				if (board[i][j]=='.') hasDot=true;

			}

		int win=0;
		int ansX=0,ansO=0;
		if (tx!=-1){
			board[tx][ty]='X';
			countXO();
			if (X>O) win=1;
			else if (X<O) win=2;
			board[tx][ty]='O';
			countXO();
			if (X>O) win=1;
			else if (X<O) win=2;

		}
		else{
			countXO();
			if (X>O) win=1;
			else if (X<O) win=2;
		}
		string ans="";
		if (win==0){
			if (hasDot) ans="Game has not completed";
			else ans="Draw";
		}
		else{
			if (win==1) ans="X won";
			else ans="O won";
		}
		printf("Case #%d: ",++TC);cout<<ans<<endl;
	}


	return 0;
}
