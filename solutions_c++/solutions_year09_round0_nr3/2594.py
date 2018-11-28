#include <iostream>
#include <vector>
#include <string>

using namespace std;

int numcases;

struct combo{
       char x;
       int val;
       };

int analyze(string mainstring)
{
    vector<combo> ini;
    vector<combo> next;
    vector<combo> emptyvec;
    combo tempcombo;
    char what='w';
    for(int x=0;x<mainstring.size();x++)
    {
     if(mainstring[x]==what)
     {
      tempcombo.x=mainstring[x];
      tempcombo.val=x;
      ini.push_back(tempcombo);
     }
    }
    string home("elcome to code jam");
    for(int i=0;i<home.size();i++)
    {
     for(int j=0;j<ini.size();j++)
     {
      for(int k=0;k<mainstring.size();k++)
      {
       if(mainstring[k]==home[i] && k>ini[j].val)
       {
        tempcombo.x=mainstring[k];
        tempcombo.val=k;
        next.push_back(tempcombo);
       }
      }
     }
     ini=next;
     next=emptyvec;
    }
    return ini.size();  
}
int main()
{
    cout.precision(4);
    cin >>numcases;
    cin.ignore();
    string mainstring;
    int x;
    for(int i=1;i<=numcases;i++)
    {
     cout <<"Case #"<<i<<": ";
     getline(cin,mainstring);
     x=analyze(mainstring);
     if(x>1000) cout <<analyze(mainstring) <<endl;
     else if(x>=100) cout <<"0"<<analyze(mainstring) <<endl;
     else if(x>=10) cout <<"00" <<analyze(mainstring) <<endl;
     else cout <<"000" <<analyze(mainstring) <<endl;
     
    }
    return 0;
}
