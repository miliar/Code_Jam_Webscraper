#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <string>
#include <numeric>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int T;
int A,B;

void getResult(){
    char s[20];
    sprintf(s,"%d",A);
    int l = strlen(s);
    int count = 0;
    int m,n;
    for(m=A;m<B;m++){
       for(int i=1;i<l;i++){
           int tmp = pow(10,i);
           n = m/tmp + (m%tmp)*pow(10,l-i);
           if(n>m&&n<=B){
               count++;
           }
       }
    }
    cout<<count<<endl;
}

int main(){
    freopen("C-small.in","r",stdin);

    cin>>T;
    for(int Case=1;Case<T+1;Case++){
        cin>>A>>B;
        cout<<"Case #"<<Case<<": ";
        getResult();
    }
    return 0;
}
