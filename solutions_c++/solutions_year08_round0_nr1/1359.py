#include<iostream>
#include<cassert>
#include<string.h>
using namespace std;

const int MAXN = 21;
const int MAXS = 101;
const int MAXQ = 1001;
const int MAXLEN = 103;
int N;
int S;
int Q;

char strS[MAXS][MAXLEN];
int seq[MAXQ];
int next[MAXQ][MAXS];
int rec[MAXQ];

void init(){
	cin>>S;
	char c;
	while((c=cin.get()) && c=='\n');
	cin.unget();
	for(int i=0; i<S; i++)
		cin.getline(strS[i], MAXLEN);
	cin>>Q;
	for(int i=0; i<Q; i++){
		char tmp[MAXLEN];
		while((c=cin.get()) && c=='\n');
		cin.unget();
		cin.getline(tmp, MAXLEN);
		int pos;
		//match S
		for(pos=0; pos<S; pos++)
			if(0 == strcmp(strS[pos], tmp))
				break;
		assert(pos < S);
		seq[i] = pos;
	}

	//clear
	memset(next, 0, sizeof(next));
	memset(rec, 0, sizeof(rec));
}

void get_next(){
	int last[MAXS];
	for(int i=0; i<S; i++)
		last[i] = Q;

	for(int j=0; j<S; j++)
		next[Q][j] = Q;

	for(int i=Q-1; i>=0; i--){
		int pos;
		for(int j=0; j<S; j++){
			if(seq[i] == j)
				last[j] = i;
			next[i][j] = last[j];	
		}
	}
}

int dp(int x){
	if(x >= Q)
		return 0;
	if(rec[x] > 0)
		return rec[x];
	int min;
	min = Q + 1;
	for(int i=0; i<S; i++){
		if(i != seq[x]){
		 	int tmp =  1+ dp(next[x][i]);
			if(tmp < min)
				min = tmp;
		}
	}
	rec[x] = min;
	return min;
}

int main(){
	cin>>N;
	for(int i=1; i<=N; i++){
		init();
		get_next();
		int out = 0;
		if(Q > 0)
			out = dp(0)-1;
		cout<<"Case #"<<i<<": "<<out<<endl;

	}
}
