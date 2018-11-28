#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
bool isletra(char ad)
{
    if(ad>='a' && ad<='z')return 1;
    return 0;
}
int main()
{
  //  freopen("in.txt","r",stdin);
  // freopen("out.txt","w",stdout);
    
    int L,D,N;
    cin>>L>>D>>N;
    vector<string>name(D),query(N);
    vector<vector<string> >consulta(N);
    vector<int>solve(N,0);
    for(int i=0;i<D;i++)
        cin>>name[i];
    for(int i=0;i<N;i++)
    {
        cin>>query[i];
        string x="";
        for(int j=0;j<query[i].size();j++)
        {
            if(query[i][j]!='(')consulta[i].push_back( string(1,query[i][j]) );
            if(query[i][j]=='(')
            {
                x="";
                j++;
                while(query[i][j]!=')')    
                {
                    x+=query[i][j];
                    j++;
                }
                sort(x.begin(),x.end());
                consulta[i].push_back(x);
            }
        }
           
    }
   
    
    for(int i=0;i<D;i++)
    {
        string s=name[i];
        for(int j=0;j<N;j++)
        {
            bool ok=1;
            for(int k=0;k<consulta[j].size();k++)
                if(binary_search(consulta[j][k].begin(),consulta[j][k].end(),s[k])!=1)ok=0;            
            if(ok)solve[j]++;
        }
    }    
    for(int i=0;i<N;i++)
        cout<<"Case #"<<i+1<<": "<<solve[i]<<endl;    
    
   // system("pause");
    return 0;
}


