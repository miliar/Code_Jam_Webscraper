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

int get(int N, int special, int lagbe, VI arr) {
    
    int ret = 0;
    SORT(arr);
    //print(arr);
    int l = arr.S;
    
    FOR(i,0,l) {
        
        bool finish = false;
        int val = arr[i];
        int ppt = (val) / 3;
        int lo = ppt - 4;int hi = ppt+5;
        
        if(special > 0) {
            
            //Try special
            FOR(i,lo,hi)FOR(j,lo,hi)FOR(k,lo,hi) {
                
                if(finish)continue;
                
                if(i < 0 || j < 0 || k < 0)continue;
                if(i + j + k != val)continue;
                VI as;as.PB(i); as.PB(j); as.PB(k); SORT(as);
                if(as[2] - as[0] != 2)continue;
                
                
                if(as[2] >= lagbe) {
                    special--;
                    ret++;
                    finish = true;
                }
            }
        }
        
        if(finish)continue;
        
        
        //Try not special
        FOR(i,lo,hi)FOR(j,lo,hi)FOR(k,lo,hi) {
                
            if(finish)continue;
            
            if(i < 0 || j < 0 || k < 0)continue;
            if(i + j + k != val)continue;
            VI as;as.PB(i); as.PB(j); as.PB(k); SORT(as);
            if(as[2] - as[0] > 1)continue;
                
                
            if(as[2] >= lagbe) {
                
                ret++;
                finish = true;
            }
        }
        
    }
    
    return special == 0 ? ret : ret;
}

int main() {


	freopen("B-large.in", "r", stdin);
	freopen("B_out_large.txt", "w", stdout);
	
	int T;
	cin >> T;
	
	FOR(t,0,T) {
        
        int N, s, p, vl; VI arr; 
        cin >> N >> s >> p;
        FOR(i,0,N) {
            
            cin >> vl;
            arr.PB(vl);
        }
        
        int res = get(N, s, p, arr);
        
        printf("Case #%d: %d\n", t+1, res);
	}

	return 0;
}

