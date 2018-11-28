#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <fstream>
using namespace std;

typedef unsigned long long int ull;
typedef long double ld;

int main()
{
        //freopen("A-small-practice.in","r",stdin);
    //freopen("A-small-practice.out","w",stdout);
    freopen("ag.in","r",stdin);
    freopen("ag.out","w",stdout);

    int t;
    cin>>t;int cn=0;
    while(t--)
    {cn++;
        int n;
        cin>>n;
        vector<string>mat;
        for(int x=0;x<n;x++)
        {
            string str;cin>>str;//cout<<"str="<<str<<"\n";
            mat.push_back(str);
        }
        vector<double>wp;
        vector<double>owp;
        vector<double>oowp;

        for(int x=0;x<n;x++)
        {double w=0.0,l=0.0;
            for(int y=0;y<n;y++)
            {
                if(mat[x][y]=='1')w++;else if(mat[x][y]=='0')l++;
                //cout<<"in here ="<<mat[x][y]<<""<<"w="<<w<<" l="<<l<<"\n";
            }
            double tt=w/(w+l);
            wp.push_back(tt);
            //cout<<"wp[x]="<<wp[x]<<"\n";
        }
        for(int x=0;x<n;x++)
        {double sum=0;int cnt=0;
            for(int y=0;y<n;y++)
            {if(y==x||mat[x][y]=='.')continue;double w=0,l=0;cnt++;
                for(int z=0;z<n;z++)
                {
                    if(z==x)continue;
                    if(mat[y][z]=='1')w++;
                    else if(mat[y][z]=='0')l++;
                }
                sum+=(w/(w+l));
            }
            owp.push_back(sum/cnt);
        }
        for(int x=0;x<n;x++)
        {double sum=0;int cnt=0;
            for(int y=0;y<n;y++)
            {
                if(y==x||mat[x][y]=='.')continue;
                sum+=owp[y];cnt++;
            }
            oowp.push_back(sum/cnt);
        } cout<<"Case #"<<cn<<":\n";
        for(int x=0;x<n;x++)
       cout<<.25*wp[x]+.5*owp[x]+.25*oowp[x]<<"\n";
    }
    return 0;
}
