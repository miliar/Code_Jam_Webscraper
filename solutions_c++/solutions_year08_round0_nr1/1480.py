#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <sstream>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
#include <conio.h>
#include <fstream>


using namespace std;

vector <int> findtot(vector <string> se, vector <string> qw, int st)
{
       vector <int> ret;
       int i,j,sum;
       for(i=0;i<se.size();i++)
       {
                               sum=0;
                               for(j=st;j<qw.size();j++)
                               {
                                                        if(se[i]==qw[j])
                                                                        sum++;
                               }
                               ret.push_back(sum);
       }
       return ret;
}
vector <int> findnxt(vector <string> se, vector <string> qw, int st)
{
       vector <int> ret;
       int i,j,sum;
       for(i=0;i<se.size();i++)
       {
                               sum=0;
                               for(j=st;j<qw.size();j++)
                               {
                                                        if(se[i]==qw[j])
                                                        {
                                                                        sum=1;
                                                                        break;
                                                        }
                               }
                               if(sum==1)
                                         ret.push_back(j);
                               else
                                   ret.push_back(-1);
       }
       return ret;
}                              
                               

int main()
{
   // clrscr();
    fstream fin("A-large.in");
    int n,s,q,i,j,k,sum,jt,ii,used;
    string t;
    char cc[1000];
    vector <string> se, qw;
    vector <int> next, total;
    fin>>n;
    for(i=0;i<n;i++)
    {
                     // fetch data at start
                     sum=0;
                    fin>>s;
                    for(j=0;j<=s;j++)
                    {
                                t.resize(0);
                                fin.getline(cc,1000);
                                for(k=0;k<strlen(cc);k++)
                                                         t.push_back(cc[k]);
                                if(j==0)
                                        continue;
                                se.push_back(t);
                    }
                    fin>>q;
                    for(j=0;j<=q;j++)
                    {
                                t.resize(0);
                                fin.getline(cc,1000);
                                for(k=0;k<strlen(cc);k++)
                                                         t.push_back(cc[k]);
                                if(j==0)
                                       continue;
                                qw.push_back(t);
                    }
                    // fetching over
                    // process data
                    //cout<<endl<<n<<" "<<s<<" "<<q<<endl;
                    //cout<<se.size()<<" "<<qw.size()<<endl;
                    used=0;
                    for(ii=0;ii<q;ii++)
                    {
                                    total=findtot(se,qw,ii);
                                    next=findnxt(se,qw,ii);
                                    
                                    jt=0;
                                    k=0;
                                    if(used==0 && ii!=0)
                                               k=k+1;
                                    for(j=0;j<next.size();j++)
                                    {
                                     if(ii>0)
                                     {
                                             if(j==used)
                                                        continue;
                                     }
                                             
                                     if(next[j]==-1)
                                                    goto finished;
                                     if(next[j]==next[k])
                                                   jt++;
                                     if(next[j]>next[k])
                                     {
                                                  k=j;
                                                  jt=0;
                                     }
                                    } 
                                    if(jt>0)
                                    {
                                            //jt=k;
                                            for(j=0;j<total.size();j++)
                                            {
                                             if(next[j]==next[k] && total[j]<total[k] && j!=used)
                                                                 k=j;
                                            }
                                    }  

                                    if(i==-1)
                                    {
                                    if(ii==0)
                                             cout<<n<<" "<<s<<" "<<q<<endl;
                                    cout<<"ii: "<<ii<<" k: "<<k<<" next[k]: "<<next[k]<<" sum: "<<sum+1<<" used: "<<used<<endl;
                                    }
                                    ii=next[k];   
                                    sum++;
                                    used=k;
                    }
                                    
                    // processing over
                    //give result
                    finished:
                    cout<<"Case #"<<i+1<<": "<<sum<<endl;
                    // result over
                    //reinitialize vars
                    se.resize(0);
                    qw.resize(0);

    }
    
    
    /* Debug
    for(i=0;i<n;i++)
    {
                    for(j=0;j<s;j++)
                                    cout<<se[j]<<endl;
                    cout<<endl;
                    for(j=0;j<q;j++)
                                    cout<<qw[j]<<endl;
    }
    */
    //cout<<"done";
    getch();
    return 1;  
}
