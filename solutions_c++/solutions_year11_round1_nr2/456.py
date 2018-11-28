#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


bool isCompatible(string &word,char c,vector<int> &mp,vector<string> & dict,vector<char> &tries)
{
     string s;
     for(int i=0;i<mp.size();i++)
     {
             s=dict[mp[i]];
             if(s.length() != word.length())
             continue;
             
             bool f=false;
             for(int k=0;k<s.length();k++)
             {
                     if(word[k]=='_')
                     {
                                     
                            for(int kk=0;kk<tries.size();kk++)
                            {
                                    if(tries[kk]==s[k])
                                    {
                                                       f=true;
                                                       goto lb;
                                    }
                            }         
                                     
                            
                     }
                     
             }
            lb: if(f) continue;
             
             bool flag=true;
             for(int j=0;j<word.length();j++)
             {
                     if(word[j]!='_')
                     {
                                     if(s[j]!=word[j])
                                     { flag=false; break;}
                     }
             }
             if(flag) return flag;
     }
     
     return false;
     
}

int reveal(string &word,string dictw,char c)
{
    bool flag=false;
    for(int i=0;i<dictw.length();i++)
    {
            if(dictw[i]==c)
            {
                           word[i]=c;
                           flag=true;
            }
                       
    }
    
return (flag)?0:1;    
}

bool allreveal(string s)
{
     for(int i=0;i<s.length();i++)
     if(s[i]=='_') return false;
     
     return true;
}
int main()
{
    
    int T,N,M;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
              
              vector<int> mp[26];
              vector<string> dict;
              vector<string> ans;
              string s;
              cin>>N>>M;
                      
              for(int i=0;i<N;i++)
              {
                      bool f[26];
                      for(int j=0;j<26;j++) f[j]=false;
                      cin>>s;
                      dict.push_back(s);
                      
                      for(int j=0;j<s.length();j++)
                      {
                              if(!f[s[j]-'a'])
                              {
                                              f[s[j]-'a']=true;
                                              mp[s[j]-'a'].push_back(i);
                              }
                      }
                      
              }
              
              for(int i=0;i<M;i++)
              {
                      int maxpoints=0;
                      cin>>s;
                      int index=0;
                      
                      for(int j=0;j<N;j++)
                      {
                            int points=0;
                            string word="";
                            vector<char> tries;  
                            for(int k=0;k<dict[j].length();k++) word+="_";
                            
                            for(int k=0;k<26;k++)
                            {
                                    if(isCompatible(word,s[k],mp[s[k]-'a'],dict,tries))
                                    {
                                               points+=reveal(word,dict[j],s[k]);
                                               
                                               if(allreveal(word))
                                               break;
                                    }
                                    tries.push_back(s[k]);
                            }
                            
                            assert(allreveal(word));
                            if(points>maxpoints)
                            {
                                                maxpoints=points;
                                                index=j;
                            }
                        }
                        
                       // cout<<dict[index]<<" ";
                        ans.push_back(dict[index]);
                  }
                        
              cout<<"Case #"<<t<<":";
              for(int i=0;i<ans.size();i++)
              cout<<" "<<ans[i];
              
              cout<<endl;
                                                            
                        
      }
              
    
    
}
