#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;
typedef pair<long long, long long> pii;
pii freq[1000];


bool kryt(pii p1, pii p2)
{
     return (p1.second > p2.second);
}


int main()
{
    long long n, k , l, p, s, acc;
    
    cin>>n;
    
    for(int i = 0; i < n; i++)
    {
       cin>>p>>k>>l;
       acc = 0;
       for (int j = 0; j < l; j++)
       {
           cin>>s;
           freq[j] = make_pair(j, s);
       }
       
       sort(freq, freq+l, kryt);
       
       for (int j= 0; j < l; j++)
       {
           acc += (freq[j].second) * (1 + j / k);
           //cout<<freq[j].first<<" "<<freq[j].second<<endl;
       }
       
       
    
        cout<<"Case #"<<i+1<<": "<<acc<<endl;        
    }
    return 0;
}
    
