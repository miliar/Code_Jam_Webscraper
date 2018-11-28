#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
int ntest;
set<string> st;
string s;
int res;
int f(string s){
    if(st.count(s)) return 0;
    int r=0;    
    st.insert(s);
    for(int i=s.length()-1; i>-1; i--){
        if(s[i]=='/'){
            string t = s.substr(0,i);            
            r++;
            if(st.count(t)) break;            
            if(i) st.insert(t);
        }
    }    
    return r;        
}
int n,q;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    for(int test=0; test<ntest; test++){
        printf("Case #%d: ",test+1);        
        st.clear();
        scanf("%d %d\n",&n,&q);
        for(int i=0; i<n; i++){     
            getline(cin,s);
            st.insert(s);
        }
        res=0;
        for(int i=0; i<q; i++){
            getline(cin,s);
            res += f(s);
        }
        printf("%d\n",res);
    }
    return 0;
}
