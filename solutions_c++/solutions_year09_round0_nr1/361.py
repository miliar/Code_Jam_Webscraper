#include<iostream>
#include<string>
#include<vector>
#include<cassert>
using namespace std;

vector<string> split(string s,string p)
{
               vector<string> prev;
               prev.push_back(s);
               for(int i=0;i<p.size();i++)
               {
                       vector<string> n;
                       for(int j=0;j<prev.size();j++)
                       {
                               string s1=prev[i];
                               int k;
                               while((k=s1.find(p[i])!=string::npos))
                               {
                                                     n.push_back(s1.substr(k));
                                                     s1=s1.substr(k+1,s1.size()-k-1);
                               }           
                       }
                       prev=n;
               }
               return prev;
}
                       
               
int main()
{
    freopen("Q1.in","r",stdin);
    freopen("A12.out","w",stdout);
    freopen("Qerror.out","w",stderr);
    int L,D,N;
    cin>>L;
    cin>>D;
    cin>>N;
    getchar();
    vector<string> A(D);
    for(int i=0;i<D;i++) cin>>A[i];
    
    for(int kase=1;kase<=N;kase++)
    {
            
            string s;
            cin>>s;
            vector<string> check;
            int k=-1;
            bool flag=false;
            for(int i=0;i<s.size();i++)
            {
                    if(s[i]=='(')
                    {
                                 assert(!flag);
                                 flag=true;
                                 k++;
                                 check.push_back("");
                    }
                    else if(s[i]==')')
                    {
                         assert(flag);
                         flag=false;
                    }
                    else
                    {
                        if(flag)
                           check[k].push_back(s[i]);
                        else
                        {
                            string s1;
                            s1.push_back(s[i]);
                            k++;
                            check.push_back(s1);
                        }
                    }
            }
            assert(!flag);
            assert(k==L-1);
            int count=0;
           
            for(int i=0;i<D;i++)
            {
                    bool isposs=true;
                    for(int j=0;j<L && isposs;j++)
                        if(check[j].find(A[i][j])==string::npos)
                           isposs=false;
                    if(isposs) count++;
            }
            cout<<"Case #"<<kase<<": "<<count<<"\n";
    }
}
                           
            
            
            
    
    

