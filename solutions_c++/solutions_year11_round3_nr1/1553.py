#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int r;
        cin>>r;
        int c;
        cin>>c;
        cout<<"Case #"<<i+1<<":"<<endl;
        string stats[r];
       
        for(int j=0;j<r;j++)
        {
                cin>>stats[j];
        }
       
        for(int j=0;j<r-1;j++)
        {
                for(int k=0;k<c-1;k++)
                {
                         if((stats[j][k]=='#')&&(stats[j][k+1]=='#')&&(stats[j+1][k]=='#')&&(stats[j+1][k+1]=='#'))
                         {
                          stats[j][k] = '/';
                          stats[j][k+1] = '\\';
                          stats[j+1][k] = '\\';
                          stats[j+1][k+1] = '/';
                         }
                }
        }
        int count=0;
        for(int j=0;j<r;j++)
        {
                for(int k=0;k<c;k++)
                {
                         if(stats[j][k]=='#')
                         {
                         count++;
                         break;
                         }     
                }
                if(count>0) break;
        }
       
        if(count>0) {cout<<"Impossible"<<endl;}
        else{
                for(int j=0;j<r;j++)
                {
                         cout<<stats[j]<<endl;
                }
        }
        
    }
    return 0;
}
