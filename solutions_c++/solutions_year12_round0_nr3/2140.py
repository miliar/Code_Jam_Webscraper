#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <set>
using namespace std;
int ntest;
int A, B;
int x;
int l;
set<pair<int,int> > st;
void f(int x){
    int res=0;
    int temp=x;
    for(int i=1; i<l; i*=10){
        int t=x/l;
        x = (x%l)*10+t;            
        if(x > temp && x<=B ) st.insert(make_pair(temp,x)) ; 
    }

}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);      
    for(int t=0; t<ntest; t++){    
        scanf("%d %d",&A,&B);
        l=1;
        while(l<=A) l*=10; l/=10;       
        int res=0;        
        st.clear();
        for(int i=A,_n=B+1; i<_n; i++) f(i);
        
        printf("Case #%d: %d\n",t+1,st.size());
    }
    return 0;
}
