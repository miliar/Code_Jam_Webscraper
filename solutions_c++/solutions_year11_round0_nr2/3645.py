#include<iostream>
#include<fstream>
#include<cstring>
#include<string>
#include<cmath>
#include<sstream>
#include<utility>
#include<vector>
#define lint long long int
using namespace std;
int main()
{
    lint count=1;
   
    ifstream fin("in1.txt");
    ofstream fout("out1.txt");
    
    
    
    lint notcs,C1,D1,N1;string inp;
    vector <pair<pair<int,int> ,int> > Cpair;
    vector<pair<int,int> > Dpair;
    vector<char> ans;
    fin>>notcs; 
    int last=0;
   
    for(lint i=0;i<notcs;i++)
    {
             vector<int> X(26,0);
             vector<char> Cstat(676,'a'); 
             vector<int> Dstat(676,-1); 
            fin>>C1;
            for(int j=0;j<C1;j++)
            { 
                    char a1,b1,c1;            
                    fin>>a1>>b1>>c1;int a2,b2,c2;a2=(int)a1-65;b2=(int)b1-65;c2=(int)c1-65;
                  
                    Cstat[a2*26+b2]=c1;
                    Cstat[b2*26+a2]=c1;
            }
            fin>>D1;
            for(int j=0;j<D1;j++)
            { 
                    char a1,b1;            
                    fin>>a1>>b1;int a2,b2;a2=(int)a1-65;b2=(int)b1-65;
                   
                    Dstat[a2*26+b2]=1;
                    Dstat[b2*26+a2]=1;
            }
            fin>>N1;int flag=1; 
            for(int j=0;j<N1;j++)
            {
                    char a1;fin>>a1;int a2 = (int)a1 - 65;
                    if(flag==1){flag=0;ans.push_back(a1);last=a2;X[last]++;}
                    else
                    {
                        if(Cstat[a2*26 + last]!='a')
                        {
                                       ans.pop_back();X[last]--;
                                       ans.push_back(Cstat[a2*26 + last]);
                                       X[(int)Cstat[a2*26 + last] - 65]++;
                                       last=(int)Cstat[a2*26 + last] - 65;
                        }
                        else
                        {
                            for(int j=0;j<26;j++)
                            {
                                    if(X[j]!=0 && Dstat[a2*26+j] == 1)
                                    {
                                               ans.resize(0);flag=1;for(int k=0;k<26;k++)X[k]=0;last=-1;break;
                                    }
                            }
                            if(flag ==0){X[a2]++;ans.push_back(a1);last=a2;}
                        }
                    }
                    
            }
            int s=ans.size();
            
            cout<<"Case #"<<(i+1)<<": [";
            for(int k=0;k<s - 1;k++)
            {
                    cout<<ans[k]<<", ";
            }
            if(s!=0)cout<<ans[s-1];
            cout<<"]\n"; 
            fout<<"Case #"<<(i+1)<<": [";
            for(int k=0;k<s - 1;k++)
            {
                    fout<<ans[k]<<", ";
            }
            if(s!=0)fout<<ans[s-1];
            fout<<"]\n"; 
            ans.resize(0);
            
            
                                                 
                        
            
    }

    int y;cin>>y;
    return 0;
}
                        
                    
           
