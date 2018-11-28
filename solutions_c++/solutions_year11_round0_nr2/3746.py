#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
void sort(char str[200][4],int n)
{
    int i,j;
    char s[4],x[4];
    for(i=1;i<n;i++)
    {
        strcpy(x,str[i]);
        for(j=i-1;j>=0;j--)
        {
            if(strcmp(str[j],x)>0)
            {
                strcpy(str[j+1],str[j]);
            }
            else
                break;
        }
        strcpy(str[j+1],x);
    }
}
char MIN(char x,char y)
{
    return((x<y)?x:y);
}
char MAX(char x,char y)
{
    return((x>y)?x:y);
}
int main()
{
    int C,D,T,N,i,j,k,x,l,flag;
    char str1[200][4],str2[100][4],str3[150],str4[200],min,max,*temp;
    scanf("%d",&T);
    for(x=0;x<T;x++)
    {
        scanf("%d",&C);
        for(i=0;i<C;i++)
        {
            scanf("%s",str1[i]);
            min=MIN(str1[i][0],str1[i][1]);
            max=MAX(str1[i][0],str1[i][1]);
            str1[i][0]=min;
            str1[i][1]=max;
            str1[i][3]='\0';
        }
        sort(str1,C);
        scanf("%d",&D);
        for(i=0;i<D;i++)
        {
            scanf("%s",str2[i]);
            min=MIN(str2[i][0],str2[i][1]);
            max=MAX(str2[i][0],str2[i][1]);
            str2[i][0]=min;
            str2[i][1]=max;
            str2[i][2]='\0';
        }
        sort(str2,D);
        //cout<<str2[0]<<endl;
        scanf("%d",&N);
        scanf("%s",str3);
        k=0;
        str4[0]=str3[0];
        for(i=1;i<N;i++)
        {
            flag=0;
            min=MIN(str4[k],str3[i]);
            max=MAX(str4[k],str3[i]);
            for(j=0;j<C;j++)
            {
                
                if(min==str1[j][0])
                {
                    if(max==str1[j][1])
                    {
                        str4[k]=str1[j][2];
                        flag=1;
                        break;
                    }
                    else if(max>str1[j][1])
                    {
                        break;
                    }
                }
                else if(min>str1[j][0])
                {
                    break;
                }
                
            }
            if(flag==0)
            {
                for(j=0;j<D;j++)
                {
                    temp=strrchr(str2[j],str3[i]);
                    if(temp!=NULL)
                    {
                        //cout<<str2[j]-temp +1<<endl;
                        for(l=0;l<=k;l++)
                        {
                            if(str2[j][str2[j]-temp +1]==str4[l])
                            {
                                k=0;
                                str4[k]=str3[i+1];
                                i++;
                                flag=-1;
                                break;
                            }
                        }
                        if(flag==-1)
                        {
                            break;
                        }
                    }
                    
                }
            }
            if(flag==0)
            {
                str4[++k]=str3[i];
            }
            str4[k+1]='\0';
            //cout<<str4<<i<<k<<endl;
        }
        printf("Case #%d: [",x+1);
        for(i=0;i<k;i++)
        {
            printf("%c, ",str4[i]);
        }
        printf("%c]\n",str4[k]);
    }
}
