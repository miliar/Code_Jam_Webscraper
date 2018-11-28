#include<fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    ifstream inputf;
    int cn=0;
    int L,D;
    ofstream outputf;
    char inputFilename[] = "A-large.in";
    char outputFilename[] = "output.list";
    inputf.open(inputFilename, ios::in);
    outputf.open(outputFilename, ios::out);
    inputf >> L;
    inputf >> D;
    inputf >> cn;
    vector <string> p_words;
    for(int i1=0;i1<D;i1++)
    {
        string word;
        inputf >> word;
        p_words.push_back(word);        
    }
    for(int i1=1;i1<=cn;++i1)
    {
       string word;
       inputf >> word;
       vector <string> poss_words;
       string temp="";
       int flag=0;
       for(int i=0;i<word.length();i++)
       {
              if(word[i]=='(')
              {
                  flag=1;
                  temp = "";
                  continue;
              }
              else if (word[i]==')')
              {
                  flag=0;
                  poss_words.push_back(temp);   
                  temp = "";
                  continue;
              }
              if (flag==1)
              {
                 temp = temp + word[i];
                 continue;
              }
              else
              {
                  temp += word[i];
              }    
              poss_words.push_back(temp);   
              temp = "";
       }
       int ret = 0;
       for(int i=0;i<D;i++)
       {
               int flag = 1;
               for(int j=0;j<L;j++)
               {
                       if(poss_words[j].find(p_words[i][j]) == -1)
                          flag=0;
               }
               ret +=flag;
       }
       outputf << "Case #"<<i1<<": "<<ret<<endl;
    }
    outputf.close();
    inputf.close();
    return 0;
}
