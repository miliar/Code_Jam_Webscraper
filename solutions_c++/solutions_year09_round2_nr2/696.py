#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    freopen("d://in.txt","r",stdin);
    freopen("d://out.txt","w",stdout);
    int n,cas;
    string tmp;
    
    cin>>n;
    for (cas=1;cas<=n;cas++)
    {
        cin>>tmp;
        cout<<"Case #"<<cas<<": ";
        if (next_permutation(tmp.begin(),tmp.end()))
        {
            cout<<tmp<<endl;
        }
        else
        {
            tmp='0'+tmp;
            sort(tmp.begin(),tmp.end());
            int i=0;
            while (tmp[i]=='0') i++;
            while (i!=0)
            {
                char ch=tmp[i];
                tmp[i]=tmp[i-1];
                tmp[i-1]=ch;
                i--;
            }
            cout<<tmp<<endl;
        }
    }
    return 0;
}
