#include<iostream>
using namespace std;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int cc;
    int i,j,k;
    int n,l,h;
    int a[110], answer;
    bool found;
    cin>>t;
    for (cc = 1; cc <= t; cc++)
    {
        cin>>n>>l>>h;
        for (i = 0; i<n; i++)
        {
            cin>>a[i];
        }
        for(answer = l; answer <= h; answer ++)
        {
            found = true;
            for (i = 0; i<n; i++)
            {
                if (answer % a[i] == 0 || a[i] % answer == 0)
                   continue;
                    else found = false;
            }
            if (found)
              break;
        }
        if (found)
        {
           cout<<"Case #"<<cc<<": "<<answer<<endl;
        }
        else cout<<"Case #"<<cc<<": NO"<<endl;
    }
    return 0;
}
