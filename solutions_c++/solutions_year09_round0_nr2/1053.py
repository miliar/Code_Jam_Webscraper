/*
  Problem No : 
  Author     : Debashis Maitra
  Complexity :
  Date       :
*/

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctype.h>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define pb push_back
#define sz size()
#define FOR(i,n) for(int i=1;i<=n;i++)
#define FORALL(i,x) for(int i=0;i<x.size();i++)
#define i64 long long
#define MAX 105
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;
int cases,caseno;
int h,w;
int mat[MAX][MAX];
char tags[]={"abcdefghifklmnopqrstuvwxyz"};
char disp[MAX][MAX];
char tag;
char dir[MAX][MAX];
int parent[MAX*MAX];
int parentClr[MAX*MAX];
int input(){
	cin>>h>>w;
	FOR(i,h){
		FOR(j,w){
			cin>>mat[i][j];
		}
	}
	return 1; 
}
void init(){
	tag='a';
	CLR(mat);
	CLR(disp);
	CLR(parent);
	CLR(parentClr);	
}
bool check(int i,int j){
	if(i<=0||j<=0||i>h||j>w)return false;
	//if(!disp[i][j])disp[i][j]='z'+1;
	return true;
}
int getMin(int i,int j){
	int ret=0;
	int mn=mat[i][j];
	if(check(i-1,j)&&mat[i-1][j]<mn){
		ret=1;
		mn=mat[i-1][j];
	}
	if(check(i,j-1)&&mat[i][j-1]<mn){
		ret=2;
		mn=mat[i][j-1];
	}
	if(check(i,j+1)&&mat[i][j+1]<mn){
		ret=3;
		mn=mat[i][j+1];
	}
	if(check(i+1,j)&&mat[i+1][j]<mn){
		ret=4;
		mn=mat[i+1][j];
	}
	return ret;
}
int getDisp(int x,int y){
	if(!x&&!y)return tag++;
	if(x<y&&x || !y)return x;
	return y;
}
int getParent(int i){
	if(parent[i]==0)return i;
	parent[i]= getParent(parent[i]);
	return parent[i];
}
void makeUnion(int x,int y){
	int retx,rety;
	retx=getParent(x);
	rety=getParent(y);
	if(retx==rety)return;
	if(retx<rety)parent[rety]=retx;
	else parent[retx]=rety;
}
int Union(int x1,int y1,int x2,int y2){
	makeUnion((x1-1)*101+y1,(x2-1)*101+y2);
	return 0;
}
void setColor(int i,int j){
	int ret=getParent((i-1)*101+j);
	if(!parentClr[ret])parentClr[ret]=tag++;
	disp[i][j]=parentClr[ret];
}
void process(){
	//disp[1][1]=tag++;
	FOR(i,h){
		FOR(j,w){			
			switch(getMin(i,j)){
				case 0:
					break;
				case 1:
					//disp[i-1][j]=disp[i][j]=getDisp(disp[i-1][j],disp[i][j]);
					Union(i-1,j,i,j);
					dir[i-1][j]=1;
					break;
				case 2:
					//disp[i][j-1]=disp[i][j]=getDisp(disp[i][j-1],disp[i][j]);
					Union(i,j-1,i,j);
					dir[i][j-1]=1;
					break;
				case 3:
					//disp[i][j+1]=disp[i][j]=getDisp(disp[i][j+1],disp[i][j]);
					dir[i][j+1]=1;
					Union(i,j+1,i,j);
					break;
				case 4:
					//disp[i+1][j]=disp[i][j]=getDisp(disp[i+1][j],disp[i][j]);
					dir[i+1][j]=1;
					Union(i+1,j,i,j);
					break;
				default:
					break;
			}
			//if(!disp[i][j])disp[i][j]=tag++;
		}
	}
	cout<<"Case #"<<(++caseno)<<":\n";
	FOR(i,h){
		FOR(j,w){
			setColor(i,j);
			if(j-1)cout<<' ';
			cout<<disp[i][j];
		}
		cout<<endl;
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("outputL.txt","w",stdout);
	cin>>cases;
	while(cases--){
		init();
		input();
		process();
	}
}
