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
#include <ctime>
#include <string>

using namespace std;

int h,w;
int inp[101][101],frminx[101][101],resinx[101][101];

int mrgxy(int x, int y){return (x*w+y);}
int spltx(int val){return val/w;}
int splty(int val){return val%w;}

void doit(){
	int tmp,tx,ty;
	int dx[4]={-1, 0,0,1};
	int dy[4]={ 0,-1,1,0};
	vector<pair<pair<int,int>,int> > vi;
	pair<pair<int,int>,int> pii;
	map<int,char> mp;
	cin>>h>>w;
	for(int i=0;i<h;i++)for(int j=0;j<w;j++){cin>>inp[i][j];resinx[i][j]=mrgxy(i,j);}
	for(int i=0;i<h;i++)for(int j=0;j<w;j++){
		frminx[i][j]=mrgxy(i,j);
		for(int k=0;k<4;k++){
			tx=i+dx[k];ty=j+dy[k];
			if(tx>=0 && tx<h && ty>=0 && ty<w){
				tmp=frminx[i][j];
				if(inp[spltx(tmp)][splty(tmp)]>inp[tx][ty])frminx[i][j]=mrgxy(tx,ty);
			}
		}
	}
	for(int k=0;k<(h+w);k++){
		for(int i=0;i<h;i++)for(int j=0;j<w;j++){
			resinx[i][j]=resinx[spltx(frminx[i][j])][splty(frminx[i][j])];
		}
	}
	tmp=0;
	for(int i=0;i<h;i++){
		cout<<endl;
		for(int j=0;j<w;j++){
			if(mp.count(resinx[i][j])==0){
				mp[resinx[i][j]]=('a'+tmp);
				tmp++;
			}
			if(j)cout<<" ";
			cout<<mp[resinx[i][j]];
		}
	}
	cout<<endl;
}
int main(){
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++){
		cout<<"Case #"<<i<<":";
		doit();
	}
	return 0;
}