#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<vector<int> > vv;
vector<int> v;
vector<long double> OWP(110);
vector<long double> res(110);
int main()
{
    ifstream cin("i.in");
    ofstream cout("o.out");
    int t, n, i, j, k, f, x;
    long double a, b, q;
    char c;
    cin>>t;
    for (i=0;i<t;++i)
    {
        cin>>n;
        for (j=0;j<n;++j)
        {
            res[j]=0;
            OWP[j]=0;
        }
        vv.clear();
        for (j=0;j<n;++j)
        {
            v.clear();
            for (k=0;k<n;++k)
            {
                cin>>c;
                if (c=='.')
                {
                    v.push_back(0);
                }
                else if (c=='1')
                {
                    v.push_back(1);
                }
                else
                {
                    v.push_back(-1);
                }
            }
            vv.push_back(v);
        }
        for (j=0;j<n;++j)
        {
            a=0;
            b=0;
            for (k=0;k<n;++k)
            {
                if (vv[j][k]!=0)
                {
                    ++b;
                    if (vv[j][k]==1)
                    {
                        ++a;
                    }
                }
            }
            res[j]+=(0.25*(a/b));
        }
        for (j=0;j<n;++j)
        {
            q=0;
            x=0;
            for (k=0;k<n;++k)
            {
                a=0;
                b=0;
                if (k==j || vv[k][j]==0)
                {
                    continue;
                }
                ++x;
                for (f=0;f<n;++f)
                {
                    if (f==j)
                    {
                        continue;
                    }
                    if (vv[k][f]!=0)
                    {
                        ++b;
                        if (vv[k][f]==1)
                        {
                            ++a;
                        }
                    }
                }
                q+=(a/b);
            }
            q/=x;
            res[j]+=(q*0.5);
            OWP[j]=q;
        }
        for (j=0;j<n;++j)
        {
            a=0;
            b=0;
            x=0;
            for (k=0;k<n;++k)
            {
                if (k!=j && vv[k][j]!=0)
                {
                    a+=OWP[k];
                    ++x;
                }
            }
            a/=x;
            res[j]+=(0.25*a);
        }
        cout<<"Case #"<<(i+1)<<":"<<endl;
        for (j=0;j<n;++j)
        {
            cout.precision(25);
            cout<<res[j]<<endl;
        }
    }
    return 0;
}
