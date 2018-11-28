#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cmath>
#include<algorithm>



using namespace std;


  bool prime[1001];
  
int parent[10000];
int rank[10000];

 int merge(int a, int b) //a y b son ambos de nivel superior
 {
     
     //Modificar para gestionar el enemy, y poner -1 si falla

      if(rank[b]>rank[a]) 
      {
         parent[a]=b;
      }
      else 
      {
         parent[b]=a;
      }
      if(rank[a]==rank[b])
        rank[a]++;
  }
 
 int find_r(int x){
     if(x==-1) return -1;
     return parent[x]=(parent[x]==x?x:find_r(parent[x]));}

 int find(int x){
     return parent[x]=(parent[x]==x?x:find(parent[x]));}
 
 

int main()
{
 int N;
 cin>>N;
 for(int i=0;i<N;i++)
 {
  cout<<"Case #"<<i+1<<": ";
  
  
  
  long long A,B,P;
  cin>>A>>B>>P;
  
    for(int i=0;i<=B;i++)
      parent[i]=i;
  
    for(int i=0;i<=B;i++)
      rank[i]=0;
 
  
  prime[0]=1;
  prime[1]=1;
  prime[2]=1;
  for(int j=3;j<1001;j++)
   prime[j]=1;
  for(int j=2;j<1001;j++)
  {
   if(prime[j])
    for(int k=2*j;k<1001;k+=j)   
     prime[k]=0;      
  }

  set<long long> counts;
  counts.clear();
  for(int j=A;j<=B;j++)
  {
    for(int k=j+1;k<=B;k++)
     for(int k1=P;k1<=B;k1++)
     {
        if(prime[k1]&&(j%k1==0)&&(k%k1==0))
          merge(find(j),find(k));
     }       
  }
  long long res=0;
  for(int j=A;j<=B;j++)
  {
    int hh=find(j);
    if(counts.find(hh)==counts.end())
    {
     res++;
     counts.insert(hh);
    }
  }
  cout<<res<<endl;
 }
}
