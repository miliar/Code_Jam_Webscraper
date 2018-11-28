#include <iostream>
#include <fstream>
#include <map>
#include <vector>


using namespace std; 

int main(int argc, char* argv[])
{
  std::ifstream input(argv[1]);
  int cases;
  input>> cases;
  map<char, bool> basemap;
  for(char st='A'; st<='Z'; st++)
  {
    if(st == 'Q' || st == 'W' ||st=='E'
       || st=='R' || st == 'A' || st == 'S'
       || st == 'D' || st == 'F')
      basemap[st] = true;
    else
      basemap[st] = false;
  }

  for(int iter=1; iter<=cases; iter++)
  {
    int combineCnt=0;
    input >> combineCnt;         
    map<string, char> combMap;
     
    for(int i=0; i<combineCnt; i++)
    {
      string s;
      input>> s; 
      string s1="";
      s1 = s1 + s[0]; s1= s1+s[1];
      combMap[s1] = s[2];
      string s2="";
      s2 = s2+s[1]; s2=s2+s[0];
      combMap[s2] = s[2];
    }
    int oppCnt=0;
    input >> oppCnt;
    map<char, char> oppMap;
    for(int i=0; i<oppCnt; i++)
    {
      string s;
      input >>s;
      oppMap[s[0]] = s[1];
      oppMap[s[1]] = s[0];
    }
    int length=1;
    input >>length;
    string inStr;
    input >> inStr;
    // Now real processing begin
    vector<char> res;
    map<char, int> charCntMap;

    for(char st='A'; st<='Z'; st++)
    {
      charCntMap[st] = 0;
    }
    for(int idx=0; idx <length; idx++)
    {
       if(res.size()>0) {
          char top = res.back();
          string s = "";
          s += top;
          s += inStr[idx];
          map<string, char>::iterator it = combMap.find(s);
          if(it!=combMap.end())
          {
             char newtop=it->second;
             res.erase(res.begin()+res.size()-1);
             res.push_back(newtop);
             continue;
          } 
          else
          {
            map<char, char>::iterator it = oppMap.find(inStr[idx]);

            if(it != oppMap.end())
            {
               char oppchar = it->second;
               int i=0;
               int len = res.size();
               for(i=0; i<len; i++)
               {
                  if(oppchar == res[i]) {
                    res.clear();
                    break;
                  }
               }
               if( i== len)
                  res.push_back(inStr[idx]);
               
             } 
             else {

               res.push_back(inStr[idx]);
             }

           }
          
       }     
       else
       {
          res.push_back(inStr[idx]);
       }
     // cout<<"idx=" <<idx;
     // for(int i=0; i<res.size(); i++)
     // cout << " " << res[i];
     // cout <<endl;     
    }

    cout<<"Case #"<<iter<<": [";
    int len = res.size();
    for(int i=0; i<len-1; i++)
      cout << res[i] <<", ";
    if(res.size()>0)
      cout << res.back();
      cout << "]"<<endl;
  }  

}
