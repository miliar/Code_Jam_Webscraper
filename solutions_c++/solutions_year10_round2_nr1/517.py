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
 

int N,M;
map<string,bool> list;
int main(){

	ifstream in("C:\\Documents and Settings\\Tomy\\Desktop\\in.txt");
	int TC;
	string s;
	in>>TC;
	FOR(tc,TC){
		in>>N>>M;
		int rtn=0;
		list.clear();
		FOR(i,N){in>>s;list[s]=true;}
		FOR(i,M){
			in>>s;
			int prev=0;
			for(int j=1;j<s.length();j++){
				if(s[j]!='/')continue;
				string t=s.substr(0,j);
				if(list.count(t)>0) continue;
				list[t]=true;
				rtn++;
				}
			if(list.count(s)<=0){
				list[s]=true;
				rtn++;
				}
			}

		

		cout<<"Case #"<<(tc+1)<<": "<<rtn<<endl;
	}



}
