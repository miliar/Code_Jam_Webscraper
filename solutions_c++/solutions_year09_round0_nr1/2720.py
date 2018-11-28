#include<iostream>
using namespace std;
#define maxl 16
#define maxd 5001
#define maxn 501
#define b 96

int L,D,N;
bool is[maxn][maxl][30];
int out[maxn];
char word[maxd][maxl];

bool check(int i,int j)
{
 for(int k=1;k<=L;k++)
  if(!is[j][k][int(word[i][k-1]-b)]) return 0;

return 1;
}

int main()
{
 scanf("%d %d %d", &L, &D, &N);
  for(int i=1;i<=D;i++)
   cin>>word[i];
   
   char a;
  for(int i=1;i<=N;i++)
   for(int j=1;j<=L;j++){
    cin>>a;
     if(a=='(') {
      while(a!=')') {
       cin>>a;
        if(a!=')')
         is[i][j][int(a-b)]++;
         }
        }
     else is[i][j][int(a-b)]++;  
       } 

  for(int i=1;i<=D;i++) 
   for(int j=1;j<=N;j++)
    if(check(i,j))
     out[j]++;
    
  for(int i=1;i<=N;i++)
   cout<<"Case #"<<i<<": "<<out[i]<<endl;  
   
return 0;
}        
