#include<iostream>
#include<string>
using namespace std;

int L,D,N;
string arr[6000],w[6000];


int sol(string wr)
{
 int i,a=0,b=0,ans=0;  
 for(i=0;i<D;i++)
 {
              a=b=0;
              while(a<wr.size()&&b<arr[i].size())
              {
                 if(wr[a]=='(')
                 {
                   a++;
                   while(wr[a]!=')')
                   {
                     if(wr[a]==arr[i][b])break;                 
                     a++;
                   }
                   if(wr[a]==')')break;
                   b++; 
                   while(wr[a]!=')')a++;
                   a++;    
                 }
                 else
                 {
                   if(wr[a]!=arr[i][b])break;
                   a++;b++;
                 }
              
              
              }
             // cout<<wr<<" "<<arr[i]<<" "<<a<<" "<<b<<endl;
              if(a==wr.size()&&b==arr[i].size())ans++;
                 
                 
 }   
 return ans;
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-attempt0.in.out","w",stdout);
    cin>>L>>D>>N;
    int i;
    for(i=0;i<D;i++)
    cin>>arr[i];
    
    
    for(i=0;i<N;i++)
    cin>>w[i];
    
    for(i=0;i<N;i++)
    cout<<"Case #"<<i+1<<": "<<sol(w[i])<<endl;
    
    cin>>N;
    
    
    
 return 0;   
}
