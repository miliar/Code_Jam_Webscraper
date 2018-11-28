#include<iostream>
#include<fstream>
#include<string.h>
#include<cmath>
#include<vector>
using namespace std;
int main()
{
    ofstream fout("out.in");
    ifstream fin("in.in");
    int t;
    fin>>t;
    string tcase = "";
    string temp;
    char values[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int test = 1;
    string output;
    while(test <= t+1)
    {
              tcase = "";
              getline(fin,temp);
                              tcase += temp + ' ';
              //fout<<tcase<<"\n";
               int len = tcase.length();
               output = "";
               for(int i=0;i<len;i++)
               {
                       if(tcase[i] != ' ')
                       output += values[tcase[i]-'a'];
                       else
                       output += ' ';
                       }
               if(test >= 2)
               fout<<"Case #"<<test-1<<": "<<output<<"\n"; 
               test++;
               }
}
