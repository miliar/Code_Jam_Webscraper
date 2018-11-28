#include<fstream>
#include<queue>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<iostream>

#define f(i,a,b) for(int (i)=(a);(i)<(b);++(i))

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B.out");
    
    int t,c,d,n;
    fin>>t;
    char temp,t2;
    string t3;
    set<char>::iterator it;
    vector<char> kl;
    vector<char> k2;
    f(cas,1,t+1)
    {
                fin>>c;
                string com[2*c];
                f(i,0,c)
                {
                        fin>>com[i];
                        com[i+c]=com[i];
                        temp=com[i+c][0];
                        com[i+c][0]=com[i+c][1];
                        com[i+c][1]=temp;
                }
                fin>>d;
                string des[d];
                
                f(i,0,d)
                {
                        fin>>des[i];
                }
                fin>>n;
                string seq;
                fin>>seq;
                string ans;
              //  set<char> bad;
                f(i,0,n)
                {
                      //  cerr<<i<<ans<<"\n";
                        ans+=seq.substr(i,1);
                        if(ans.size()>1)
                        {
                                        f(j,0,2*c)
                                        {
                                                 if(ans.substr(ans.size()-2,2)==com[j].substr(0,2))
                                                 {
                                                                                                   ans.replace(ans.size()-2,2,com[j].substr(2,1));
                                                                                                   break;
                                                 }
                                        }
                                        
                                       
                        }
                        
                        f(j,0,((int)ans.size())-1)
                        {
                                         //  cerr<<j<<" "<<ans.size();
                                           f(p,0,d)
                                           {
                                                   if(ans[j]==des[p][0]&&ans[ans.size()-1]==des[p][1])
                                                   {
                                                                                                      ans="";
                                                                                                      break;
                                                   }
                                                  // cerr<<"t";
                                                   if(ans[j]==des[p][1]&&ans[ans.size()-1]==des[p][0])
                                                   {
                                                                                                      ans="";
                                                                                                      break;
                                                   }
                                           }
                        }
                       // cerr<<"\n";
                        
                }
                fout<<"Case #"<<cas<<": [";
                f(i,0,(int)ans.size()-1)
                {
                                   fout<<ans[i]<<", ";
                }
                if(ans.size()>0)
                {
                                fout<<ans[ans.size()-1];
                                
                }
                fout<<"]\n";
    }
    
    fin.close();
    fout.close();
   // cin>>t;
    return 0;
}
    
