#include <iostream>
#include <string>
using namespace std;

int main()
{
    int l,d,n;
    bool mask[15][26];
    int dic[5000][15];

    cin >> l >> d >> n;
    string str;
    getline(cin,str);
    
    for (int i = 0; i<d; ++i)
    {
        getline(cin,str);
        for (int j = 0; j<str.length(); ++j)
            dic[i][j] = str[j]-'a';
    }
    
    for (int i = 0; i<n; ++i)
    {
        memset(mask,0,sizeof(mask));
        getline(cin,str);
        int t = -1;
        for (int j = 0; j<l; ++j)
            if (str[++t] == '(')
                while (str[++t]!=')')
                    mask[j][str[t]-'a'] = true;
            else mask[j][str[t]-'a'] = true;
        int ans = 0;
        // for (int j=0; j<l; ++j){
        //     for (int k =0; k<26; ++k)
        //         cout<<(int)mask[j][k];
        //     cout<<endl;
        // }
        
        for (int j = 0; j<d; ++j)
        {
            bool q = true;
            for (int k=0; k<l; ++k)
                if (!mask[k][dic[j][k]])
                {
                    q = false;
                    break;
                }
            if (q) ++ans;
        }

        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
}

