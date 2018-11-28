#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

#include <set>
#include <map>

#include <queue>
#include <deque>
#include <stack>
#include <list>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#define all(c) (c).begin(),(c).end()

using namespace std;

int main(){
    freopen("A2.in","r",stdin);
    freopen("A2.out","w",stdout);
    int n;
    scanf("%d\n",&n);
    for(int i=0; i<n; i++){
        unsigned long long sum=0;
        int p,k,l;
        scanf("%d%d%d\n",&p,&k,&l);
        vector<int> letras,used(l,0);
        for(int j=0; j<l; j++){
            int dato; (j!=l-1)?scanf("%d",&dato):scanf("%d\n",&dato);
            letras.push_back(dato);    
        }
        sort(all(letras)); reverse(all(letras));                
        for(int j=0; j<l; j++){
            int pos=j,par=1;
            if(used[pos]==0)
            while(pos<l && par<=p){
                if(used[pos]==0){sum=sum+letras[pos]*par; par++;used[pos]=1;
                pos+=k; }
            }      
        }
        cout<<"Case #"<<(i+1)<<": "<<sum;
        if(i!=n-1)cout<<endl;           
    }  
return 0;
}
