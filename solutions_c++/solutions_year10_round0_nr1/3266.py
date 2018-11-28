//Bismillahir Rahmanir Rahim

#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;



int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outputfile.out","w",stdout);
    vector<int>vec;
    int n,k,j,m;
    int i,kas;
    cin>>kas;

    for(i=0;i<kas;i++)
    {
        cin>>n>>k;
        cout<<"Case #"<<i+1<<": ";
        vec.clear();

        while(k>0)
        {
            //cout<<k%2<<endl;
            int t=k%2;
            vec.push_back(t);
            k/=2;
        }
        int flag=1;
        for(k=0;k<vec.size();k++)
        {
            if(vec[k]==0)
            flag=0;
            if(flag==1)
            {
                vec[k]=1;
            }
            else
            vec[k]=0;

        }


//        reverse(vec.begin(),vec.end());
        if(vec.size()<n)
        cout<<"OFF"<<endl;
        else if(vec[n-1]==0)
        {
            cout<<"OFF"<<endl;
        }
        else
        cout<<"ON"<<endl;
    }
    return 0;
}
