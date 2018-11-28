#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <sstream>
#include <utility>
#pragma comment (linker, "/STACK:90000000")
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) a.begin(), a.end()
#define pb push_back
#define PII pair<int, int>
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
using namespace std;


char asd[256][256];
bool qwe[256][256];

void solve(int tc){
	int c;
	cin >> c;
	memset(asd,0,sizeof(asd));
	memset(qwe,0,sizeof(qwe));

	forn(i,c){
		string s;
		cin >> s;
		asd[s[0]][s[1]]=asd[s[1]][s[0]]=s[2];
	}
	int d;
	cin >> d;
	forn(i,d){
		string s;
		cin >> s;
		qwe[s[0]][s[1]]=qwe[s[1]][s[0]]=true;
	}
	string s;
	cin >> s;
	cin >> s;
	string res="";
	fors(i, s){
		if (res.length()==0){
			res+=s[i];
		}else {
			res+=s[i];
			if (asd[res[res.length()-1]][res[res.length()-2]]){
				char c = asd[res[res.length()-1]][res[res.length()-2]];
				res=res.substr(0, res.length()-2);
				res+=c;
			}else{
				forv(i,res){
					if (i==res.length()-1)break;
					if (qwe[res[i]][res[res.length()-1]]){
						res="";
						break;
					}
				}
			}
		}
	}
	printf("Case #%d: [", tc);
	if (res.size()){
		printf("%c", res[0]);
		for(int i=1;i<res.length();++i){
			printf(", %c", res[i]);
		}
	}
	printf("]\n");

}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int q=0,w=0;
	int tc;
	cin >> tc;
	forn(i,tc){
		solve(i+1);
	}

	return 0;
} 