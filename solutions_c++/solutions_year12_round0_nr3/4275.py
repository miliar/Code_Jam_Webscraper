#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cstring>
#include<sstream>

using namespace std;

int a , b;

int dig1[10]  , dig2[10];

string rotate(string s)
{
    int n = s.size();
    char temp = s[n - 1];
    for(int i=n-1;i>=1;i--)
    {
        s[i] = s[i-1];
    }
    s[0] = temp;
    return s;
}

string toString(int n)
{
    ostringstream os;
    os<<n;
    return os.str();
}

int isRecycle(int n , int m)
{
    if(n == m)return 1;
    string s1 = toString(n);
    string s2= toString(m);

    memset(dig1 , 0 , sizeof(dig1));
    memset(dig2 , 0 , sizeof(dig2));

    int sz1 = s1.size();
    int sz2 = s2.size();

    if(sz1 != sz2)return 0;

    for(int i=0;i<sz1;i++)
        dig1[s1[i] - '0']++;
    for(int i=0;i<sz2;i++)
        dig2[s2[i] - '0']++;

    for(int i=0;i<10;i++)
        if(dig1[i] != dig2[i])return 0;

    for(int i=0;i<sz1;i++)
    {
        s1 = rotate(s1);
        if(s1 == s2)return 1;
    }
    return 0;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int testcase;
    int caseNo = 1;
    scanf("%d",&testcase);
    while(testcase--)
    {
        cin>>a>>b;
        int ans = 0;

        for(int n = a; n <= b;n++)
        {
            for(int m = n+1;m<=b;m++)
            {
                if(isRecycle(n,m))
                {
                    ans ++;
                }
            }
        }
        printf("Case #%d: ",caseNo++);
        cout<<ans<<endl;
    }

    return 0;
}
