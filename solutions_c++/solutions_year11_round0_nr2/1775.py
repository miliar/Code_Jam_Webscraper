#include <fstream>
#include <string>
#include <utility>
#include <map>
#include <set>
#include <vector>
#include <list>
using namespace std;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.in");
    int test;
    fin>>test;
    for(int i=1;i<=test;i++)
    {
        int c,d,n;
        fin>>c;
        string s;
        map< pair<char,char>,char> basenot;
        for(int j=0;j<c;j++)
        {
            fin>>s;
            pair<char,char> temp;
            temp.first=s[0];
            temp.second=s[1];
            pair< pair<char,char>,char > obj;
            obj.first=temp;
            obj.second=s[2];
            basenot.insert(obj);

        }
        set<pair<char,char> > notfri;
        fin>>d;
        for(int j=0;j<d;j++)
        {
            fin>>s;
            pair<char,char> temp;
            temp.first=s[0];
            temp.second=s[1];
            notfri.insert(temp);
        }
        list<char> ans;
        fin>>n;
        char ch;
        for(int j=0;j<n;j++)
        {
            fin>>ch;
            ans.push_back(ch);
            list<char>::reverse_iterator rit;
            if(ans.size()>1)
            {
                rit=ans.rbegin();
                map< pair<char,char>,char>::iterator mit;
                pair<char,char> temp;
                temp.first=*rit;
                rit++;
                temp.second=*(rit);
                mit=basenot.find(temp);
                if(mit!=basenot.end())
                {
                    ans.pop_back();
                    ans.pop_back();
                    ans.push_back(mit->second);
                    continue;
                }
                rit=ans.rbegin();
                temp.second=*(rit);
                rit++;
                temp.first=*(rit);
                mit=basenot.find(temp);
                if(mit!=basenot.end())
                {
                    ans.pop_back();
                    ans.pop_back();
                    ans.push_back(mit->second);
                    continue;
                }
                 rit=ans.rbegin();
                 rit++;
                 while(rit!=ans.rend())
                 {
                     temp.first=ch;
                     temp.second=*(rit);
                     if(notfri.find(temp)!=notfri.end())
                     {
                         ans.clear();
                         rit++;
                         continue;
                     }
                     temp.second=ch;
                     temp.first=*rit;
                    if(notfri.find(temp)!=notfri.end())
                     {
                         ans.clear();
                         rit++;
                         continue;
                     }
                    rit++;

                 }
            }

        }
        fout<<"Case #"<<i<<": [";
        list<char>::iterator ansit;
        ansit=ans.begin();
        if(ansit!=ans.end())
        {
            fout<<*ansit;
            ansit++;
        }
        while(ansit!=ans.end())
        {
            fout<<", "<<*ansit;
             ansit++;
        }
        fout<<"]"<<endl;
        ans.clear();
        basenot.clear();
        notfri.clear();
    }
    return 0;
}
