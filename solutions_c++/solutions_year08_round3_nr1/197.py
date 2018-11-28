#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#define MAXI(a,b) ((a>b)?(a):(b))
#define MINI(a,b) ((a<b)?(a):(b))

bool find(vector<long long> vx,vector<long long> vy,long long xc,long long yc)
    {
    int z=vx.size();
    for(int i=0;i<z;i++)
        {
        if(vx[i]==xc && vy[i]==yc ) return true;
        }
    return false;    
    }

int main()
{
long long   N, P , K , L , temp;
vector<long long> v;

cin>>N;
for(int i=1;i<=N;i++)
    {
    cin>>P>>K>>L;
    v.clear();
    
    for(int j=0;j<L;j++)
            {
            cin>>temp;
            if(temp>0) v.push_back(temp);
            }               
    sort(v.begin(),v.end());
    
    int z=v.size();
    int pos=z-1;
    long long min=0;
    int wt=1;
    
    while( pos>=0)
        {
        for(int j=0;(j<K)&&(pos>=0);j++,pos--)
                {
                min+=wt*v[pos]; 
                }
        wt++;
        }
    cout<<"Case #"<<i<<": "<<min<<endl;
    }
    
return 0;
}
