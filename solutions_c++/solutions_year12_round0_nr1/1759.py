#include <iostream>
#include <bitset>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

void problemA()
{
      char tab[26];
      tab['a'-'a']='y';
      tab['o'-'a']='e';
      tab['z'-'a']='q';
      tab['q'-'a']='z';
      string str="ejp mysljylc kd kxveddknmc re jsicpdrysi";
      string str1="our language is impossible to understand";
      ifstream in("A-small.in");
      for(int i=0;i<str.size();i++)
      {
            if(str[i]!=' ')
            {
                  tab[str[i]-'a']=str1[i];
            }
      }

       str="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
       str1="there are twenty six factorial possibilities";
      for(int i=0;i<str.size();i++)
      {
            if(str[i]!=' ')
            {
                  tab[str[i]-'a']=str1[i];
            }
      }

       str="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    str1="so it is okay if you want to just give up";
      for(int i=0;i<str.size();i++)
      {
            if(str[i]!=' ')
            {
                  tab[str[i]-'a']=str1[i];
            }
      }



      int T;
      getline(in,str);
      stringstream bs(str);
      bs>>T;

      for(int i=1;i<=T;i++)
      {
            cout<<"Case #"<<i<<": ";
            getline(in,str);
            for(int j=0;j<str.size();j++)
            {
                  if(str[j]==' ')
                  cout<<str[j];
                  else
                  cout<<tab[str[j]-'a'];
            }
            cout<<endl;

      }
      in.close();

}

int main()
{
    problemA();
    return 0;
}
