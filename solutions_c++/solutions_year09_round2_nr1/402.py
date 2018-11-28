#include<iostream>
using namespace std;
const int MAXN = 1000;

char str[MAXN][MAXN];
int child[MAXN][2];

char name[MAXN][MAXN];
double p[MAXN];

int L,A,n;
int Q;
int Len[MAXN];
struct node
{
       char str[1000];
}a[MAXN];
int size;
char ss[1000];
int main()
{
    int i,J,k,len,cur;
    int down;
    int cnt1,cnt2;
    double tmp,carry;
    freopen("B.txt","w",stdout);
    int ncase,casenum = 1;
    scanf("%d",&ncase);
    while(ncase--)
    {
          cin>>L;
          for(i = 1;i <= L;i++)
           p[i] = 0.0000;
          memset(name,0,sizeof(name));
          memset(child,0,sizeof(child)); 
          for(i = 1;i <= L;i++)
          {
              scanf("\n");
              gets(str[i]);
              len = strlen(str[i]);
              Len[i] = len;
              tmp = 0.0000;
              for(J = 0;J < len;J++)
              {
                  if(isdigit(str[i][J]))
                  {
                     while(J < len && isdigit(str[i][J]))
                     {
                           p[i] = p[i] * 10.000 
                           + str[i][J] - '0';
                         J++;
                     }
                     carry = 1.0000;
                     J++;
                     while(J < len && isdigit(str[i][J]))
                     {
                           carry *= 0.1;
                           tmp = tmp + carry * (str[i][J] - '0');
                         J++;  
                     }
                     p[i] += tmp;
                  }
                  
                  else if(isalpha(str[i][J]))
                  {
                       cur = 0;
                       while(J < len && isalpha(str[i][J]))
                       {
                             name[i][cur++] = str[i][J];
                          J++;
                       }
                      name[i][cur] = '\0';
                  }       
                                      
              }                              
          }
          for(i = 1;i <= L;i++)
          {
              if(name[i][0] == '\0') continue;
              
              cnt1 = 0;
              for(J = i + 1;J <= L;J++)
              {
               for(k = 0;k < Len[J];k++)
               {
                if(str[J][k] == '(')
                cnt1++;
                if(str[J][k] == ')')
                cnt1--;
               }
               if(cnt1==0) break;
              }
             child[i][0] = i + 1;
             child[i][1] = J + 1;
          }      
          /*for(i = 1;i <= L;i++)
          printf("%lf ",p[i]);
          putchar('\n');
          for(i = 1;i <= L;i++)
          printf("%s\n",name[i]);
          putchar('\n');
          for(i = 1;i <= L;i++)
           printf("%d %d   ",child[i][0],child[i][1]);
          putchar('\n'); */
          printf("Case #%d:\n",casenum++);
          cin>>n;
          while(n--)
          {
          scanf("%s",ss);
          cin>>size;
          for(i = 0;i < size;i++)
           cin>>a[i].str;
          double tot = 1.0000;
          for(i = 1;i <= L;)
          {
              tot *= p[i];
             // printf("tot = %lf p[i] = %lf i = %d\n",tot,p[i],i);
              if(name[i][0] == '\0') break;
              bool flag = false;
              for(J = 0;J < size;J++)
               if(strcmp(a[J].str,name[i]) == 0)
               {
                  flag = true;
                  break;
               }
            //  printf("flag = %d\n",flag);
              if(flag)
              {
              i = child[i][0];
              }
              else
              {
              i = child[i][1];                               
              }
          }
          printf("%.7lf\n",tot); 
          }
                      
    }          
   // system("pause");
    return 0;
}
