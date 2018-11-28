#include<sstream>
#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<set>
#include<utility>
using namespace std;

int main ()
{
  ifstream in ("C-small-attempt0.in");
  ofstream out ("A.out");
  int T,A,B;
  in>>T;
  for (int i=1;i<T+1;++i)
  {
    if (i!=1)
      out<<endl;
    in>>A>>B;
    set< pair<int,int> > s;
    for (int j=A;j<=B;++j)
    {
      stringstream ss;
      ss<<j;
      string temp=ss.str();
      for (int k=1;k<temp.size();++k)
      {
        string temp1=temp.substr(k,temp.size()-k+1);
        temp1+=temp.substr(0,k);
        int toInsert=atoi(temp1.c_str());
        if (temp1[0]!='0'&&toInsert!=j&&toInsert>=A&&toInsert<=B)
        {
          s.insert(pair<int,int>(min(toInsert,j),max(toInsert,j)));
        //  out<<"Works: "<<min(toInsert,j)<<' '<<max(toInsert,j)<<endl;
        }
       /* else
          out<<"Doesn't Work: "<<min(toInsert,j)<<' '<<max(toInsert,j)<<endl;*/
      }
    }
    out<<"Case #"<<i<<": "<<s.size();
  }
  return 0;
}