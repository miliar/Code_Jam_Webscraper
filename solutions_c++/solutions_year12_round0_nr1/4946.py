#include<iostream>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
    string s="ynficwlbkuomxsevzpdrjgthaq";
    string p="yhesocvxduiglbkrztnwjpfmaq";
    int i,j,k,l=0,t;
    cin>>t;
    cin.ignore();
    while(t--)
    {
              string sa;
              getline(cin,sa);
              i=sa.length();
              //cout<<i;
               cout<<"Case #"<<++l<<": ";
              for(j=0;j<i;j++)
              {
                        if(sa[j]==' ')
                        cout<<" ";
                        else
                        cout<<p[sa[j]-'a'];
              }
              cout<<endl;
    }
return 0;

}

    
