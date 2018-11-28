#include <iostream>
#include <cstdio>
#include <list>
#include <vector>
using namespace std;
list<int> adj;
int main(){
    int k,p,q,l;
    cin >> k;
    for(int i=0;i<k;i++){
            cin >> p >> q >> l;
            adj.clear();
            for(int j=0;j<l;j++){
                    int u;
                    cin >> u;
                    adj.push_back(u);        
            }
            adj.sort();
            int layer = 1,num=1;
            int sum = 0;
            while(!adj.empty()){
                                if(num%(q+1) == 0){ 
                                               num = 1; 
                                               layer++;
                                }
                                int u;
                                u = adj.back();
                                adj.pop_back();
                                //cout << u << " " << layer << " " << endl;;
                                sum += u*layer;
                                
                                
                                num++;
                                                                
            }
            //cout << endl;
            cout << "Case #" << i+1 << ": " << sum << endl;        
    }
    return 0;    
}
