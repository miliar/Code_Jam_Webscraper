#include <iostream>
using namespace std;
char com[30][30];
bool opp[30][30];
int tn,t;
string s;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j;
    
    cin >> tn;
    for (t=1;t<=tn;t++)
    {
        memset(com,0,sizeof(com));
        memset(opp,0,sizeof(opp));
        int c,d,n;
        cin >> c;
        for (i=0;i<c;i++)
        {
            cin >> s;
            com[s[0]-'A'][s[1]-'A'] = com[s[1]-'A'][s[0]-'A'] = s[2];
        }
        cin >> d;
        for (i=0;i<d;i++)
        {
            cin >> s;
            opp[s[0]-'A'][s[1]-'A'] = opp[s[1]-'A'][s[0]-'A'] = true;
        }
        cin >> n;
        cin >> s;
        for (i=1;i<s.length();i++)
        {
            if (i>0 && com[s[i]-'A'][s[i-1]-'A'])
            {
                s[i-1]=com[s[i]-'A'][s[i-1]-'A'];
                s.erase(i--,1);
                continue;
            }
            for (j=0;j<i;j++)
                if (opp[s[i]-'A'][s[j]-'A'])
                {
                   s.erase(0,i+1);
                   i=0;
                   break;
                }
        }
        cout << "Case #" << t << ": [";
        if (s.length()>0)
        {
            for (i=0;i<s.length()-1;i++)
                cout << s[i] << ", ";
               cout << s[s.length()-1];
        }
        cout << "]" << endl;
    }
    
}
