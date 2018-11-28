#include <iostream>
#include <bitset>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

void ProblemC()
{
      const int MAX_N=2000001;
      vector<set<int> > tab(MAX_N);
      ifstream in("C-large.in");

      for(int i=1;i<MAX_N;i++)
      {
            set<int> tmp;
            stringstream bs;
            bs<<i;
            string str=bs.str();
            int len=str.size();

            for(int j=1;j<len;j++)
            {
                  string str1=str.substr(j);
                  string str2=str.substr(0,j);
                  string str3=str1+str2;

                  stringstream bs1(str3);
                  int t;
                  bs1>>t;
                  stringstream bs2;
                  bs2<<t;

                  if(bs2.str().size()==len)
                  {
                        if(i<t)
                  tmp.insert(t);
                  }




            }
            tab[i]=tmp;
      }
            int T;
            in>>T;
            for(int i=1;i<=T;i++)
            {
                  int A,B;
                  in>>A>>B;
                  long long int count=0;
                  for(int j=A;j<=B;j++)
                  {
                        set<int>::iterator it;
                        for(it=tab[j].begin();it!=tab[j].end();it++)
                        {
                              if((*it) <= B)
                              count++;
                              else
                              break;
                        }
                  }
                  cout<<"Case #"<<i<<": "<<count<<endl;

            }

            in.close();







}

int main()
{
    ProblemC();
    return 0;
}
