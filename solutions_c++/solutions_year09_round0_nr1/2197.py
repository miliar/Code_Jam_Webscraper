#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int l,d,n;
bool used[510][32];
string s[5010];

int main()
{
    cin >> l >> d >> n;
    for(int i=0;i<d;i++) cin >> s[i];
    
    for(int i=1;i<=n;i++)
    {
        memset(used,0,sizeof(used));
        
        cout << "Case #" << i << ": ";
        string tmp;
        cin >> tmp;
        int ind=-1;
        bool fl=false;
        for(int j=0;j<tmp.size();j++)
        {
            if(tmp[j]>='a' && tmp[j]<='z')
            {
                if(!fl) ind++;
                used[ind][ tmp[j]-'a' ] = 1;
            }
            else if(tmp[j]=='(') { fl=true; ind++; }
            else fl=false;
        }
        
        int cnt=0;
        for(int j=0;j<d;j++)
        {
            bool issol=true;
            for(int k=0;k<l;k++) if(!used[k][ s[j][k]-'a' ]) { issol=false; break; }
            if(issol) cnt++;
        }
        cout << cnt << endl;
    }
    
    return 0;
}
