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
#include <climits>

using namespace std;
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define REP(a,b) FOR(a,0,b)

int main(){
int T;
cin>>T;
for(int i=0;i<T;i++){
int N,S,P;
cin>>N>>S>>P;
int a[N];
    for(int j=0;j<N;j++){
        cin>>a[j];
    }
    int count =0;
    cout<<"Case #"<<i+1<<": ";
for(int j=0;j<N;j++){
        if(a[j]%3 ==0 || a[j]%3 ==1){
                  int temp;
                  temp=((a[j]/3)+(a[j]%3));
                  if(temp>=10)temp=10;
               if(temp >=P && temp<=10){
                       count++;
                       if(a[j]%3 ==0)a[j]=1;
               }
               if(a[j]%3==1)a[j]=1;
        }else if(a[j]%3==2){
                            int temp;
                            temp=((a[j]/3)+(a[j]%3));
                            temp--;
                            if(temp>=10)temp=10;
                            if(temp>=P  && temp<=10){
                                        count++;
                                        a[j]=1;
                            }
        }
}

for(int j=0;j<N;j++){
        if(a[j]%3 ==2 ||a[j]%3==0){
                       int temp;
                       temp=((a[j]/3)+(a[j]%3));
                       if(a[j]%3==0 && a[j]!=0)temp++;
                       if(temp>=10)temp=10;
                       if(S>0 && temp>=P  && temp<=10){
                                count++;
                                S--;
                       }
        }
}
cout<<count<<"\n";
}
//while(1);
return 0;
}
