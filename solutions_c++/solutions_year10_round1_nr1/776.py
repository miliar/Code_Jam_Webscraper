#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <cstring>
#include <queue>
#include <utility>
#include <cmath>

#define NM 42
#define inf 0x3f3f3f3f
#define FOR(i,n) for(int i=0;i<(n);i++)
#define fill(c) memset(c,0,sizeof(c))
#define fill1(c) memset(c,-1,sizeof(c))
using namespace std;
typedef  pair< int,int > pii;
typedef  long double LD;



int N,K;
char B[60][60];
char temp[60][60];
void rotate(){
	FOR(i,N)FOR(j,N){
		temp[j][N-i-1]=B[i][j];
		}
	FOR(i,N)FOR(j,N){
		B[i][j]=temp[i][j];
		}
}
void gravity(){
	FOR(k,N)FOR(j,N)FOR(i,N-1)
		if(B[i+1][j]=='.') swap(B[i+1][j],B[i][j]);
	}
bool check(char c){
	int cnt=0;
	FOR(i,N){
		cnt=0;
		FOR(j,N){
		if(B[i][j]==c){cnt++; if(cnt==K) return true;}
		else cnt=0;
		} 
	}
	FOR(j,N){
		cnt=0;
		FOR(i,N){
		if(B[i][j]==c){cnt++; if(cnt==K) return true;}
		else cnt=0;
		} 
	}

	FOR(i,N){
		FOR(j,N){
			cnt=0;	
			FOR(k,N)if(i+k>=N || j+k>=N)break;
			else if(B[i+k][j+k]==c){cnt++; if(cnt==K) return true;}
			else cnt=0;
		} 
	}
	FOR(i,N){
		FOR(j,N){
			cnt=0;	
			FOR(k,N)if(i+k<0 || j+k>=N)break;
			else if(B[i-k][j+k]==c){cnt++; if(cnt==K) return true;}
			else cnt=0;
		} 
	}
	return false;
	}

int main(){

	ifstream in("C:\\Documents and Settings\\Tomy\\Desktop\\in.txt");
	int TC;
	in>>TC;
	FOR(tc,TC){
		in>>N>>K;
		FOR(i,N)FOR(j,N) in>>B[i][j];
		rotate();
		gravity();
		bool rtn1=check('B');
		bool rtn2=check('R');
		string rtn=(rtn1&&rtn2)?"Both":(rtn1?"Blue":(rtn2?"Red":"Neither"));
		cout<<"Case #"<<(tc+1)<<": "<<rtn<<endl;
	}



}
