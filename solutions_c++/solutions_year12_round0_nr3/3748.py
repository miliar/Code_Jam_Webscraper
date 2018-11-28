/* Author :  Jay Pandya */

// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>

//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>

//Macros
#define all(c) c.begin(),c.end() //all element in container c

#define tr(container, it) \
   for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //to iterate in container

#define stringswap(swstingA, swstringB) \
   swstringA.swap(swstringB) //to swap string

#define present(container, element) (container.find(element) != container.end()) //to check whether a element is in a set or a map
#define cpresent(container, element) (find(all(container),element) != container.end()) //to check whether  a element is in container like vector

#define print(x) cout<<#x<<" is "<<x<<endl;//for printing
#define sz(a) int((a).size()) 
#define pb push_back 
#define vi vector<int>; 
#define vvi  vector<vi>; //2D string 
#define ii pair<int,int>; 
#define mp(typeA,typeB)  make_pair<typeA,typeB> //maing pair

//macros for limits

#define MAX 1123456
#define LLI long long int
#define ULLI unsigned long long int

using namespace std;

void preprocess()
{
}
int func(int i,int A,int B)
{
   string a = "";
   int i1 = i;
   while(i>0)
   {
      a+=((i%10)+'0');
      i/=10;
   }
   string a1(a.rbegin(),a.rend());
   a = a1;
   int count = 0;
   while(1)
   {
      a+=a[0];
      a.erase(a.begin());
      if(atoi(a.c_str())==i1)
	 break;
      if(a[0]!='0')
      if(atoi(a.c_str())>=A && atoi(a.c_str())<=B)
      {
	 count++;
      }

   }
   return count;
}
int main()
{
   preprocess();
   int test;
   scanf("%d",&test);
   for(int i=1;i<=test;i++)
   {   
      printf("Case #%d: ",i);
      int A,B;
      long long int ans = 0;
      scanf("%d %d",&A,&B);
      for(int j=A;j<=B;j++)
	 ans+=func(j,A,B);
      printf("%lld\n",ans/2);
   }
   return 0;
}


