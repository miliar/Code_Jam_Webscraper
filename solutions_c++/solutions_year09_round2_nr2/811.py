#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    string s;
    for(int t=1; t<=T; t++)
    {
        cout << "Case #" << t << ": ";
        cin >> s;
        string backup = s;
        if(next_permutation(s.begin(), s.end())) cout << s;
        else
        {
            if(s == "0") cout << "0";
            else
            {
                sort(s.begin(), s.end());
                char min = '9' + 1;
                int len = s.length();
                for(int i=0; i<len; i++) if(s[i] > '0') min <?= s[i];
                cout << min << '0';
                
                bool check = 1;
                for(int i=0; i<len; i++)
                {
                    if(s[i] == min && check) check = 0;
                    else cout << s[i];
                }
/*                
                string temp = "";
                temp += s[0];
                temp += '0';
                int len = s.length();
                for(int i=1; i<len; i++) temp += s[i];
                
                if(temp[0] == '0')
                {
                    cout << backup << '0';
                }
                else
                {
                    cout << temp;
                }
*/
            }
        }
        cout << endl;
    }
}
