#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define li		long long
#define rep(i,to)	for(li i=0;i<((li)to);i++)
#define pb		push_back
#define sz(v)		((li)v.size())

#define MAX 105

int dp[MAX][MAX][MAX];
int n;
char order0[MAX];
int order1[MAX];
int main(){
	ofstream ofs;
	ofs.open("output.txt");
	ifstream ifs;
	ifs.open("input.txt");
	int m;
	ifs>>m;
	rep(stage,m){
		rep(i,MAX)rep(j,MAX)rep(k,MAX) dp[i][j][k]=-1;
		ifs>>n;
		rep(i,n) ifs>>order0[i]>>order1[i];
		#define make(a,b,c) make_pair(a,make_pair(b,c))
		queue<pair<int,pair<int,int> > > q;
		q.push(make(1,1,0));
		dp[1][1][0]=0;
		int pos0,pos1,button;
		while(sz(q)){
			pair<int,pair<int,int> > p=q.front();
			q.pop();
			pos0=p.first;
			pos1=p.second.first;
			button=p.second.second;
			if(button==n) break;
#define ope(a,b,c) { if(dp[a][b][c]==-1){ dp[a][b][c]=dp[pos0][pos1][button]+1; q.push(make(a,b,c)); } }
			if(pos0<100) ope(pos0+1,pos1,button);
			if(pos0<100 && pos1<100) ope(pos0+1,pos1+1,button);
			if(pos0<100 && pos1>1) ope(pos0+1,pos1-1,button);
			if(pos0<100 && pos1==order1[button] && order0[button]=='B') ope(pos0+1,pos1,button+1);
			if(pos0>1) ope(pos0-1,pos1,button);
			if(pos0>1 && pos1<100) ope(pos0-1,pos1+1,button);
			if(pos0>1 && pos1>1) ope(pos0-1,pos1-1,button);
			if(pos0>1 && pos1==order1[button] && order0[button]=='B') ope(pos0-1,pos1,button+1);
			if(pos0==order1[button] && order0[button]=='O') ope(pos0,pos1,button+1);
			if(pos0==order1[button] && order0[button]=='O' && pos1<100) ope(pos0,pos1+1,button+1);
			if(pos0==order1[button] && order0[button]=='O' && pos1>1) ope(pos0,pos1-1,button+1);
			if(pos1<100) ope(pos0,pos1+1,button);
			if(pos1>1) ope(pos0,pos1-1,button);
			if(pos1==order1[button] && order0[button]=='B') ope(pos0,pos1,button+1);
		}
		ofs<<"Case #"<<stage+1<<": "<<dp[pos0][pos1][button]<<endl;
	}
}
