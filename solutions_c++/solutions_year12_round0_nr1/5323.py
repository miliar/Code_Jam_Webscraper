#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>

using namespace std;

string trim( const string& s )
  {
  string result( s );
  result.erase( result.find_last_not_of( " " ) + 1 );
  result.erase( 0, result.find_first_not_of( " " ) );
  return result;
  }
  
string translate(map<char, char> peta, string s)
{
       char ss[127], tt[127];
       strcpy(ss, s.c_str());
       int i=0;
       while(ss[i])
       {
        
        if(!isalpha(ss[i]) && ss[i]!=' ') break;
        if(ss[i]==' ')
         tt[i]=' ';
        else
         tt[i] = peta[ss[i]];
         i++;
       }
       tt[i] = '\0';
       return string(tt);
}
int main()
{
    
    char in[112] = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupazooq";
    char out[112] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyqeez";
    map<char, char> peta;
    map<char, char>::iterator it;
    int i;
    for(i=0;i<110;i++)
     peta.insert(pair<char, char>(out[i],in[i]));
    /*
    for(it=peta.begin(); it!=peta.end(); ++it)
     cout<<it->first<<"->"<<it->second<<endl;
    */
     
     string s;
     int c=0,n;
     cin>>n;
     getline(cin,s);
     for(c=0;c<n;c++)
     {
      getline(cin, s);
      //cout<<s.size()<<endl;
      string h = translate(peta, s);
      cout<<"Case #"<<c+1<<": "<<h<<endl;
     }
    
    return 0;
}
    
    
