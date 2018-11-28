#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cmath>
#include<algorithm>



using namespace std;



int assigns[5000];
int next[5000];


int main()
{
 int N;
 cin>>N;
 for(int i=0;i<N;i++)
 {
  cout<<"Case #"<<i+1<<": ";
  long long K,n;
  cin>>K;
  
  for(int j=0;j<K;j++)
   assigns[j]=-1;

  for(int j=0;j<K;j++)
   next[j]=(j+1)%K;   
     
  long long cur=0;
  long long count=0;
  int last=-1;
  for(int j=0;j<K;)
  {
   if(assigns[cur]==-1)
   {
     
     if(count==j)
     {
      assigns[cur]=j;
      count=0;
      j++;
     }
     else
     {
       count++; 
       if(last!=-1)
         next[last]=cur;
       last=cur;
     }      
   }       
   cur=next[cur];
  }
  
  long long N;
  cin>>N;
  for(int j=0;j<N;j++)
  {
    int ind;
    cin>>ind;
    cout<<assigns[ind-1]+1<<" ";        
  }
  cout<<endl;
 }
}
