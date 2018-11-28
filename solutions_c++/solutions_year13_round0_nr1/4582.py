#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define fori(i,j,n) for (int i = j; i <= n; i++)
#define ford(i,n,j) for (int i = n; i >= j; i--)
#define every(t) t.begin(),t.end()
#define pb(t) push_back(t)
#define mk(a,b) make_pair(a,b)
#define ll long long
#define inf 1 << 30

void openFiles() {
    freopen("input.txt", "r",stdin);
    freopen("output.txt","w",stdout);
}

int n = 4, t;

string s[4];

bool checkline(int i,int j,int ii, int jj,char c) {
	int cnt = 0;
	while(i >= 0 && j >= 0 && i < n && j < n) {
		if (s[i][j] == c || s[i][j] == 'T')
			cnt++;
		i += ii;
		j += jj;
	}
	return cnt == n;
}

bool checkplayer(char c) {
	fori(i,0,3)
		if (checkline(0,i,1,0,c))
			return true;
	fori(i,0,3)
		if (checkline(i,0,0,1,c))
			return true;
	if (checkline(0,0,1,1,c) || checkline(0,3,1,-1,c))
		return true;
	return false;
}

int getcnt() {
	int cnt = 0;
	fori(i,0,3)
		fori(j,0,3)
			cnt += (s[i][j] != '.');
	return cnt;
}

int main() {
	openFiles();
	cin>>t;
	int k = 0;
	while(k++ < t) {
		fori(i,0,3)
			cin>>s[i];
		cin.clear();
		if (checkplayer('X'))
			cout<<"Case #"<<k<<": X won"<<endl;
		else if (checkplayer('O'))
				cout<<"Case #"<<k<<": O won"<<endl;
		else if (getcnt() == 16)
			cout<<"Case #"<<k<<": Draw"<<endl;
		else
			cout<<"Case #"<<k<<": Game has not completed"<<endl;
	}
    return 0;
}
