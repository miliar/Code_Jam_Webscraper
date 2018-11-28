#include <iostream>
#include <vector>
#include <deque>

#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

typedef long long ll;

typedef std::pair<ll,ll> mypair;


int main()
{
    ll T, N, D;
    
    cin>>T;
    
     
    for(int i=0; i<T; ++i)
    {
        vector<mypair> vines;
        
        cin>>N;
        
        for (int j=0; j<N; ++j) {
            
            mypair v;
            
            cin>>v.first>>v.second;
            
            vines.push_back(v);
        }
        
        cin>>D;
        
        //ll reach = vines[0].first * 2;
        //ll pos = 0;
    
        //
        
        bool p = false;
        //int j=0;
        /*
        while(j<N) {
            
            cout<<"vine: "<<j<<" reach: "<<reach<<endl;
            
            if(reach >= D)
            {
                p = true;
                break;
            }
            
            int k = j+1;
            
            int tentative_j = -1;
            ll tentative_reach = reach;
            
            while(k<N && vines[k].first <= reach)
            {
                ll vine_reach = vines[k].first + min(vines[k].second, vines[k].first - vines[j].first);
                
                cout<<vine_reach<<endl;
                
                if(vine_reach > tentative_reach)
                {
                    tentative_reach = vine_reach;
                    tentative_j = k;
                
                }
            
                ++k;
            }
            
            //cout<<tentative_reach<<endl;
            
            if(tentative_reach > reach)
            {
                j = tentative_j;
                reach = tentative_reach;
            }
            else
                break;
            
            //pos = vines[j];
        }
        */
        
        vector<ll> reach (N);
        reach[0] = vines[0].first * 2;
        
        
        if(reach[0] >= D)
        {p=true; goto skip;}
        
        for(int j=1; j<N; ++j)
        {
            for(int k=0; k<j; ++k)
                if(reach[k] >= vines[j].first)
                {
                    ll vine_reach = vines[j].first + min(vines[j].second, vines[j].first - vines[k].first);
                    
                    //cout<<vine_reach<<endl;
                    
                    if(vine_reach > reach[j])
                    {
                        reach[j] = vine_reach;
                        //tentative_j = k;
                        
                        if(vine_reach >= D)
                        {p=true; goto skip;}
                    }
                    

                
                }
        
        }
        
    skip:
        if(p)
            cout<<"Case #"<<i+1<<": "<<"YES"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
        
    }
	return 0;
}
