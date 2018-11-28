#include <iostream>
#include <queue>
using namespace std;
int main(){
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
            
            unsigned long int r,k;
            short int n;
            queue<unsigned long int> G,rk;
            unsigned long int g;
            
            cin >> r >> k >> n;
            for(int j=0;j<n;j++){
                  cin >> g;
                  G.push(g); 
            }
            unsigned long int s=0;
            for(int j=0;j<r;j++){
                    unsigned long int p=0;
                    unsigned long int now=0;
                    while(now+p<=k && !G.empty()){
                                  p=G.front();
                                  if(now+p<=k){
                                               now+=p;
                                               G.pop();
                                               rk.push(p);
                                               p=0;
                                  }      
                    }
                    while(!rk.empty()){
                                       p=rk.front();
                                       rk.pop();
                                       G.push(p);
                    }
                                      
                    s+=now;
            }
            cout << "Case #" << i+1 << ": " << s << endl;
    }  
	return 0;
}
