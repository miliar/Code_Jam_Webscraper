#include <iostream>
#include <string>
using namespace std;
string Sch[102];
string Qry[1002];
bool temp[102];
int q;
int s;

bool Search(string str)
{
    if (str == Sch[s-1])
    {
        if (!temp[s-1])
        {
                temp[s-1] = 1;
                //cout << s-1 <<endl;
                return true;
        }
        else
        {
                return false;
        }
    }
    int i = 0; 
    int j = s-1;
    int m = (i + j) / 2;
    while (str != Sch[m])
    {
        if (str > Sch[m])
        {
                i = m;
                m = (i + j) / 2;
        }
        else
        {
                j = m;
                m = (i + j) / 2;
        }
    }
    
    if (!temp[m])
    {
        temp[m] = true;//cout << m << endl;
        return true;
    }
    else
    {
        return false;
    }
};
int main()
{
    int cases;
    int i = 1;
    cin >> cases;
    while (cases--)
    {
        cin >> s;
        char tt[102];
        gets(tt);
        for (int i=0; i<s; i++)
        {
                gets(tt);
                Sch[i] = tt;
        }
        
        sort(Sch, Sch+s);
        cin >> q;
        gets(tt);
        for (int i=0; i<q; i++)
        {
                gets(tt);
                Qry[i] = tt;
        }
        
        int ans = 0;
        int n = 0;
        int num;
        
        for (; n<q; )
        {
                num = 0;
                
                while (n < q)
                {
                        if (Search(Qry[n]))
                        {
                                num++;
                        }
                        n++;
                        if (num == s)
                                break;
                }
                
                memset(temp, 0, sizeof(temp));
                if ((num==s) && (n<=q))
                {
                        ans++;
                        n--;
                }
                //n--;
         }
        
        cout << "Case #" << i << ": " <<  ans << endl;
        i++;
    }
    return 0;
}
