#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>

using namespace std;

int n;
int mat[50][50];
vector<int> arr;
int ans;

bool check(vector<int> &x){
	vector<int>::iterator iter = x.begin();
	int i = 0;
	while( iter!=x.end() ){
		if( (*iter)>i )	return false;
		++i;
		++iter;
	}
	return true;
}

void pnt(vector<int> &x){
	vector<int>::iterator iter = x.begin();
	while( iter!=x.end() ){
		cout << (*iter) << "  ";
		++iter;
	}
	cout << '\n';
}

void solve(){
	ans = -1;
	set< vector<int> > hs;
	queue< vector<int> > QQ;
	queue< int > DQ;
	//pnt( arr );
	if( check(arr) ){
		ans = 0;
		return;
	}
	QQ.push(arr);
	DQ.push(0);
	hs.insert( arr );
	while( ans==-1 && !QQ.empty() ){
		vector<int> src = QQ.front();
		int ds = DQ.front();
		QQ.pop();	DQ.pop();
		//pnt(src);
		//cout << ds << endl;
		for(int i=1;i<src.size();++i){
			int tmp = src[i];
			src[i] = src[i-1];
			src[i-1] = tmp;
			if( hs.find(src)==hs.end() ){
				hs.insert( src );
				QQ.push( src );
				DQ.push( ds+1 );
				if( check( src ) ){
					ans = ds+1;
					break;
				}
			}
			tmp = src[i];
			src[i] = src[i-1];
			src[i-1] = tmp;
		}
	}
}

/*
1
8
00000000
01000000
00000000
01000000
00010000
01111000
01000000
01000000
*/
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	int T, turn;
	cin >> T;
	
	for(turn=0;turn<T;++turn){
		int i, j;
		cin >> n;
		for(i=0;i<n;++i){
			string str;
			cin >> str;
			for(j=0;j<n;++j)	mat[i][j] = str[j]-'0';
		}
		arr.clear();
		for(i=0;i<n;++i){
			for(j=n-1;j>=0;--j){
				if( mat[i][j]==1 ){
					arr.push_back( j );
					break;
				}
			}
			if( j==-1 )	arr.push_back(-1);
		}
		solve();
		printf("Case #%d: %d\n",1+turn,ans);
	}
	
	return 0;
}
