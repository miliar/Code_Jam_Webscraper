#include <stdlib.h>
#include <stdio.h>

int match(char ** s, int d, int l, char * pattern)
{
    int count = 0;
    int i,j;
    int index;
    
    for(i=0;i<d;i++)
    {
                    index = 0;
                    for(j=0;j<l;j++)
                    {
                                    if(pattern[index]=='('&&pattern[index]!='\0')
                                    {
                                                           index++;
                                                           while(pattern[index]!=')')
                                                           {
                                                                                         if(pattern[index]==s[i][j])   
                                                                                         {
                                                                                                                   while(pattern[index]!=')')
                                                                                                                        index++;
                                                                                                                   if(pattern[index+1]=='\0')
                                                                                                                       count ++;
                                                                                                                   if(pattern[index]==')')
                                                                                                                       index ++;
                                                                                                                   break;
                                                                                         }
                                                                                         else
                                                                                              index++;
                                                                                         
                                                           }
                                                           if(pattern[index+1]=='\0')
                                                                break;
                                    }
                                    else if(pattern[index]==s[i][j])
                                    {
                                         index++;
                                         if(pattern[index]=='\0')
                                        {
                                             count++;
                                             break;
                                        }
                                    }
                                    else if(pattern[index] != s[i][j])
                                         break;
                    }
    }
    return count;                                                        
}

int main()
{
    freopen("A-small-attempt1.in","rt",stdin);
    freopen("A-small-attempt1.out","wt",stdout);
    
    int l,d,n;
    int i,j;
    char ** str;
    char pattern[226];
    
    scanf("%d%d%d",&l,&d,&n);
    
    str = (char **)malloc(sizeof(char *)*d);
    for(i=0;i<d;i++)
        str[i] = (char *)malloc(sizeof(char)*(l+1));
    
    for(i=0;i<d;i++)
        scanf("%s",str[i]);
        
    //for(i=0;i<d;i++)
//        printf("%s",str[i]);
        
    for(i=0;i<n;i++)
    {
                    scanf("%s",pattern);
                    j=match(str,d,l,pattern);
                    printf("Case #%d: %d\n",i+1,j);
    }
        
    //system("pause");
    
}
