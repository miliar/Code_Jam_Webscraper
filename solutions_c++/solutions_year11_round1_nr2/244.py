#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long		ui64;
typedef long long				i64;
typedef	vector<int>				vi;
typedef	vector<string>			vs;
typedef	pair<int,int>			pii;
typedef	pair<double,double>		point;

#define pb						push_back
#define mp						make_pair
#define X						first
#define Y						second
#define all(a)					(a).begin(), (a).end()
#define INF						(2000000000)

bool check(string s1, string s2,string alpha, int ends){
	if(s1.size()!=s2.size())
		return false;
	for(int i=0;i<(int)s1.size();i++){
		if(s1[i]=='.'){
			int t = 0;
			while(alpha[t]!=s2[i])
				t++;
			if(t<ends)
				return false;
			continue;
		}
		if(s1[i]!=s2[i])
			return false;
	}

	return true;
}

bool is(char ch, string s){
	for(int i=0;i<(int)s.size();i++)
		if(s[i]==ch)
			return true;
	return false;
}

string corrected(string s, char ch, string key){
	string res = s;
	for(int i=0;i<(int)res.size();i++){
			if(key[i]==ch)
				res[i] = ch;
	}
	return res;
}



int solve(vs a, string s){
	int res = -1;
	int pos = 0;
	string sans = ".";

	for(int i=0;i<(int)a.size();i++){
		sans  = "";
		sans.resize(a[i].size(),'.');
		int tmpans = 0;
		//choose word i
		for(int j=0;j<(int)s.size();j++){
			int words = 0;
			for(int k=0;k<(int)a.size();k++)
				if( check(sans,a[k],s,j) && is(s[j],a[k]) )
					words++;
			if( is(s[j],a[i]) ){
				sans = corrected(sans, s[j], a[i]);
			}
			else
				if(words)
					tmpans++;

		}
		if(res<tmpans){
			res = tmpans;
			pos = i;
		}
	}
//	cout << res << endl;
	return pos;
}

int main(){
	//SMALL INPUT

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests1; cin >> tests1;
	for(int tests=0;tests<tests1;tests++){
		cout << "Case #"<<tests+1 << ": ";
		int n,m;
		cin >> n >> m;
		vs v;
		for(int i=0;i<n;i++){
			string s;cin >> s;
			v.pb(s);
		}

		for(int i=0;i<m;i++){
			string s; cin >> s;
			cout << v[solve(v,s)];
			if(i==m-1)
				cout << endl;
			else
				cout << " ";
			//cout << i << endl;
		}

	}

	return 0;
}