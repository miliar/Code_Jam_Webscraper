/*-------------------------------------------------------------*/
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <fstream>
#include <stdio.h>
#include <stack>
#include <memory.h>

using namespace std;

#define memset0(x) memset((x),0,sizeof(x)) // 0
#define memsetN(x) memset((x),-1,sizeof(x))  // 0xffffffff = -1
#define memsetM(x) memset((x),0x3f,sizeof(x)) // 0x3f3f3f3f = 1061109567
typedef long long llg;

template<class T>inline void OUTLN(T &arr,int len){
	for(int i=0;i < len;i++)
		cout << arr[i] << " ";
	cout << endl;
}

#define MOD 1000000009
#define EPS 1e-6

/*--------------------------------------------------------------*/
const int n = 4;
char mat[4][4];
int tx,ty;
bool ocur;
bool judge(char c){
	if(ocur)
		mat[tx][ty]=c;
	bool pure=true;
	for(int i=0;i < n;i++){
		pure=true;
		for(int j=0;j < n;j++)
			if(mat[i][j] != c)
				pure=false;
		if(pure) return true;
	}
	for(int i=0;i < n;i++){
		pure=true;
		for(int j=0;j < n;j++)
			if(mat[j][i] != c)
				pure=false;
		if(pure) return true;
	}
	if(mat[0][0] == c && mat[1][1] == c && mat[2][2] == c && mat[3][3] == c)
		return true;
	if(mat[0][3] == c && mat[1][2] == c && mat[2][1] == c && mat[3][0] == c)
		return true;
	return false;
}
int main(){
	freopen("A-large.in","r",stdin);
	//freopen("in.txt","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin >> T;
	int _c=1;
	while(T--){
		for(int i=0;i < n;i++){
				for(int j=0;j < n;j++)
					cin >> mat[i][j];
		}
		ocur=false;
		for(int i=0;i < n;i++)
			for(int j=0;j < n;j++)
				if(mat[i][j] == 'T'){
					ocur=true;
					tx=i,ty=j;
				}
		bool f1=judge('X');
		bool f2=judge('O');
		string str;
		if(f1 == f2){
			str = "Draw";
			bool f3=false;
			for(int i=0;i < n;i++)
				for(int j=0;j < n;j++){
					if(mat[i][j] == '.')
						f3 = true;
				}
			if(f3) str="Game has not completed";
		}
		if(f1)
			str = "X won";
		if(f2)
			str = "O won";
		cout << "Case #" << _c++ << ": " << str << endl;
	}
	fclose(stdout);
	return 0;
}