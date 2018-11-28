#include<iostream>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<deque>
#include<stack>
#include<algorithm>
#include<queue>
#include<map>
#include<cstdio>
using namespace std;
int main()
{
int t,n,c,d,cs=0;
map<char,int> m;
for(int i=0;i<26;i++) m['A'+i]=-1;
m['Q']=0;m['W']=1;m['E']=2;m['R']=3;m['A']=4;m['S']=5,m['D']=6,m['F']=7;
char comb[8][8];
int opp[8][8];
char c1,c2,c3;
cin>>t;
       while(t--)
       {cs++;
       for(int i=0;i<8;i++)
       for(int j=0;j<8;j++)
       {opp[i][j]=0;
       comb[i][j]='a';
       }
                 cin>>c;
                 for(int i=0;i<c;i++)
                 {
                         cin>>c1>>c2>>c3;
                         comb[m[c1]][m[c2]]=c3;
                          comb[m[c2]][m[c1]]=c3;
                         }
                         cin>>d;
                         for(int i=0;i<d;i++)
                         {
                                 cin>>c1>>c2;
                                 opp[m[c1]][m[c2]]=1;
                                 opp[m[c2]][m[c1]]=1;
                                 }
                                 cin>>n;
                                 //cout<<n<<endl;
                                 vector<char> v;
                                 for(int i=0;i<n;i++)
                                 {
                                         cin>>c1;
                                        // cout<<c1<<endl;
                                         v.push_back(c1);
                                         if(v.size()==1) continue;
                                         vector<char>::iterator it=v.end(),it1=v.end();
                                         --it;
                                         --(--it1);
                                        // cout<<*it<<" "<<*it1<<endl;
                                         if(m[*it1]!=-1)
                                         {
                                         if(comb[m[*it]][m[*it1]]!='a')
                                         {
                                                 char in=comb[m[*it]][m[*it1]];
                                                 v.pop_back();
                                                 v.pop_back();
                                                 v.push_back(in);                      
                                                                       }
                                                                       }
                                                                       
                                            vector<char>::iterator itr=v.end();
                                           itr--;
                                           if(m[*itr]!=-1)
                                           {
                                                  for(int i=0;i<v.size();i++)
                                                  {if(m[v[i]]!=-1)
                                                  if(opp[m[v[i]]][m[*itr]]==1)
                                                  {v.clear();
                                                  break;
                                                  }
                                                  } 
                                                  }                     
                                                                           
                                                                           
                                         
                                         
                                         }
                                         if(v.size()==0) cout<<"Case #"<<cs<<": []"<<endl;
                                         else{
                                         cout<<"Case #"<<cs<<": ["<<v[0];
                                         for(int i=1;i<v.size();i++)
                                         {
                                                cout<<", "<<v[i];
                                         }
                                         cout<<"]"<<endl;
                                                 }
                 }


return 0;
}
