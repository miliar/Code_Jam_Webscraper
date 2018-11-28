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

char in[20][20];

int gval(int v, int t) {
    
    if(v == 4)return 1;
    if(v == 3 && t == 1)return 1;
    return 0;
}

int win(char ch) {
    
    FOR(i,0,4) {
        
        int v, t;
        v = t = 0;
        FOR(j,0,4) {
            if(in[i][j] == ch)v++;
            if(in[i][j] == 'T')t++;
        }
        if(gval(v,t))return 1;
    }
    
    FOR(i,0,4) {
        
        int v, t;
        v = t = 0;
        FOR(j,0,4) {
            if(in[j][i] == ch)v++;
            if(in[j][i] == 'T')t++;
        }
        if(gval(v,t))return 1;
    }
    
    int v, t;
    v = t = 0;
    FOR(i,0,4) {
        
        if(in[i][i] == ch)v++;
        if(in[i][i] == 'T')t++;
    }
    if(gval(v,t))return 1;
    
    v = t = 0;
    FOR(i,0,4) {
        
        if(in[i][4-i-1] == ch)v++;
        if(in[i][4-i-1] == 'T')t++;
    }
    if(gval(v,t))return 1;
    
    return 0;
}

int vora() {
    
    FOR(i,0,4)FOR(j,0,4)if(in[i][j] == '.')return 0;
    return 1;
}

int main() {


	freopen("A-large.in", "r", stdin);
	freopen("A_large_out.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	FOR(t, 0, T) {
        
        FOR(i,0,4)scanf("%s", &in[i]);
        
        printf("Case #%d: ", t+1);
        
        if(win('X'))printf("X won");
        else if(win('O'))printf("O won");
        else if(vora())printf("Draw");
        else printf("Game has not completed");
        printf("\n");
    }

	return 0;
}

