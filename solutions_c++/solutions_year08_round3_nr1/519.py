#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>
using namespace std;
int main()
{
        unsigned long long int n;
        cin>>n;
        for(unsigned long long int i=0;i<n;i++)
        {
                unsigned long long int p,k,l,t;
                cin>>p>>k>>l;
                vector<unsigned long long int> v;
                for( unsigned long long int j=0;j<l;j++)
                {
                        cin>>t;
                        v.push_back(t);
                }
                sort(v.begin(),v.end());
                                unsigned long long int h = l/k,ans=0,ne = v.size();
                
                for(unsigned long long int u =0;u<=h;u++)
                {
                        for(unsigned long long int w=0;w<k;w++)
                        {
                                if(u==h && (w+u*k) >= ne ) break; 
                                ans+= (u+1)*v[ne-1 -(w + u*k)];
                        }
                }
                cout<<"Case #"<<i+1<<": "<<ans<<endl;
                
        }        
        return 0;
}
