#include<stdio.h>
int main()
{
//   char str1[26]= {'a=y','b=h','c=e','d=s','e=o','f=c','g=v','h=x','i=d','j=u','k=i','l=g','m=l','n=b','o=k','p=r','q=z','r=t','s=n','t=w','u=j','v=p','w=f','x=m','y=a','z=q'} 
   char str1[26]= {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char str[105]="acd";
    char q;
    int t,i,j;
    scanf("%d",&t);
    for(j=0;j<=t;j++)
    {
              gets(str);
              if(j!=0)
              {
                      printf("Case #%d: ",j);
                      
                      for(i=0;str[i]!='\0';i++)
                      {
                                          if(str[i]!=' ')
                                          str[i]=str1[str[i]-'a'];
                                          printf("%c",str[i]);
                      }
                                          printf("\n");
              }
    
    }
//    scanf("%d",&t);
                                  return 0;
}
                                  
              
