#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <cstring>

using namespace std;

long long dists[1000010];
long long aux1[1000010];
long long aux2[1000010];


int main()
{
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
        long long l,t,n,c;
        cin>>l>>t>>n>>c;
        memset(aux1,0,sizeof (aux1));
        memset(dists,0,sizeof (dists));
        memset(aux2,0,sizeof (aux2));            
            
        long long resp = 0;
        
        for(int i = 0; i < c; i++) cin>>aux1[i];

        aux2[0] = 0;
        for(int i = 1, j = 0; i <= n; i++, j++)
        {
            dists[i] = aux1[j%c];
            aux2[i] = dists[i] + aux2[i-1];
            resp += dists[i];
        }
        resp *= 2;
        int id = lower_bound(aux2,aux2+n,t/2) - aux2;
        vector<long long> aux3;
        aux3.push_back(t/2-aux2[id]);
        for(int i = id+1; i <= n; i++) {
            aux3.push_back(-dists[i]);
        }
        sort(aux3.begin(),aux3.end());
        for(int i = 0, j = 0; i < l && j < aux3.size(); i++, j++)
        {
            resp += aux3[j];
        }

       	cout<<"Case #"<<ii<<": "<<resp<<endl; 
        
        
    }
    
    return 0;
}
