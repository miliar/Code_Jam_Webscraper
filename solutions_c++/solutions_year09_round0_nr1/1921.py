#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int L, D, N;
    cin >> L >> D >> N;
    
    //input dictionary
    vector <string> dict;
    for(int i=0; i<D; i++)
    {
        string s;
        cin >> s;
        dict.push_back(s);
    }
    
    for(int i=0; i<N; i++)
    {
        cout << "Case #" << i+1 << ": ";
        string s;
        cin >> s;
        bool exist[15][26];
        memset(exist, 0, sizeof(exist));
        
        int length = s.length();
        int idx = 0;
        bool active = 0;
        for(int j=0; j<length; j++)
        {
            if(s[j] == '(')
            {
                //if(j>0 && s[j-1] != ')') idx ++;
                active = 1;
            }
            else if(s[j] == ')')
            {
                //if(j+1<length && s[j+1] != '(') idx ++;
                idx ++;
                active = 0;
            }
            else
            {
                if(active)
                {
                    exist[idx][s[j]-'a'] = 1;
                }
                else
                {
                    exist[idx][s[j]-'a'] = 1;
                    idx ++;
                }
            }
        }
        
        int total = 0;
        for(int j=0; j<D; j++)
        {
            bool check = 1;
            for(int k=0; k<dict[j].length(); k++) if(exist[k][dict[j][k]-'a'] == 0)
            {
                check = 0;
                break;
            }
            if(check) total ++;
        }
        
        cout << total << endl;
    }
}
