#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef vector<int> vi;
typedef long long int64;
#define MAX_N 101

int main() {
	int T,N,time;
	char bot;
	short button,orange,blue,sequence[MAX_N];
	short *next_o;
	short *next_b;
	bool next;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>N;
		memset(sequence,0,sizeof(short)*MAX_N);
		for(int n=0;n<N;n++){
			cin>>bot>>button;
			sequence[n]=(bot=='O'?button:-button); 
		}
		orange=1; blue=-1;
		time=0;
		next_o=next_b=sequence;
		for(int n=0;n<N;n++){	
			while(*next_o<0)next_o++;
			while(*next_b>0)next_b++;
			next=false;
			while(!next){
				time++;
				if(orange==sequence[n]){
					next_o++; next=true;
				}
				else if(orange<*next_o) 
					orange++;	
				else if(orange>*next_o)
					orange--;
				if(blue==sequence[n]){
					next_b++; next=true;
				}
				else if(blue<*next_b) 
					blue++;	
				else if(blue>*next_b)
					blue--;					
			}
		}
		cout<<"Case #"<<t<<": "<<time<<endl;
	}
	return 0;
}
