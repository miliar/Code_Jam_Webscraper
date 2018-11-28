#include<fstream>
#include<string>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main ()
{
  ifstream in ("A-small-attempt0.in");
  ofstream out ("A.out");
  string dummy;
  int T;in>>T;getline(in,dummy);
  string alphabet="yhesocvxduiglbkrztnwjpfmaq";
  for (int i=1;i<T+1;++i)
  {
    if (i!=1)
      out<<endl;
    string toTranslate;
    getline(in,toTranslate);
    out<<"Case #"<<i<<": ";
    for (int j=0;j<toTranslate.size();++j)
    {
      if (toTranslate[j]==' ')
        out <<' ';
      else
        out<<alphabet[toTranslate[j]-'a'];
    }
  }
  return 0;
}