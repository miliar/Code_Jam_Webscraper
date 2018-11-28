#include<stdio.h>
#include<string>
#include<fstream>

using namespace std;
int main()
{
  char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  ifstream in ("C:/Users/Mohit/Desktop/A-small-attempt0.in");
  ofstream out("C:/Users/Mohit/Desktop/output1.txt");
  int t;
  string str;
  in>>t;
  getline(in,str);
  for(int i=1;i<=t;i++)
  {
    getline(in,str);
    out<<"Case #"<<i<<": ";
      for(int j=0;j<str.length();j++)
        {
            if(str[j]==' ')
                out<<" ";
            else
                out<<map[str[j]-'a'];
        }
        out<<"\n";

  }
}


