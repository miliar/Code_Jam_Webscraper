#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> s;
int main()
{
int i,x,notc,n,k,p,l,temp;
scanf("%d",&notc);
for(x=0;x < notc ;x++)
{
 scanf("%d %d %d",&p,&k,&l);   
 s.clear();
 for(i=0;i<l;i++)
                 {
                 scanf("%d",&temp);
                 s.push_back(temp);
                 }
 int j=1,count=0;
 long long sum=0;
 sort( s.begin(), s.end() );
 //printf("\n==%d==\n",s.size());
for( int i= s.size()-1 ; i >=0 ;i-- )
     {
     if(count==k){j++;count=0;} 
     sum = sum  + j*s[i];
     count++;
     }
cout<<"Case #"<<x+1<<": "<<sum<<"\n";}
//system("pause");
}
