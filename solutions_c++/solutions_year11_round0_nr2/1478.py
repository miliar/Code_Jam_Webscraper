#include<cstdio>
#include<cstdlib>
int N,M,l,T;
char str[101],temp0,tag1[28][28],tag2[28][28];
int main()
{
    freopen("test.in","r",stdin);
    freopen("output.txt","w",stdout);
   scanf("%d",&T);
   for(int round = 1;round<=T;round++)
   {
       for(int i=0;i<28;i++)
         for(int j=0;j<28;j++)
           tag1[i][j] = 0,tag2[i][j] = 0;
       scanf("%d",&N);
       for(int i=0;i<N;i++)
       {
          scanf("%s",str); 
          tag1[str[0]-'A'][str[1]-'A'] = str[2];    
          tag1[str[1]-'A'][str[0]-'A'] = str[2];    
       }
       scanf("%d",&M);
       for(int i=0;i<M;i++)
       {
          scanf("%s",str);
          tag2[str[0]-'A'][str[1]-'A'] = 1;
          tag2[str[1]-'A'][str[0]-'A'] = 1;
       }
       scanf("%d",&N);
       l=0;
       for(int i=0;i<N;i++)
       {
          scanf(" %c",&temp0);        
          if(l!=0)     
          {
             if(tag1[temp0-'A'][str[l-1]-'A'] != 0)
                str[l-1] = tag1[temp0-'A'][str[l-1]-'A'];
             else
             {
                for(int j=0;j<l;j++)
                {
                  if(tag2[temp0-'A'][str[j]-'A'] == 1)
                     {l = 0;goto ou1;}        
                }    
                str[l++] = temp0;
             }             
             ou1:;
          }
          else
             str[l++] = temp0;
       }
       printf("Case #%d: [",round); 
       if(l!=0)
         printf("%c",str[0]);
       for(int i=1;i<l;i++)
         printf(", %c",str[i]);
       printf("]\n");//printf("%d",'Z'-'A');
   }//system("pause");
   return 0;    
}
