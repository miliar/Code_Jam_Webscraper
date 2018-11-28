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
#include<fstream>
 
using namespace std;
 
 int main()
 {
     ifstream file;
     ofstream out;
     file.open("c:\\b\\input.txt");
     out.open("c:\\b\\output.txt");
     int n;
     file>>n;
     char replace[26];
     replace[0]='y';
     replace[1]='h';
     replace[2]='e';//c
     replace[3]='s';
     replace[4]='o';
     replace[5]='c';
     replace[6]='v';
     replace[7]='x';//h
     replace[8]='d';
     replace[9]='u';//j
     replace[10]='i';
     replace[11]='g';
     replace[12]='l';
     replace[13]='b';
     replace[14]='k';
     replace[15]='r';
     replace[16]='z';////
     replace[17]='t';
     replace[18]='n';
     replace[19]='w';
     replace[20]='j';
     replace[21]='p';
     replace[22]='f';
     replace[23]='m';
     replace[24]='a';
     replace[25]='q';

     string tmp;
     getline(file,tmp);
     for(int i=0;i<n;i++)
     {
         string s;
         getline(file,s);
         for(int j=0;j<s.length();j++)
         {
             if(s[j]==' ')
                 continue;
             s[j]=replace[s[j]-'a'];
         }
         out<<"Case #"<<(i+1)<<": "<<s<<endl;
     }
     return 0;
 }