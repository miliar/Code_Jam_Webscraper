#pragma warning(disable:4018)  // signed/unsigned mistatch
#pragma warning(disable:4244)  // w64 to int cast
#pragma warning(disable:4267)  // big to small -- possible loss of data
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4800)  // forcing int to bool
#pragma warning(disable:4996)  // deprecations
#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}
using namespace std;
int memo[1010][1010];
bool mark[1010][1010];

int f(const vector <int> &v, int i, int w, int x, int y){
    if(i+w == (int) v.size()){
		if(x == y && i > 0 && w > 0)
			return 0;
		else 
			return -1;
	}
	int &best = memo[i][w];
	//if(mark[i][w])return true;
	//mark[i][w] = true;
	int l1 = f(v,i+1,w,x^v[i+w],y);
	int l2 = f(v,i,w+1,x,y^v[i+w]);
	if(l1 > -1)l1 += v[i+w];
	best = max(l1,l2);
	return best;
}


int main(){
    freopen("data.in","r",stdin);
	freopen("data.out", "w", stdout);
    int casos,n; 
    scanf("%d",&casos); 
    for(int p=1; p<=casos; ++p){
            scanf("%d",&n);
            vector<int> v(n);  
            for(int i=0; i<n; ++i)
                    scanf("%d",&v[i]);
            memset(mark,false,sizeof(mark));
		    int sol = f(v, 0, 0, 0, 0);
		    if(sol == -1){
			printf("Case #%d: NO\n", p);
		 }else printf("Case #%d: %d\n",p, sol);
            }
    
    
return 0;     
}
