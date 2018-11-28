#include <iostream>
#include <cstdio>
#include <algorithm>
#include <complex>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <memory.h>
#include <iostream>
#include<list>
using namespace std;

#define pb push_back
#define sz size()
#define mp make_pair
#define mset(ar,val) memset(ar,val,sizeof ar)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
void scan(int* i) {int t = 0;char c;bool negative = false;c = getchar_unlocked();while (c < '0' || c > '9') {if (c == '-')negative = true;c = getchar_unlocked();}while (c >= '0' && c <= '9') {t = (t << 3) + (t << 1) + c - '0';c = getchar_unlocked();}if (negative)t = ~(t - 1);*i = t;}
void scan(long long int* i) {long long int t = 0;char c;bool negative = false;c = getchar_unlocked();while (c < '0' || c > '9') {if (c == '-')negative = true;c = getchar_unlocked();}while (c >= '0' && c <= '9') {t = (t << 3) + (t << 1) + c - '0';c = getchar_unlocked();}if (negative)t = ~(t - 1);*i = t;}

int main() {
	int T,t,i,j,OtherCount;
	char board[5][5],temp;
	bool Xwon,Owon;
	int Xcounts[8];
	int Ocounts[8];
	// = \ / ||||
	scan(&T);
	for(t=1;t<=T;++t){
		OtherCount=0;
		mset(Xcounts,0);
		mset(Ocounts,0);
		Xwon=Owon=0;
		for(i=0;i<4;++i){
			for(j=0;j<4;++j){
				scanf("%c",&board[i][j]);
				if(board[i][j]=='X'|| board[i][j]=='T'){
					++Xcounts[0];
					++Xcounts[j+3];
					if(i==j)
						++Xcounts[1];
					if(i+j==3)
						++Xcounts[2];
				}
				if(board[i][j]=='O' || board[i][j]=='T'){
					++Ocounts[0];
					++Ocounts[j+3];
					if(i==j)
						++Ocounts[1];
					if(i+j==3)
						++Ocounts[2];
				}
				if(board[i][j]=='.')
					++OtherCount;
			}
			temp=getchar();
			if(Xcounts[0]==4)
				Xwon=1;
			if(Ocounts[0]==4)
				Owon=1;
			Xcounts[0]=Ocounts[0]=0;
		}
		if(Xwon==0 && Owon==0){
			for(i=0;i<7;++i){
				if(Xcounts[i]==4)
					Xwon=1;
				if(Ocounts[i]==4)
					Owon=1;
			}
		}
		if(Xwon==1)
			printf("Case #%d: X won\n",t);
		else if(Owon==1)
			printf("Case #%d: O won\n",t);
		else {
			if(OtherCount!=0)
				printf("Case #%d: Game has not completed\n",t);
			else
				printf("Case #%d: Draw\n",t);
		}
		temp=getchar();

	}
	return 0;
}

