#include <iostream>

using namespace std;

char dict[5001][16];
char input[17][1000];
char tmp[1000];
int l, d, n;

bool find(char* str)
{
 int i, j; 
 int flag ;

 for(i=0; i<l; i++)
 { 
  flag = 0;
  for(j=0; input[i+1][j]; j++)
  {
   if(input[i+1][j]==str[i])
   {
    flag = 1;
    break;
   }
  }
  if(!flag)
   return false;
 }
 return true;
}

int main()
{
 freopen("A-large.in", "r", stdin);
 freopen("22.txt", "w", stdout);
 int i, j;
 int t1, t2;
 int ans;
 int flag;
 while(scanf("%d %d %d", &l, &d, &n)!=-1)
 {
  getchar();
  for(i=1; i<=d; i++)
   gets(dict[i]);

  for(i=1; i<=n; i++)
  { 
   memset(input, 0, sizeof(input));
   gets(tmp);
   t1 = 1;
   t2 = 0;
   flag = 0;
   for(j=0; tmp[j]!=0; j++)
   {
    if(!flag)
    {
     if(tmp[j]!='(' && tmp[j]!=')')
      input[t1++][0] = tmp[j];
     else
     {
      flag = 1;
      t2 = 0;
     }
     
    }
    else
    {
     if(tmp[j]!='(' && tmp[j]!=')')
      input[t1][t2++] = tmp[j];
     else
     {
      flag = 0;
      t1++;
     }
    }
    
   } 
   
  // for(j=1; j<=l; j++)
  // {
  //  printf("%s\n", input[j]);
  // }
  // system("pause");
   ans = 0;
   for(j=1; j<=d; j++)
   {
    if(find(dict[j]))
     ans++;
   }
   printf("Case #%d: %d\n", i, ans);
  
  }
 }
 //system("pause");
 return 0;
}


