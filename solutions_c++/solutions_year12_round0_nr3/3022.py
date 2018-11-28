#include<iostream>
#include<stdio.h>
#include<cmath>
#include<string.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<sstream>
#include<map>
#include<stack>
#include <utility>
#include <bitset>
#define pb push_back

using namespace std;


int main(){
    map<pair<int,int> , bool> maps;
    int ret;
    int A,B,m,n,i,j,k,t;
    string num;
  //  freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++){
            maps.clear();
            ret=0;
            printf("Case #%d: ",i);
            scanf("%d %d",&A,&B);
            for(n=A;n<=B;n++)
            {
               stringstream ss;
               ss<<n;              
               ss>>num;
               for(j=0;j<num.length()-1;j++){
                   char last=num[num.length()-1];
                   num=num.substr(0,num.length()-1);
                   num=last+num;
                   stringstream ss2(num);
                   int x;
                   ss2>>x;
                   if(x>n&&x<=B){
                     maps[make_pair(n,x)]=true;            
                   }
               }
                             
            }
            cout<<maps.size()<<endl;
                           
    }
    return 0;
}
