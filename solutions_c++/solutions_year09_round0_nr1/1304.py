#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(void)
{
    int l,d,n;
    string s;
    getline(cin,s);
    stringstream ss(s);
    ss >> l >> d >> n;
    string word[5005];
    string pat;
    for (int i=0; i<d; i++)
    {
        getline(cin,word[i]);
    }
    for (int i=0; i<n ; i++)
    {
        int count = 0;
        getline(cin, pat);
        for (int k=0; k<d; k++)
        {
            bool broke = false;
            int j = 0;
            int next = 0;
            while (j<l)
            {
                if (pat[next]=='(')
                {
                    next++;
                    bool found = false;
                    while (pat[next]!=')')
                    {
                        if (pat[next]==word[k][j])
                        {   found = true;   }
                        next++;
                    }
                    if (!found)
                    {broke= true;  break;}
                }else
                {
                    if (pat[next]!=word[k][j])                    
                    { broke= true;  break;  }
                }
                next++;
                j++;
            }
            if (!broke) {count++;}
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }
}
