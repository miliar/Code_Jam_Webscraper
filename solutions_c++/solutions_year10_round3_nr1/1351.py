#include<iostream>
#include<cstdio>
#include<cmath>
#include<cctype>
#include<vector>
#include<map>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w+",stdout);
    int t;
    cin>>t;
    for(int i= 1;i<=t;i++){
            int n,x,y;
            int count = 0;
            vector<int> a,b;
            cin>>n;
            for(int j= 0;j<n;j++){
                    cin>>x>>y;
                    a.push_back(x);
                    b.push_back(y);
            }
            for(int k= 0;k<n-1;k++){
                   for(int j = k+1;j<n;j++){
                         if((a[k]>a[j] and b[k]<b[j] )|| (a[k]<a[j] && b[k]>b[j])){
                                       count++;
                         }
                   }
            }
            cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}
            
