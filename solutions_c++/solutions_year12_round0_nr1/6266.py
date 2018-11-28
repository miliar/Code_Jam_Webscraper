#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<set>
#include<algorithm>
#include<cstdlib>
#include<cctype>
#include<iomanip>
#include<sstream>
#include<stack>
#include<queue>
#include<utility>
#include<functional>
#include<numeric>
#include<ctime>
#include<fstream>
//#include<conio.h>
using namespace std;
int main()
{
    char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
      int t,l,x;
      string str,res;
      ifstream ifile("input.txt");
      ofstream ofile("output.txt");
      if(ifile.is_open())
      getline(ifile,str);
      t=atoi(str.c_str());
      for(int i=1;i<=t;i++)
      {
              res="";
              getline(ifile,str);   
              int l=str.length();
              for(int j=0;j<l;j++)
              {
                      if(isspace(str[j]))
                       res+=" ";
                      else
                      {
                          x=str[j];
                          res+=a[x-97];
                      }
              }       
              ofile<<"Case #"<<i<<": "<<res<<"\n";                     
      }
      ifile.close();
      ofile.close();
      return 0;
}
