#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<string> v_1;
vector<string> v_2;
int main()
{
    ifstream cin("a.txt");
    ofstream cout("b.txt");
    int t, c, d, n, i, j, k, x;
    string S, res;
    cin>>t;
    bool z;
    for (k=0;k<t;++k)
    {
        cin>>c;
        v_1.clear();
        v_1.reserve(c);
        for (j=0;j<c;++j)
        {
            cin>>S;
            v_1.push_back(S);
        }
        cin>>d;
        v_2.clear();
        v_2.reserve(d);
        for (j=0;j<d;++j)
        {
            cin>>S;
            v_2.push_back(S);
        }
        cin>>n;
        cin>>S;
        res=S[0];
        for (i=1;i<n;++i)
        {
            z=0;
            for (j=0;j<c;++j)
            {
                if ((v_1[j][0]==S[i] && v_1[j][1]==res[res.length()-1]) || (v_1[j][0]==res[res.length()-1] && v_1[j][1]==S[i]))
                {
                    res[res.length()-1]=v_1[j][2];
                    z=1;
                    break;
                }
            }
            if (z)
            {
                continue;
            }
            for (j=0;j<d;++j)
            {
                if (v_2[j][0]==S[i])
                {
                    for (x=0;x<res.length();++x)
                    {
                        if (res[x]==v_2[j][1])
                        {
                            res="";
                            ++i;
                            z=1;
                            break;
                        }
                    }
                    if (z)
                    {
                        break;
                    }
                }
                if (v_2[j][1]==S[i])
                {
                    for (x=0;x<res.length();++x)
                    {
                        if (res[x]==v_2[j][0])
                        {
                            res="";
                            ++i;
                            z=1;
                            break;
                        }
                        if (z)
                        {
                            break;
                        }
                    }
                }
            }
            if (i!=n)
            {
                res+=S[i];
            }
        }
        cout<<"Case #"<<k+1<<": [";
        for (j=0;j<res.length();++j)
        {
            cout<<res[j];
            if (j!=(res.length()-1))
            {
                cout<<", ";
            }
        }
        cout<<"]"<<endl;
    }
    return 0;
}
