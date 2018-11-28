#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
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

using namespace std;

#define FOR(i,a,b) for(int i=(a);(int)i<(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}


int main()
{
   
    freopen("A-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    //1 + 2 + 4 + 8
    
    int cases;
    scanf("%d",&cases);
    REP(v,cases) {
        int n,k;
        scanf("%d %d",&n,&k);
        printf("Case #%d: ",v+1); 
        int a = 0;
        a = (int)pow(2.0,n);     
        if((k+1)%a==0) printf("ON");
        else printf("OFF");
        printf("\n");
    }

     return 0;
}
