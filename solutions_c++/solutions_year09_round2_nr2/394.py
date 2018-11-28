#include <iostream>
#include <string>
#include <vector>
using namespace std;

string inp;
vector<int> lef;
string sear(int pos, bool strict)
{
    if(pos == inp.size())
        return "";
    int st=0;
    if(strict)
    {
        st = inp[pos]-'0';
        if(pos == inp.size()-1)
            st++;
    }
    for(int d = st;d<10;d++)
    {
        if(!lef[d])
            continue;
        lef[d]--;
        string ret = sear(pos+1, strict && d+'0'==inp[pos]);
        lef[d]++;
        if(ret != "-")
        {
            ret = "-" + ret; 
            ret[0] = d + '0';
            return ret;
        }
    }
    return "-";
}

int main()
{
    int n;
    cin >> n;
    for(int i=1;i<=n;i++)
    {
        cin >> inp;
        inp = string("0") + inp;
        cout << "Case #" << i << ": ";
        lef.clear();
        lef.resize(10);
        for(int k=0;k<inp.size();k++)
            lef[inp[k]-'0']++;
        string r = sear(0,true);
        if(r[0]=='0')
            r = r.substr(1,r.size()-1);
        cout << r << endl;

    }
}
