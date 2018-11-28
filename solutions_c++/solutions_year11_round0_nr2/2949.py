#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<cmath>
#include<map>
using namespace std;

int main()
{
    int t,count = 0;
    ifstream fin("B-small-attempt7.in");
    ofstream fout("output2.in");
    vector <string> a;
    map <char, char> del;
    vector <char> res;
    fin>>t;
    while(t--)
    {
              a.clear();res.clear();del.clear();
              int n1,n2,n3;
              fin>>n1;
              string tmp;
              for(int i = 0; i < n1; i++)
              {
                      fin>>tmp;
                      a.push_back(tmp);
              }
              fin>>n2;
              for(int i = 0; i < n2; i++)
              {
                      fin>>tmp;
                      del[tmp[0]] = tmp[1];
                      del[tmp[1]] = tmp[0];
              }
              fin>>n3;
              fin>>tmp;
              for(int i=0;i<n3;i++)
              {
                      res.push_back(tmp[i]);
                      if(res.size()>1)
                      {
                             char ch1 = res[res.size()-1];
                             char ch2 = res[res.size()-2];
                             int flg = 0;
                             for(int j=0;j<a.size();j++)
                             {
                                     string t1 = a[j];
                                     if(t1[0] == ch1 && t1[1] == ch2)
                                     {res.erase(res.begin()+res.size()-1);res.erase(res.begin()+res.size()-1);res.push_back(t1[2]);
                                     flg=1;break;}
                                     else if(t1[0] == ch2 && t1[1] == ch1)
                                     {res.erase(res.begin()+res.size()-1);res.erase(res.begin()+res.size()-1);res.push_back(t1[2]);
                                     flg=1;break;}
                             }
                             
                             if(flg == 1)
                             {continue;}
                      }
                      map<char, char>::iterator it = del.find(res[res.size()-1]);
                      if(it != del.end())
                      {
                          //cout<<"here "<<del[res[res.size()-1]]<<endl;
                          for(int j=0;j<res.size()-1;j++)
                          if(res[j] == del[res[res.size()-1]])
                          {res.clear();
                           break;}
                      }
                      for(int j=0;j<res.size();j++)
                      cout<<res[j]<<"  ";
                      cout<<endl;
              }
              count++;
              fout<<"Case #"<<count<<": [";
              if(res.size() > 0)
              for(int i=0;i<res.size()-1;i++)
              fout<<res[i]<<", ";
              if(res.size()>0)
              fout<<res[res.size()-1];
              fout<<"]"<<endl;
    }
    //system("pause");
    return 0;
}

// 1 QFT 1 QF 7 FAQFDFQ
