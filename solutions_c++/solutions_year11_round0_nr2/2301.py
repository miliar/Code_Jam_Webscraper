#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <list>
using namespace std;

void exec();
int main()
{
    exec();
    return 0;
}
void exec()
{
    ifstream file("B-large.in");

    int T=0,C,D,N;
    string str2="";
    char str1;
    map<string,char>::iterator it1;
    set<string>::iterator it2;
    list<char>::iterator it3;
    list<char>::reverse_iterator  it;
    file>>T;
    for(int i=1;i<=T;i++)
    {
          file>>C;
          map<string,char> comb;
          set<string> opp;
          list<char> liste;
          for(int j=0;j<C;j++)
          {
                file>>str1;
                str2="";
                str2.push_back(str1);
                file>>str1;
                str2.push_back(str1);
                file>>str1;
                comb.insert(pair<string,char>(str2,str1));
                }
          file>>D;
          for(int j=0;j<D;j++)
          {

                file>>str1;
                str2="";
                str2.push_back(str1);
                file>>str1;
                str2.push_back(str1);
                opp.insert(str2);
                }

           file>>N;
           for(int j=0;j<N;j++)
           {
                 file>>str1;
                 if(liste.empty())
                       liste.push_back(str1);
                 else
                 {
                       str2="";
                       str2.push_back(liste.back());
                       str2.push_back(str1);
                       it1=comb.find(str2);
                       if(it1!=comb.end())
                            {

                                  liste.pop_back();
                                  liste.push_back((*it1).second);
                                  continue;
                            }

                        str2="";
                        str2.push_back(str1);
                        str2.push_back(liste.back());
                        it1=comb.find(str2);
                        if(it1!=comb.end())
                            {
                                  liste.pop_back();
                                  liste.push_back((*it1).second);
                                  continue;
                            }
                        liste.push_back(str1);

                        for(it=liste.rbegin();it!=liste.rend();it++)
                            {
                                   str2="";
                                   str2.push_back(str1);
                                   str2.push_back(*it);
                                   it2=opp.find(str2);
                                   if(it2!=opp.end())
                                   {
                                          liste.clear();
                                          break;
                                   }


                                   str2="";
                                   str2.push_back(*it);
                                   str2.push_back(str1);
                                   it2=opp.find(str2);
                                   if(it2!=opp.end())
                                   {
                                          liste.clear();
                                          break;
                                   }
                              }




                 }

           }
         cout<<"Case #"<<i<<": "<<"[";
         for(it3=liste.begin();it3!=liste.end();++it3)
         {
               if(it3==liste.begin())
                cout<<*it3;
                else
                 cout<<", "<<*it3;
         }
         cout<<"]"<<endl;
    }
    file.close();
}
