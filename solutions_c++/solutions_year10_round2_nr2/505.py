#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <cstring>
#include <queue>
#include <utility>
#include <cmath>
#include <map>

#define NM 42
#define inf 0x3f3f3f3f
#define FOR(i,n) for(int i=0;i<(n);i++)
#define fill(c) memset(c,0,sizeof(c))
#define fill1(c) memset(c,-1,sizeof(c))
using namespace std;
typedef  pair< int,int > pii;
typedef  long double LD;
 

long N,K,B,T;
long X[60],V[60];

int main(){

	ifstream in("C:\\Documents and Settings\\Tomy\\Desktop\\in.txt");
	int TC;
	string s;
	in>>TC;
	FOR(tc,TC){
		in>>N>>K>>B>>T;
		FOR(i,N) in>>X[i];
		FOR(i,N) in>>V[i];
		int rtn=0;
		int kcnt=0;
		for(int i=N-1;i>=0;i--){
			if((B-X[i]) <= V[i]*T){
				kcnt++;				
				for(int j=i+1;j<N;j++){
					if((B-X[j]) <= V[j]*T){						
						}else{
						swap(X[i],X[j]);
						swap(V[i],V[j]);
						rtn++;
						}
				}
				if(kcnt==K) break;
				}
	
		}
		if(kcnt<K)cout<<"Case #"<<(tc+1)<<": IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<(tc+1)<<": "<<rtn<<endl;
	}



}
