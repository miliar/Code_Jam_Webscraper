#include <iostream>
#include <string>
#include <queue>
using namespace std;
int main (){
    freopen("C-small-attempt0.in","rt",stdin);
    freopen("Cout.in","w",stdout);
    int c;
    cin>>c;
    int m=1;
    while(c--){
               int r,k,n,l;
               cin>>r>>k>>n;
               queue<int>q;
               int co=0;
               for(int i=0;i<n;i++){cin>>l; q.push(l);}
               queue<int>A=q;
               while(r--){
                          int count=0,c=0;  
                          queue<int>A=q;
                          while(count<k && c<n ){
                                        c++;
                                         int t=q.front();
                                         count+=t;
                                         q.pop();
                                         q.push(t);
                                         if(q.front()+count>k)break;
                          }
                          co+=count;
               }           
               cout<<"Case #"<<m<<": "<<co<<endl;
               m++;
  }
  return 0;
}
