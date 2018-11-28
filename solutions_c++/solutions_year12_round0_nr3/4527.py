#include<iostream>
#include<string>
#include<sstream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
              
              string a,b;
              cin>>a>>b;
              int test,adec,bdec,counter=0;
              while(1)
              {
              istringstream stream(a);
              stream>>adec;
              istringstream stream2(b);
              stream2>>bdec;
              if(adec==bdec)
              {cout<<"Case #"<<tt<<": "<<0<<endl;
              break;}
              for(int i=1;i<a.size();i++)
              {
                      if(a[i]=='0')
                      continue;
              string a1;
              a1.insert(a1.begin(),a.begin()+i,a.end());
              a1.insert(a1.end(),a.begin(),a.begin()+i);
              istringstream streamtest(a1);
              streamtest>>test;
              if(test>adec && test<=bdec)
                  {
                  counter++;
                  }
              a1.clear();
              }
              adec++;
              ostringstream streamout;
              streamout<<adec;
              a=streamout.str();
              if(adec==bdec)
              {
                            cout<<"Case #"<<tt<<": "<<counter<<endl;
                            counter=0;
              break;
              }
              }
              }
              }
