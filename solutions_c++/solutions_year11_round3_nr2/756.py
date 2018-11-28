#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool customsort(pair<int, int> a, pair<int, int> b)
{
    if(a.second<=b.second)
        return false;
    else return true;
}

int main()
{

    int T;
    cin>>T;
    for(int test=0;test<T;test++)
    {
        cout<<"Case #"<<test+1<<": ";
        
        long long L, t, N, C;
        cin>>L>>t>>N>>C;
        vector<int> v;
        for(int i=0;i<C;i++)
        {
            int x;
            cin>>x;
            v.push_back(x);
        }
        vector<int> dist(N, 0);
        for(int i=0;i<N;i++)
        {
            int k=0;
            int s1, s2;
            do {
                
                s1 = (k*C)+i;
                s2 = (k*C)+i+1;
                if(s2<=N && dist[s2-1] == 0)
                {
                    dist[s2-1] = v[i];
                    //cout<<i<<" "<<k<<" "<<s1<<" "<<s2<<" "<<v[i]<<endl;
                }
                k++;

            }while(s2<N);
        }
        /*
        for(int i=0;i<N;i++)
        {
            cout<<dist[i]<<" ";

        }
        
        cout<<endl;
        */
        double dt = 0.5*t;
        long long d = 0;
        int i=0;
        for(i;d<dt&&i<N;i++)
        {
            d+=dist[i];
        }
        //cout<<i<<endl;
        vector<pair<int, int> > dist2;
        dist2.push_back(make_pair(i, d-dt));
        i++;
        for(i;i<=N;i++)
        {
            dist2.push_back(make_pair(i, dist[i-1]));
        }

        sort(dist2.begin(), dist2.end(), customsort);
        /*
        for(int k=0;k<dist2.size();k++)
        {
            cout<<dist2[k].first<<" "<<dist2[k].second<<", ";
        }
        cout<<endl;
        */

        vector<int> haveT(N, 0);
        for(int k=0;k<L;k++)
        {
           haveT[dist2[k].first-1] = 1;
        }
        /*
        for(int i=0;i<N;i++)
        {
            cout<<haveT[i]<<" ";
        }
        cout<<endl;
        */

        double total = 0;
        for(int i=1;i<=N;i++)
        {
            
            //cout<<dist[i-1]<<" ";
            if(haveT[i-1]==0)
            {
                total += (double)dist[i-1]/0.5;
            }
            else if(haveT[i-1]==1)
            {
                if(total>=t)
                {
                    total += (double)dist[i-1];
                }
                else
                {
                    double less = (t-total)*0.5;
                    total += double(less)/0.5;
                    double good = dist[i-1]-less;
                    total += double(good);
             //       cout<<"less: "<<less<<" good: "<<good<<endl;
                }
            }
            //cout<<total<<" ";
        }

        cout<<(long long)total;
        cout<<endl;
    }

    return 0;
}
