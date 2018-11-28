#include<iostream>
#include<map>
#include<list>
#include<vector>
#include<set>
#include<algorithm>
#include<math.h>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    map<char, char> mapa;
    
    string a[4];
    string b[4];
    
    a[1] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    a[2] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    a[3] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    b[1] = "our language is impossible to understand";
    b[2] = "there are twenty six factorial possibilities";
    b[3] = "so it is okay if you want to just give up";
    
    for(int j = 1; j <= 3; j ++)
    {
      for(int i = 0; i < a[j].size(); i ++)
      {
              mapa[a[j][i]] = b[j][i];
      }
    }
    mapa['z'] = 'q';
    mapa['q'] = 'z';
    
    /*
    map<char, char>::iterator it;
    for(it = mapa.begin(); it != mapa.end(); it++)
    {
           cout<<it->first<<" "<<it->second<<endl;
    }
    */
    
    int casos, caso = 1;
    string variable;
    cin>>casos;
    cin.ignore();
    while(casos--)
    {
                  
                  getline(cin, variable);
                  cout<<"Case #"<<caso<<": ";
                  for(int i = 0;i < variable.size(); i ++)
                  {
                          cout<<mapa[variable[i]];
                  }
                  cout<<endl;
                  caso++;
    }
    
    
    
    
   
    return 0;
}
