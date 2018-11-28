#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<bitset>


using namespace std;

long long unsigned int t,n,k;



int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   
   cin>>t;
   string ans;
   for(int prob=0;prob<t;prob++)
   {
           cin>>n>>k;
           k++;
           if(k%(1<<n)==0)
           ans="ON";
           else
           ans="OFF";
           
           printf("Case #%d: %s\n",prob+1,&ans[0]);
   }

   //system("pause");
   return 0;

}
