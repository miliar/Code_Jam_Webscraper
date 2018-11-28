#include<iostream>
#include<vector>
using namespace std;
string W[5000];
int main()
{
    int N,D,C;
    
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>C>>D>>N;
    for(int i=0;i<D;i++)cin>>W[i];
    for(int caso=0;caso<N;caso++)
    {
            string temp;
            cin>>temp;
            vector<string>V;
            int d=0;
            while(d<temp.size())
            {
                  if(temp[d]!='(')
                  {
                       string hh="";
                       hh+=temp[d];
                       d++;        
                       V.push_back(hh);
                       continue;                
                  }              
                  d++;              
                  string u="";
                  while(temp[d]!=')')
                  {
                     u+=temp[d];
                     d++;                   
                  }
                  d++;
                  V.push_back(u);                    
            }
          
            int s=0;
            for(int i=0;i<D;i++)
            {
                 int j;   
                 for( j=0;j<C;j++)
                 {
                       int k=0;
                       for(k=0;k<V[j].size();k++)if(V[j][k]==W[i][j])break;
                       if(k==V[j].size())break;        
                 }   
                 if(j==C)s++;
            }
            cout<<"Case #"<<caso+1<<": "<<s<<endl;        
    }
return 0;    
}
