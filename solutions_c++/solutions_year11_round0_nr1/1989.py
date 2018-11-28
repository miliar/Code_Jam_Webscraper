#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>

using namespace std;

int n,na,nb,ta,tb;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cs,k=0,i;
    cin>>cs;
    while (cs--){
          na=nb=1;
          ta=tb=0;
          int tmp=0;
          cin>>n;
          for (i=1;i<=n;i++){
              int t;
              char ch;
              cin>>ch>>t;
              if (ch=='O'){ 
                           if (tmp==2) ta=max(ta+abs(na-t),tb)+1;
                              else ta+=abs(na-t)+1;
                           na=t;
                           tmp=1; }
                 else { 
                       if (tmp==1) tb=max(ta,tb+abs(nb-t))+1;
                          else tb+=abs(nb-t)+1;
                       nb=t;
                       tmp=2; }
              //cout<<ta<<" "<<tb<<endl;
              }
          k++;
          printf("Case #%d: %d\n",k,max(ta,tb));
          }
}
          
