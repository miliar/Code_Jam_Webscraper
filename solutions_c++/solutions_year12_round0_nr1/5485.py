#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
    string c(123,0);
    c[97]='y';
    c[98]='n';
    c[99]='f';
    c[100]='i';
    c[101]='c';
    c[102]='w';
    c[103]='l';
    c[104]='b';
    c[105]='k';
    c[106]='u';
    c[107]='o';
    c[108]='m';
    c[109]='x';
    c[110]='s';
    c[111]='e';
    c[112]='v';
    c[113]='z';
    c[114]='p';
    c[115]='d';
    c[116]='r';
    c[117]='j';
    c[118]='g';
    c[119]='t';
    c[120]='h';
    c[121]='a';
    c[122]='q';
    
    int t;
    cin>>t;
   cin.ignore('\n');
    cin.clear();
    cin.sync();
    string s;
    for(int i=0;i<t;i++)
    {
             if(getline(cin,s));
             for(int counter=0;counter<s.size();counter++)
             {
                     if(c.find(s[counter])!=-1)
                     s[counter]=c.find(s[counter]);
                     }
              cout<<"Case #"<<i+1<<": "<<s<<endl;
              s.clear();
              }
              }
