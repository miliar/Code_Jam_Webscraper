#include <iostream>
#include <vector>	
#include <algorithm>
#include <cmath>
using namespace std;

int getdigits(int x)  
{  
    return (x < 10 ? 1 :   
        (x < 100 ? 2 :   
        (x < 1000 ? 3 :   
        (x < 10000 ? 4 :   
        (x < 100000 ? 5 :   
        (x < 1000000 ? 6 :   
        (x < 10000000 ? 7 :  
        (x < 100000000 ? 8 :  
        (x < 1000000000 ? 9 :  
        10)))))))));  
}

bool check(vector <int> one,vector <int> two,int a,int b)
{
 int l;
 for(l=0;l<one.size();l++)
 {
  if(one[l]==a)
  if(two[l]==b)
    return 0;
  }
  return 1;
}

int main()
{
 int tc,i,j;cin>>tc;
 for(i=0;i<tc;i++)
  {
   int a,b,ans=0;cin>>a>>b;
   vector <int> one,two;
   for(j=a;j<=b;j++)
   {
    int temp = j,k;
     for(k=10000;k>=10;k=k/10)
     {
      int div = temp/k;
      int dg = getdigits(div);
      int onother = ((temp%k)*(pow(10,dg)))+div;
      if(div)
      if(onother<=b)
       if(temp%k!=temp%(k/10))	//not zero front
      { 
         if(temp!=onother) // not the same element
        {
          if(onother>= a && onother <=b)
           if(check(one,two,temp,onother))	
          {   
              ans++;
              one.push_back(temp);
              one.push_back(onother);
	      two.push_back(onother);
              two.push_back(temp);
            }
        }
      }
       
     }
    }
   cout<<"Case #"<<i+1<<": "<<ans<<"\n";
  }

}
 
