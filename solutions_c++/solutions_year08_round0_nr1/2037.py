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

using namespace std;
vector<string> buscadores,queries;

int cambios(int ind){
    if(ind!=queries.size()){
        int mmax=0, mi=ind;
        for(int i=0; i<buscadores.size();i++){
            int cont=0,j;
            for(j= ind; j<queries.size(); ++j)
            {   if(queries[j]==buscadores[i])break;
                else{ cont++; }
            }
            if(cont>mmax){ mmax=cont; mi=j; //cout<<cont<<endl;
            }
        }
            return 1+cambios(mi);
    }
    else
        return 0;    
}

int main(){
    freopen("A1.in", "r",stdin);
    freopen("Alarge.out","w",stdout);   
    int n,se,qq,sw;
    scanf("%d\n",&n);
    for(int i=0; i<n; i++){
        se=0; qq=0; sw=0;
        scanf("%d\n",&se);   
        buscadores.clear(); queries.clear();
        for(int j=0; j<se; j++){
            string dato; getline(cin,dato,'\n');
            buscadores.push_back(dato);      
        }        
        scanf("%d\n",&qq);        
        for(int j=0; j<qq; j++){
            string linea; getline(cin,linea,'\n');
            queries.push_back(linea);      
        }                
        (qq!=0)?sw=cambios(0):sw=0;
        if(sw!=0)sw--;
        cout<<"Case #"<<(i+1)<<": "<<sw;        
        if(i!=n-1)cout<<endl;
               
    }
return 0;
}
