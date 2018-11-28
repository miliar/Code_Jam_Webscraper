#include <iostream>
#include <vector>
using namespace std;

int solve(int x)
{
    int p;
    cin>>p;
    int r;
    cin>>r;
    vector <int> rel;
    for(int i=0;i<r;i++)
     {
            int t;
            cin>>t;
            rel.push_back(t);
     }
    int min=999999,t=0;
    do
    {
    bool b[10000];
    for(int i=0;i<10000;i++)
     b[i]=0;
    for(int i=0;i<rel.size();i++)
    {
            b[rel[i]]=1;
            //cout<<"!"<<rel[i]<<endl;
            for(int j=rel[i]-1;j>=1&&b[j]==0;j--)
             t++;
            //cout<<"!"<<rel[i]<<" "<<t<<endl;
            for(int j=rel[i]+1;j<=p&&b[j]==0;j++)
             t++;
            
    }
    //cout<<"!"<<t<<endl;
    if(min>t)min=t;
    t=0;
    }
    while(next_permutation(rel.begin(),rel.end()) );
    cout<<"Case #"<<x<<": "<<min<<endl;   
}
            
int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
     solve(i+1);
    return 0;
}
