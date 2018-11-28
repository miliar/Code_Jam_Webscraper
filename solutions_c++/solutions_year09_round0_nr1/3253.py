#include <iostream>
#include <string>
#include <boost/regex.hpp>
#include <vector>
using namespace std;

int main()
{
    int a,b,c;
    cin>>a>>b>>c;
    //string str1,str2;
    vector<string> vstr1;
    vector<string> vstr2;
    string temp;
    for (int i = 0;i!=b;i++)
    {
        cin>>temp;
        vstr1.push_back(temp);
    }
    for (int i = 0;i != c;i++)
    {
        cin>>temp;
        for (string::size_type j = 0;j != temp.size();j++)
        {
            if(temp[j] == '(')
                temp[j] = '[';
            if(temp[j] == ')')
                temp[j] = ']';
        }
        vstr2.push_back(temp);
    }
    
    for(int i = 0;i != c;i++)
    {
        int ntemp = 0;
        for(int j = 0;j != b;j++)
        {
            if(boost::regex_match(vstr1[j],boost::regex(vstr2[i])))
                ntemp++;
        }
        cout<<"Case #"<<i+1<<": "<<ntemp<<endl;
    }
    return 0;
}
