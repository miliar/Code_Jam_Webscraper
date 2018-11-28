#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main()
{
    map<char,char> tr;
    ifstream trans("trans.txt");
    //ofstream trans("trans2.txt");
    while(!trans.eof())
    {
        string s1,s2;
        trans>>s1>>s2;
        for(int i=0;i<s1.size();i++)
        {
            //cout<<s1[i]<<" "<<s2[i]<<endl;
            tr[char(s1[i])]=char(s2[i]);
        }
    }
    tr['q']='z';
    tr['z']='q';
    tr[' ']=' ';
    ifstream be("jam.be");
    ofstream ki("jam.ki");
    int t;
    be>>t;
    string s;
    getline(be,s);
    for(int testcase=1;testcase<=t;testcase++)
    {
        ki<<"Case #"<<testcase<<": ";
        getline(be,s);
        for(int i=0;i<s.size();i++)
            ki<<tr[s[i]];
        ki<<endl;
    }
    be.close();
    ki.close();
    return 0;
    return 0;
}
