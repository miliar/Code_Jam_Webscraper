#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;

bool xor_sum(vector<int>& v,int p)
{
    int v1=v[0];
    int v2=v[p];
    for (int i=1;i<p;i++)
    {
        v1 = v1^v[i];
    }
    for (int i=p+1;i<v.size();i++)
    {
        v2 = v2^v[i];
    }
    if (v1==v2)
    return true;
    else
    return false;
}
        

int main()
{
    int cases;
    cin>>cases;
    
    for (int i=1;i<=cases;i++)
    {
        int N;
        cin>>N;
        vector<int> v(N);
        for (int j=0;j<N;j++)
        cin>>v[j];
        sort(v.begin(),v.end());
        
        int pat = v[0];
        int sean = 0;
        int p=1;
        
        while (!xor_sum(v,p) && p<v.size())
            p++;
        
        for (int ii=p;ii<v.size();ii++)
            sean += v[ii];
        
        if (p==v.size())
            cout<<"Case #"<<i<<": NO"<<endl;
        else
            cout<<"Case #"<<i<<": "<<sean<<endl;
    }
        
        return 0;
}
        
        
            
