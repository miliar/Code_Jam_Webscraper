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

#define stringswap(swstingA, swstringB) swstringA.swap(swstringB) //to swap string

#define present(container, element) (container.find(element) != container.end()) //to check whether a element is in a set or a map
#define cpresent(container, element) (find(all(container),element) != container.end()) //to check whether  a element is in container like vector

#define CLR(x,v) memset(x,v,sizeof(x)) //memset

#define print(x) cout<<#x<<" is "<<x<<endl;//for printing
#define sz(a) int((a).size()) 
#define pb push_back 
#define vi vector<int> 
#define vvi  vector<vi> //2D string 
#define ii pair<int,int> 
#define mp(typeA,typeB)  make_pair<typeA,typeB> //maing pair

//macros for limits

#define MAX 1123456
#define LLI long long int
#define ULLI unsigned long long int

using namespace std;

void preprocess()
{
}
char A[5][5];
bool check(char C)
{
   int countc=0,countt=0;
   for(int i=0;i<4;i++)
   {
      countc=0;countt=0;
      for(int j=0;j<4;j++)
      {
	 if(A[i][j]==C)
	    countc++;
	 if(A[i][j]=='T')
	    countt++;
      }
      if(countc+countt==4)
	 return true;
   }
   for(int i=0;i<4;i++)
   {
      countc=0;countt=0;
      for(int j=0;j<4;j++)
      {
	 if(A[j][i]==C)
	    countc++;
	 if(A[j][i]=='T')
	    countt++;
      }
      if(countc+countt==4)
	 return true;
   }
   countc=0;countt=0;
   for(int i=0,j=0;i<4;i++,j++)
   {
      if(A[j][i]==C)
	 countc++;
      if(A[j][i]=='T')
	 countt++;
   }
   if(countc+countt==4)
      return true;
   countc=0;countt=0;
   for(int i=0,j=3;i<4;i++,j--)
   {
      if(A[j][i]==C)
	 countc++;
      if(A[j][i]=='T')
	 countt++;
   }
   if(countc+countt==4)
      return true;
   return false;
}
bool isempty()
{
   for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
	 if(A[i][j]=='.')
	    return true;
   return false;
}
int main()
{
   preprocess();
   int test;
   scanf("%d",&test);
   for(int cas=1;cas<=test;cas++)
   {
      printf("Case #%d: ",cas);
      for(int i=0;i<4;i++) scanf("%s",A[i]);
      if(check('X')) printf("X won\n");
      else if(check('O')) printf("O won\n");
      else if(isempty()) printf("Game has not completed\n");
      else printf("Draw\n");
   }
   return 0;
}


