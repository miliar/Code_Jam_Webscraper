#include <iostream>
#include <vector>
#include <set>
#include <string>
using namespace std;
int main()
{
    int n;
    cin >> n;
    for(int z=1;z<=n;z++)
    {
        int s, q;
        string xx;
        cin >> s;
        set<string> en;
        getline(cin,xx);
        for(int i=0;i<s;i++) {getline(cin,xx); en.insert(xx);}
        cin >> q;
        vector<string> qu(q,"");
        getline(cin,xx);
        for(int i=0;i<q;i++) getline(cin,qu[i]);
        set<string> u;
        int res=0;
        u=en;
        for(int i=0;i<q;i++)
        {
            if(u.empty() && i) {u=en; u.erase(qu[i-1]);}
            else u=en;
            while(i<q && u.size())
            {
                u.erase(qu[i]);
                if(u.size()) i++;
            }
            if(u.empty()) res++;
        }
        cout << "Case #" << z << ": " << res << endl;
    }
}
