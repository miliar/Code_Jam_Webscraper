#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

long long inf=1<<30;

int main()
{
    int t, n;
    cin>>t;
    
    for(int ii=1; ii<=t; ii++)
    {
        cin>>n;
        long long resp=inf,si=0,aux=0;
        
	for(int i=0; i<n; i++)
	{
            long long act;
	    cin>>act;
            si^=act;
	    aux+=act;
            resp=min(resp,act);
        }
        
        if (si== 0) cout<<"Case #"<<ii<<": "<<aux-resp<<endl;  
        else cout<<"Case #"<<ii<<": NO\n";
    }
    return 0;
}