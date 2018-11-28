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
//#define B				begin()
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

int A, B, ns, omod[20];
char od[10], ov[10], done[2000009];

int get(int now) {
    
    
    int ret = 0;
    sprintf(od, "%d", now);
    int l = strlen(od);
    ns = now;
    
    for(int i = 0;i < l+2;i++) {
        
        if(ns >= A && ns <= B && done[ns] == 0) {
            ret++;
            done[ns] = 1; 
        }
        
        int os = ns;
        int fdigit = ns / omod[l-1]; int lpart = ns % omod[l-1];
        ns = lpart*10 + fdigit;
    }
    
    return (ret*(ret-1))/2;
}

int main() {


	//freopen("C-large.in", "r", stdin);
	//freopen("out_C_large.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	omod[0] = 1;
	FOR(i,1,10)omod[i] = omod[i-1] * 10;
	
	FOR(t,0,T) {
        
        clr(done, 0);
        
        bint res = 0;
        scanf("%d %d", &A, &B);
        FOR(i,A,B+1) {
            
            if(done[i])continue;
            
            res += get(i);
        }
        
        //printf("Case #%d: %d\n", t+1, res);
        cout << "Case #"<<t+1<<": "<<res<<"" << endl;
	}

	return 0;
}

