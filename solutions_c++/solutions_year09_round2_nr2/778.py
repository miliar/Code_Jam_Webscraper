#include<iostream>
#include<string>   
using namespace std;
main()
{
 long int a,b,T,i,j,k,l;
 string N;
  cin>>T;
 for(i=1;i<=T;i++)
 {
    cin>>N;
    int fl=0;
    for(int j=0;j<N.size()-1;j++)
    {
     if(N[j+1]>N[j])
     {fl=1;break;}
    }
    if(fl==0)
    N="0"+N;
    next_permutation(N.begin(),N.end());
    
    
    cout<<"Case"<<" #"<<i<<": "<<N<<endl;                                              
 }
 
}
