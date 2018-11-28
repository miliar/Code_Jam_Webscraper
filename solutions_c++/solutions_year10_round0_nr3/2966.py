#include<iostream>
#include<queue>
using namespace std;

int main(){
    int t,r,k,n,y,tmp;
    cin>>t;
    for(int tn=1;tn<=t;tn++){
               cin>>r>>k>>n;
               queue<int> g,q;
               for(int i=0;i<n;i++){
                  cin>>tmp;
                  g.push(tmp);
               }
               y=0;
               while(r>0){
                 int sum=0;
                 while(!g.empty() && sum+g.front()<=k){
                    sum+=g.front();
                    q.push(g.front());
                    g.pop();         
                 }
                 while(!q.empty()){
                    g.push(q.front());        
                    q.pop();
                 }
                 y+=sum;
                 r--;
               }
               cout<<"Case #"<<tn<<": "<<y<<endl;
    }
    //system("PAUSE");
    return 0;
}
