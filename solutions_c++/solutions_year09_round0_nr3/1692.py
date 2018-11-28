#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORD(i,n,e) for(int i=(n)-1;i>=(e);--i)

const bool dbg = 0;
const int MAXN = 600;
char line[MAXN];
char welcome[] = "welcome to code jam";
const int N = 20;
const int M = 1000;
int count[N];
int tmp[N];

void compute(int cas){
	cin.getline(line,MAXN);
	if(dbg)cout << cas+1 << ": " << string(line);
	int n = strlen(line);
	if(dbg)cout << " ("<<n<<")"<<endl;
	REP(i,N)
		count[i] = 0;
	count[N-1] = 1;
	FORD(i,n,0){
		if(dbg)cout << "i: " << i <<endl;
		FORD(j,N-1,0){
			if(dbg)cout << "j: "<< j << endl;
			tmp[j] = count[j];
			if(welcome[j] == line[i])
				tmp[j] += count[j+1];

		}
		REP(j,N-1)
			count[j] = tmp[j] % M;
	}
	printf("Case #%d: %04d\n",cas+1,count[0]);

}



int main(){
	int t;
	cin>>t;
	cin.getline(line,MAXN);
	REP(i,t)
		compute(i);
}
