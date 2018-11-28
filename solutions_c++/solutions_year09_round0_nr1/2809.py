#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

int l,d,n,i,j,k,m,ct,ans;
char c;
string S,t;
bool b;
vector <string> s,s1,s2;
vector <int> v;

int cal(string tmp)
{
    k=0;
    for(j=0;j<l;j++)
    {
        if(j==0)
        {
                  if(tmp[k]=='(')
                  {
                      k++;
                      while(tmp[k]!=')')
                      {
                          c=tmp[k];
                          for(m=0;m<s.size();m++)
                          {
                              if(c==s[m][j])
                              {
                                  s1.push_back(s[m]);

                              }
                          }

                          k++;
                      }
                      k++;
                  }
                  else
                  {
                          c=tmp[k];
                          for(m=0;m<s.size();m++)
                          {
                              if(c==s[m][j])
                              {
                                  s1.push_back(s[m]);
                              }
                          }
                          k++;
                  }
        }
        else
        {

                 if(tmp[k]=='(')
                  {
                      k++;
                      while(tmp[k]!=')')
                      {
                          c=tmp[k];
                          for(m=0;m<s1.size();m++)
                          {
                              if(c==s1[m][j])
                              {
                                  s2.push_back(s1[m]);

                              }
                          }

                          k++;
                      }
                      k++;
                  }
                  else
                  {
                          c=tmp[k];
                          for(m=0;m<s1.size();m++)
                          {
                              if(c==s1[m][j])
                              {
                                  s2.push_back(s1[m]);
                              }
                          }
                          k++;
                  }
                 s1.erase(s1.begin(),s1.end());
                 for(m=0;m<s2.size();m++)
                 {
                     s1.push_back(s2[m]);
                 }
                 s2.erase(s2.begin(),s2.end());

        }
    }
    m=s1.size();
    s1.erase(s1.begin(),s1.end());
    return(m);
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
   
    scanf("%d %d %d%c",&l,&d,&n,&c);
    for(i=0;i<d;i++)
    {
         getline (cin , S);
         stringstream ss(S);
          while(ss>>t)
         {
             s.push_back(t);
         }
    }
    for(i=1;i<=n;i++)
    {

        getline (cin , S);
         stringstream ssb(S);
          while(ssb>>t)
         {
              printf("Case #%d: %d\n",i,cal(t));
         }
         
         
    }
    s.erase(s.begin(),s.end());
}