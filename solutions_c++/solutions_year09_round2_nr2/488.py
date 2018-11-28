#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int si[1000];
int no[1000];
int papa[1000];
double val[1000];
string palabra[200];
double prob(int donde,vector<string>&pal)
{  
     if(donde==-1)return 1;
     bool z=0;
     for(int i=0;i<pal.size();i++)if(pal[i]==palabra[donde]){z=true;break;}
     if(donde==0)z=true;
     if(z)
     {
           //cout<<donde<<si[donde]<<" "<<val[donde]<<endl;
           return val[donde]*prob(si[donde],pal);   
     }
     
     //cout<<donde<<no[donde]<<" "<<val[donde]<<endl;
     return val[donde]*prob(no[donde],pal);       
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int N;
    scanf("%d\n",&N);
    for(int caso=1;caso<=N;caso++)
    {
        char A[100];
        scanf("%s\n",A);
        string temp=A;
        string res=A;
        string respuesta="";
        vector<char>G;
        for(int i=0;i<temp.size();i++)G.push_back(temp[i]);
        next_permutation(G.begin(),G.end());
        for(int i=0;i<temp.size();i++)res[i]=G[i];
                if(res>temp)respuesta=res;
        
        if(respuesta=="")
        {
              int Z[10]={0};
              for(int i=0;i<temp.size();i++)Z[temp[i]-'0']++;
              Z[0]++;
              int u=1;
              while(Z[u]==0)u++;
              Z[u]--;
              respuesta+=u+'0';
              for(int i=0;i<10;i++)while(Z[i]>0){Z[i]--;respuesta+=i+'0';}                 
        }
        cout<<"Case #"<<caso<<": "<<respuesta<<"\n";

            
    }
    return 0;    
}
