#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<stack>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<set>
#include<bitset>

using namespace std ;
#define INF (int)1e9 


int main()
{
    freopen("a.in","r",stdin);
  freopen("out.txt","w",stdout);
    int i,j,k,nt,ns,nq;
    cin>>nt;
    for(i=0;i<nt;i++)
    {
            cin>>ns;getchar();
            vector <string> search;
            vector <string> query;
            vector <string> temp;
            string s;
            for(j=0;j<ns;j++)
            {
             char inp[500] ;
             gets(inp) ;
             s.assign(inp) ;
             temp.push_back(s) ;
            }
            search.assign(temp.begin(),temp.end());
            temp.clear();
            cin>>nq;getchar();
            for(j=0;j<nq;j++)
            {
             char inp[500] ;
             gets(inp) ;
             s.assign(inp) ;
             temp.push_back(s) ;
            }
            query.assign(temp.begin(),temp.end());
            
            vector<vector <int> > pos;
            vector <int>  v;  
            for(j=0;j<ns;j++)
            {
                    for(k=0;k<nq;k++)
                    {
                            if(query.at(k)==search.at(j))
                            v.push_back(k);
                            
                    }
                    pos.push_back(v);
                    v.clear();
                    
            }
            
            int ret = 0 ;
            int ptr = 0 ;
            while(ptr < nq)
            {
             int best = ptr ;
             for(j=0;j<ns;j++)       
             {
              if(pos[j].size() == 0) break ;
              if(pos[j][pos[j].size()-1] < ptr){best = nq ;break;}
              for(k=0;k<pos[j].size();k++)
               if(pos[j][k] >= ptr)
               {
                if(pos[j][k] == ptr) break ;
                if(pos[j][k] > best)
                 best = pos[j][k] ;            
                break ;
               }
             }       
             if(j < ns) break ;
             ret ++ ; ptr = best ;
            }
            
     printf("Case #%d: %d\n",i+1,ret) ; 
     
    } 
    
}

