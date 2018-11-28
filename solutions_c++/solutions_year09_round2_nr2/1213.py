#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;

//long long int x;
string s;
int n[10],T;

void getdigits()
{
     for(int i=0;i<s.length();i++)
     {
               n[int(s[i]-'0')]++;

     }
}
int main(int argc, char* argv[])
{
    int i,j,k,min,tk;
    cin>>T;
    //cout<<T;
    for(int j=0;j<T;j++)
    {
     vector <char> v;
      for(i=0;i<10;i++)
                       n[i]=0;
      cin>>s;
      //cout<<"s="<<s<<endl;
      getdigits();
      //for(i=0;i<10;i++)
        //               cout<<n[i];
                       
      i=s.length() -2;
      v.push_back(s[i+1]);
      while(i>=0)
      {
              n[int(s[i]-'0')]--;
              v.push_back(s[i]);
              if(s[i] < s[i+1])
                      break;
              i--;
                 
      }
      if(i!=-1)
      {
               //cout<<"v"<<v[1];
               sort(v.begin(),v.end());
               min=s[i+1];
               for(k=0;k<v.size();k++)
                                      if(s[i+1]==v[k])
                                                      tk=k;
               for(k=0;k<v.size();k++)
               {
                                        if(v[k]<min && v[k]>s[i])
                                        {
                                                     min=v[k];
                                                     tk=k;
                                        }
               }
               k=0;
               s[i]=min;
               i++;
               //cout<<v[tk];
               while(k<v.size())
               {
                   if(k!=tk)
                   {
                             s[i]=v[k];
                             i++;
                   }
                   k++;
                                  
               }
               //cout<<"min"<<char(min);
               cout<<"Case #"<<j+1<<": "<<s<<endl;
      }
      else
      {
          char g[30];
          int q;
          sort(v.begin(),v.end());
          q=0;
          while(v[q]=='0') q++;
          g[0]=v[q];
          g[1]='0';
          i=2;
          //cout<<"*"<<g[0]<<"*";
          for(k=0;k<v.size();k++)
          {
            if(k!=q)
            {        g[i]=v[k];                     
                     i++;
            }
          }
          g[i]='\0';
          cout<<"Case #"<<j+1<<": "<<g<<endl;
      }
      
    }
    //cout<<c;
    //system("PAUSE");
}
