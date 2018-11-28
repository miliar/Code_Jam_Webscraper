#include <iostream>
#include <set>
#include <string>
using namespace std;

string updir(string s)
{
    string ans;
    int i, j;
    for(j=s.length()-1; j>=0; j--)
        if(s[j]=='/')
            break;
    for(i=0; i<j; i++)
        ans += s[i];
    if(ans.length()==0)
        ans += '/';
    return ans;
}

int main()
{
    int T, t;
    int N, M;
    set<string> exist;
    int ans;
    int i;
    int before, after;
    string next;

    cin>>T;
    for(t=1; t<=T; t++)
    {
        exist.clear();
        exist.insert("/");
        cin>>N>>M;
        for(i=1; i<=N; i++)
        {
            cin>>next;
            while(next!="/")
            {
                exist.insert(next);
                next = updir(next);
            }
        }
        before = exist.size();
        for(i=1; i<=M; i++)
        {
            cin>>next;
            while(next!="/")
            {
                exist.insert(next);
                next = updir(next);
            }
        }
        after = exist.size();
        ans = after-before;
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}

