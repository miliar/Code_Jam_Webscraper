#include <iostream>
#include <map>
#include <vector>
#include<fstream>

using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    vector <string> vg,ve;
    map <char,char> m;
    map <char,char>::iterator itr;

    vg.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    vg.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    vg.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");

    ve.push_back("our language is impossible to understand");
    ve.push_back("there are twenty six factorial possibilities");
    ve.push_back("so it is okay if you want to just give up");

    for (int i=0; i<vg.size(); i++)
    {
        for (int j=0; j<vg[i].size(); j++)
        {
            m[vg[i][j]]=ve[i][j];
        }
    }

    m['z']='q';
    m['q']='z';

    vg.clear();
    ve.clear();

    int n;
    cin >> n;
    string s;

    getline(cin,s);

    for (int i=0; i<n; i++)
    {
        getline(cin,s);

        vg.push_back(s);
    }

    for (int i=0; i<n; i++)
    {
        s="";
        for (int j=0; j<vg[i].size(); j++)
        {
            if (vg[i][j]!=' ')
                s+=m[vg[i][j]];
            else
                s+=' ';
        }
        ve.push_back(s);
    }

    for (int i=0; i<n; i++)
    {
        cout << "Case #" << i+1 << ": " << ve[i] << endl;
    }

    return 0;
}



