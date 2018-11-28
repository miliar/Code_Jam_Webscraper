#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    cin>>t;
    for(int i = 0; i < t; i++)
    {
        int ans = 0;
        int n,s,av;
        cin>>n>>s>>av;
        for(int j = 0; j < n; j++)
        {
            int temp,q;
            cin>>temp;
            q = temp%3;
            if(temp / 3 >= av) {ans++; continue;}
            if(q == 0)  if(temp / 3 + 1 >= av && s && temp / 3 + 1 <= temp) {ans++; s--; continue;}
            if(q == 1)  if(temp / 3 + 1 >= av && temp / 3 + 1 <= temp) {ans++; continue;}
            if(q == 2)  if(temp / 3 + 1 >= av && temp / 3 + 1 <= temp) {ans++; continue;}
            else if(q == 2 && s)
                if(temp/3 + 2 >= av && temp / 3 + 2 <= temp) {ans++; s--; continue;}
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
return 0;
}
