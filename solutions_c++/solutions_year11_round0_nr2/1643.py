#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<map>

using namespace std;

map<char,char> com[27];
vector<char> opp[27];
int t,i,j,tc,c,d,n,ich;
string ss;
char ch,pch;

//map<char,bool> mark;
bool mark[27];

main()
{
      char s[10];
      
      scanf("%d",&t);
      
      for(tc=1;tc<=t;++tc){
         
         memset(mark,0,sizeof(bool) * 27);
         for(i=0;i<27;++i) { com[i].clear(); opp[i].clear(); } 
         ss="";
         
         scanf("%d",&c);
         
         for(i=0;i<c;++i){
            scanf("%s",&s);
            //cout<<s<<"\n";
            //com[s[0]-'A'].push_back(s[1]);
            //com[s[0]-'A'].push_back(s[2]);
            com[s[0]-'A'][s[1]]=s[2];
            
            //com[s[1]-'A'].push_back(s[0]);
            //com[s[1]-'A'].push_back(s[2]);
            com[s[1]-'A'][s[0]]=s[2];
         }
         
         scanf("%d",&d);
         for(i=0;i<d;++i){
            scanf("%s",&s);
           // cout<<s<<"\n";
            opp[s[0] - 'A'].push_back(s[1]);
            opp[s[1] - 'A'].push_back(s[0]);
            
            //com[s[0]].push_back(s[2]);
         }
         
         scanf("%d",&n);
         
         cin>>ch; 
         mark[ch - 'A']=true;
         pch=ch;
         ss=ch;
         //cout<<ch<<"\n\n";
         //cout<<"--- "<<ss<<"\n";
         
         for(i=1;i<n;++i){
            cin>>ch;
            mark[ch - 'A']=true;
            ss+=ch;
            //cout<<ss<<" ---------------------------\n\n";
            ich=ch-'A';
            
            if(ss.length()>1){
            
               if(com[ich].find(pch)!=com[ich].end())
               {  
                   ss.erase(ss.length()-2);
                   if(ss.find(ch)==string::npos) mark[ich]=false;
                   if(ss.find(pch)==string::npos) mark[pch-'A']=false;
                   
                   ss+=com[ich][pch];
                   pch=com[ich][pch];
               }
               else if(! (opp[ich].empty()))
               {   for(j=0;j<opp[ich].size();++j)
                   {   if(mark[opp[ich][j] - 'A'])
                       {    ss="";
                            memset(mark,0,sizeof(bool) * 27);
                            break;
                       }
                   }
               }
            }
            
            if(ss.length()) pch=ss[ss.length()-1];
            
            //cout<<"--- "<<ss<<"\n";
         
         }
         cout<<"Case #"<<tc<<": ";
         
         cout<<"[";
         if(ss.length()) cout<<ss[0];
         for(i=1;i<ss.length();++i) cout<<", "<<ss[i];
         
         cout<<"]\n";
         
      }
}
