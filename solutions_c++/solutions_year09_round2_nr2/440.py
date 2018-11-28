#include<iostream>
using namespace std;

char str[100];
int axis[100];
int tmp[100],size;
int n,m;
bool cmp()
{
     int i,J,k;
     
     for(i = 0;i < size;i++)
     {
      if(tmp[i] < axis[i])
      return false;
      if(tmp[i] > axis[i])
      return true;
     }
   
   return false;
}

int main()
{
    int ncase,casenum = 1;
    int i,J,k,len;
    freopen("Al.txt","w",stdout);
    scanf("%d",&ncase);
    while(ncase--)
    {
          scanf("%s",str);
          len = strlen(str);
          size = 0;
          for(i = 0;i < len;i++)
          {
              axis[size++] = str[i] - '0';
              tmp[size - 1] = axis[size - 1];
          }
          bool flag = false;
          
          do
          {
               if(cmp())
               {
                  flag = true;
                  break;
               }
          }while(next_permutation( tmp, tmp + size ) );
          printf("Case #%d: ",casenum++);
          if(flag)
          {
             for(i = 0;i < size;i++)
              printf("%d",tmp[i]);
             putchar('\n');
          }
          else
          {
              tmp[size++] = 0;
              sort(tmp,tmp + size);
              for(i = 0;i < size;i++)
               if(tmp[i])
               {
                 // printf("tmp[i] = %d\n",tmp[i]);
                  swap(tmp[i],tmp[0]);
                 break;
               }
             for(i = 0;i < size;i++)
              printf("%d",tmp[i]);
             putchar('\n');
          }                            
           
    }          
//    system("pause");           
    
    return 0;
}   
