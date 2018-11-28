#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<int> v;
int main()
{
    ifstream cin ("i.in");
    ofstream cout ("o.out");
    int t, n, L, H, i, j, k;
    bool z;
    cin>>t;
    for (i=0;i<t;++i)
    {
        cin>>n>>L>>H;
        v.clear();
        for (j=0;j<n;++j)
        {
            cin>>k;
            v.push_back(k);
        }
        cout<<"Case #"<<(i+1)<<": ";
        for (k=L;k<=H;++k)
        {
            z=1;
            for (j=0;j<n;++j)
            {
                if (k%v[j]!=0 && v[j]%k!=0)
                {
                    z=0;
                    break;
                }
            }
            if (z)
            {
                cout<<k<<endl;
                break;
            }
        }
        if (!(z))
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
