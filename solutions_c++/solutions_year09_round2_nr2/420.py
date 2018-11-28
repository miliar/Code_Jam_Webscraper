#include <iostream>
#include <vector>
#include <algorithm>

#define all(v) (v).begin(), (v).end()

using namespace std;

bool mayor(string a, string b)
{
    return a > b;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin>>T;
    
    for(int nCaso = 1; nCaso <= T; nCaso++)
    {
        string s;
        cin>>s;
        
        if(next_permutation(all(s))) cout<<"Case #"<<nCaso<<": "<<s<<endl;
        else
        {
            string t = s;
            sort(all(t));
            string tmp = "";
            int cnt = 0;
            for(int i=0; i<t.size(); i++)
            {
                if(t[i]=='0') cnt++;
                else tmp += t[i];
            }
            cnt++;
            string aux = string(cnt, '0');
            
            cout<<"Case #"<<nCaso<<": "<<tmp[0] + aux + tmp.substr(1)<<endl;
        }
    }
    return 0;
}
