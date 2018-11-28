#include<iostream>
using namespace std;
const int MAXN = 6000;
const int MAXLEN = 120;
char str[MAXN][MAXLEN];
char s[MAXLEN * 10000];
int L,D,n,len;
bool ok(const int id)
{
     int i,J,k;
     int p = 0;
     bool flag;
     for(i = 0;i < len;i++,p++)
     {
         if(s[i]=='(')
         {
            flag = false;          
            for(J = i + 1;J < len;J++)
             if(s[J] == ')')
             break;
            for(k = i + 1;k < J;k++)
             if(s[k] == str[id][p])
             {
                flag = true;
                break;
             }
            if(flag == false) return false;
          i = J;
         }
         else if(s[i] != str[id][p])
          return false;
     }
   return true;
}                          
int main()
{
    int i,J,k,cnt;
    int casenum = 1;
    freopen("A.txt","w",stdout);
    scanf("%d%d%d",&L,&D,&n);
    for(i = 0;i < D;i++)
      scanf("%s",str[i]);
    for(casenum = 1;casenum <= n;casenum++)
    {
        scanf("%s",s);
        len = strlen(s);
        cnt = 0;
        for(i = 0;i < D;i++)
         if(ok(i))
         cnt++;
        printf("Case #%d: %d\n",casenum,cnt);  
    }           
   // system("pause");   
    return 0;
}
