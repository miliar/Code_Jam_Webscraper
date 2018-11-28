#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <stdlib.h>
#include <ctime>
#include <fstream>

using namespace std;

void add(int r,int c,char ch);
void make(char ch,int ta[]);
int M,N,K;
int a[600][600];
char s[200];
map<int,int> ans;
void work(int);
void solve(int r,int c,int d);
void pr();
int main() {
	//freopen("f:\\c-small.in","r",stdin); freopen("f:\\c-small.out","w",stdout);
	freopen("f:\\c-large.in","r",stdin); freopen("f:\\c-large.out","w",stdout);
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		cout<<"Case #"<<j<<": ";
		cin>>M>>N;
		ans.clear();
		for(int i=0;i<M;i++){
			scanf("%s",s);
			int len = strlen(s);
			for(int k=0;k<len;k++){
				add(i,k*4,s[k]);
			}

		}
	//	pr();
		K=min(M,N);
		for(int i=K;i>=1;i--){
			work(i);
		}
		cout<<ans.size()<<endl;
		map<int,int> ::reverse_iterator iter = ans.rbegin();
		while(iter != ans.rend()) {
			cout<<iter->first<<" "<<iter->second<<endl;
			iter++;
		}
	}
}
void work(int d) {
	for(int i=0;i<M-d+1;i++){
		for(int j=0;j<N-d+1;j++){
			solve(i,j,d);
		}
	}
}

void solve(int r,int c,int d) {
	int lastr;
	int lastc;
//	cout<<r<<c<<endl;
	lastr=a[r][c];
	lastc=a[r][c];
	if(lastr==2) return;
	for(int i=0;i<d;i++){
		
		if(i!=0 && a[r+i][c]==lastr) return ;
		else {
			lastr=a[r+i][c];
			lastc=a[r+i][c];
		}
		if(lastr==2) return;
		for(int j=1;j<d;j++){			
			if(a[r+i][c+j]==lastc) return;
			lastc=a[r+i][c+j];
			if(lastc==2) return;
		}
	}
	for(int i=0;i<d;i++){
		for(int j=0;j<d;j++){
			a[r+i][c+j]=2;
		}
	}
	ans[d]+=1;
//	pr();
}

void pr() {
	cout<<"*************************"<<endl;
	for(int i=0;i<M;i++){
		for(int j=0;j<N;j++){
			cout<<a[i][j];
		}
		cout<<endl;
	}
}
void add(int r,int c,char ch) {
	int atmp[4];
	make(ch,atmp);
	for(int i=0;i<4;i++){
		a[r][c+i]=atmp[i];
	}
}
void make(char ch,int ta[]){
	if(ch=='0') {
		ta[0]=0; ta[1]=0;ta[2]=0;ta[3]=0;
	}
	if(ch=='1'){
		ta[0]=0; ta[1]=0;ta[2]=0;ta[3]=1;
	}
	if(ch=='2'){
		ta[0]=0; ta[1]=0;ta[2]=1;ta[3]=0;
	}
	if(ch=='3'){
		ta[0]=0; ta[1]=0;ta[2]=1;ta[3]=1;
	}
	if(ch=='4'){
		ta[0]=0; ta[1]=1;ta[2]=0;ta[3]=0;
	}
	if(ch=='5'){
		ta[0]=0; ta[1]=1;ta[2]=0;ta[3]=1;
	}
	if(ch=='6'){
		ta[0]=0; ta[1]=1;ta[2]=1;ta[3]=0;
	}
	if(ch=='7'){
		ta[0]=0; ta[1]=1;ta[2]=1;ta[3]=1;
	}
	if(ch=='8') {
		ta[0]=1; ta[1]=0;ta[2]=0;ta[3]=0;
	}
	if(ch=='9') {
		ta[0]=1; ta[1]=0;ta[2]=0;ta[3]=1;
	}
	if(ch=='A') {
		ta[0]=1; ta[1]=0;ta[2]=1;ta[3]=0;
	}
	if(ch=='B') {
		ta[0]=1; ta[1]=0;ta[2]=1;ta[3]=1;
	}
	if(ch=='C') {
		ta[0]=1; ta[1]=1;ta[2]=0;ta[3]=0;
	}
	if(ch=='D') {
		ta[0]=1; ta[1]=1;ta[2]=0;ta[3]=1;
	}
	if(ch=='E') {
		ta[0]=1; ta[1]=1;ta[2]=1;ta[3]=0;
	}
	if(ch=='F') {
		ta[0]=1; ta[1]=1;ta[2]=1;ta[3]=1;
	}
}