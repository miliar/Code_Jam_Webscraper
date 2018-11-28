/*
Try Try & Try until you solve the problem...
Nothing is impossible for the problem solvers... :)
*/
/*

*/
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <numeric>

#include <cmath>
#include <cstdio>

#define IP(n) for(i=0;i<n;i++)
#define JP(n) for(j=0;j<n;j++)
#define KP(n) for(k=0;k<n;k++)

#define vi vector<int>
#define vi2 vector<vector<int>>
#define vs vector<string>

#define pb push_back
#define TC int t,check=1;cin>>t;while(check<=t)
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)


using namespace std;

string so="yhesocvxduiglbkrztnwjpfmaq ";
string si="abcdefghijklmnopqrstuvwxyz ";

char place(char ch)
{
    for(int i=0;i<27;i++)
    if(si[i]==ch) return so[i];

    return '.';
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    int t,check=1;
    cin>>t;
    char grbg[5];
    gets(grbg);

    while(t--)
    {
        string s;
        getline(cin,s);
        printf("Case #%d: ",check++);
        for(int i=0;i<s.size();i++)
        {
            cout<<place(s[i]);
        }
        cout<<endl;

    }

    return 0;
}
