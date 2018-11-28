#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <stack>
#include<cctype>
#include<map>
#include<set>
#include<stdio.h>
using namespace std;

#define ABS(x) ((x)<0?-(x):x)
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
char org[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ' };
char mod[] = { 'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x',
's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q', ' ' };
int main()
{
    freopen("A-small-attempt1.in", "rt", stdin);
    freopen("out.out", "wt", stdout);
    int t;
    string g = "",out = "";
    cin>>t;
    getline(cin,g);
    for(int i=0;i<t;i++)
    {
        out = "";
        getline(cin,g);
        for(int j=0;j<g.size();j++)
        {
            for(int k=0;k<27;k++)
            {
                if(g[j] == mod[k])
                {
                    out += org[k];
                    break;
                }

            }
        }
        cout<<"Case #"<<i+1<<": "<<out<<endl;

    }
	return 0;
}
