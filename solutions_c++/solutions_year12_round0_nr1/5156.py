#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cstring>

using namespace std;

char mapping[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int testcase;
    int caseNo = 1;
    scanf("%d\n",&testcase);
    while(testcase--)
    {
        string s;
        getline(cin , s);
        int sz = s.size();
        string ans = "";
        for(int i=0;i<sz;i++)
        {
            if(s[i] == ' ')
                ans += " ";
            else
            ans += mapping[s[i] - 'a'];
        }
        printf("Case #%d: ",caseNo++);
        cout<<ans<<endl;
    }


    return 0;
}
