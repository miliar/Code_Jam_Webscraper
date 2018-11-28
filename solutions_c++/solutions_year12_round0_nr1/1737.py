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
#include <queue>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define PB           	push_back
#define INF          	INT_MAX
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
#define B				begin()
#define E				end()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(___i,1,___v.S)cout<<","<<___v[___i];cout<<"]\n";}
#define clr(___x, ___v)	memset(___x, ___v , sizeof ___x);
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)


int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long 					bint;
template<typename T> string tos( T a ) 	{ stringstream ss; string ret; ss << a; ss >> ret; return ret;}

char g[500];

string source[3];
string dest[3];

int main() {


	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A_out.txt", "w", stdout);
	
	clr(g, 0);
	source[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	source[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	source[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	
	dest[0]   = "our language is impossible to understand";
	dest[1]   = "there are twenty six factorial possibilities";
	dest[2]   = "so it is okay if you want to just give up";
	
	char marka[500], markb[500];clr(marka, 0); clr(markb, 0);
	
	FOR(i,0,3) {
        
        int la = source[i].S;
        FOR(j,0,la) {
            g[source[i][j]] = dest[i][j];
            marka[source[i][j]] = 1;
            markb[dest[i][j]] = 1;
        }
	}
	
	string lft, rtt;
	rtt = lft = "";
	
	for(char ch='a'; ch <= 'z';ch++) {
        
        if(marka[ch] == 0){
            lft += ch;
        }
        if(markb[ch] == 0) {
            rtt += ch;
        }
        
        //if(g[ch] != 0)printf("%c => %c\n", ch, g[ch]);
        //else cout << "Not found !!!" << endl;
	}
	//DEBUG(lft); DEBUG(rtt);
	
	int flag = 0;
	if(flag) {
        g['q'] = 'q';
        g['z'] = 'z';
	}
	else {
        g['z'] = 'q';
        g['q'] = 'z';
	}
	
	int T; char nin[200];
	string st;
	
	scanf("%d", &T);gets(nin);
	FOR(t,0,T) {
        
        gets(nin);
        st = nin;
        
        string res = ""; int la = st.S;
        FOR(i,0,la) {
            res += g[st[i]];
        }
        
        printf("Case #%d: %s\n", t+1, res.c_str());
	}

	return 0;
}

