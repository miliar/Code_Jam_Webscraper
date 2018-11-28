#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

int sound[100005];
int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,l,h;
    int i;
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        cout<<"Case #"<<cas++<<": ";
        cin>>n>>l>>h;
        for(i =0;i<n;i++)
            cin>>sound[i];
        for(i =l;i<=h;i++)
        {
            //cout<<i<<endl;
            bool flag = true;
            for(int j =0;j<n;j++)
            {
                if(sound[j]%i!=0 && i%sound[j]!=0)
                {
                    flag = false;
                    break;
                }
            }
            if(flag)
                break;
        }
        if(i>h)
        {
            cout<<"NO"<<endl;
        }
        else
        {
            cout<<i<<endl;
        }
    }
    return 0;
}
