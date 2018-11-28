#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
//#include<conio.h>
using namespace std;
vector<int> v1,v2;
int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");
    int t,n,i,temp,ans,cas=1;
    fin>>t;
    cout<<t;
    while(t--)
    {
              v1.clear(); v2.clear();
           fin>>n;   
           v1.resize(n); v2.resize(n);
           for(i=0;i<n;i++)
             fin>>v1[i];
             for(i=0;i<n;i++)
             fin>>v2[i];
           sort(v1.begin(), v1.end());
           sort(v2.begin(), v2.end());
           ans=0;
           for(i=v1.size()-1;i>=0;i--)
           {
             ans+=v1[i]*v2[v2.size()-1-i];
           }
           fout<<"Case #"<<cas<<": "<<ans<<endl;
           cas++;
           //cout<<ans;
    }
    //getch();
    return 0;
}
