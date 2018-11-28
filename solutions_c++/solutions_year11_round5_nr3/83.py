#include <iostream>
#include <set>
#include <algorithm>
#include <cstdio>

using namespace std;

int r,c,ans;
char s[111][111];

pair<int,int> dir[111][111];

void check(){
	set<pair<int,int> > s;
	for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
			s.insert(make_pair(i,j));
	for(int i=0;i<300;i++){
		set<pair<int,int> > n;
		for(set<pair<int,int> >::iterator it=s.begin();it!=s.end();it++){
			pair<int,int> cur = *it;
			int x = cur.first + dir[cur.first][cur.second].first;
			int y = cur.second + dir[cur.first][cur.second].second;
			x = (x+r) % r;
			y = (y+c) % c;
			if(x>=0&&y>=0&&x<r&&y<c){
				if(n.find(make_pair(x,y))!=n.end())
					return;
				n.insert(make_pair(x,y));
			}
		}
		s=n;
	}
	ans++;
}

void go(int x,int y){
	if(y==c){
		go(x+1,0);
		return;
	}
	else if(x==r){
		check();
		return;
	}
	if(s[x][y]=='|'){
		dir[x][y]=make_pair(-1,0);
		go(x,y+1);
		dir[x][y]=make_pair(1,0);
		go(x,y+1);
	}
	else if(s[x][y]=='-'){
		dir[x][y]=make_pair(0,-1);
		go(x,y+1);
		dir[x][y]=make_pair(0,1);
		go(x,y+1);
	}
	else if(s[x][y]=='/'){
		dir[x][y]=make_pair(-1,1);
		go(x,y+1);
		dir[x][y]=make_pair(1,-1);
		go(x,y+1);
	}
	else{
		dir[x][y]=make_pair(1,1);
		go(x,y+1);
		dir[x][y]=make_pair(-1,-1);
		go(x,y+1);
	}
}

int main(){
	int t;
	cin >> t;
	for(int cc=0;cc<t;cc++){
		printf("Case #%d: ", cc+1);
		cin >> r >> c;
		for(int i=0;i<r;i++)
			cin >> s[i];
		ans=0;
		go(0,0);
		cout << ans << endl;
	}
	return 0;
}
