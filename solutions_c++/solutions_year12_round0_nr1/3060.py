#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define REP(i,j,k) for(int i=j;i<(int)(k);++i)
#define foreach(i,c) for(__typeof(c.begin()) i=c.begin();i!=c.end();++i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef long long ll;
const int INF = 99999999;
const double EPS = 1e-9;

int n;
string s1="abcdefghijklmnopqrstuvwxyz \n";
string s2="yhesocvxduiglbkrztnwjpfmaq \n";

int main()
{
	cin >> n;
	char str2[10];
	cin.getline(str2,10);
	rep(i,n){
		char str[103];
		string ans;
		cin.getline(str,102);
		rep(j,strlen(str)) ans+=s2[s1.find(str[j])];
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	
    return 0;
}
