#include<cstdio>
#include<iostream>
#include<conio.h>
#include<ctype.h>
#include<cstring>

struct combo
{
       char c[40][5];
};

struct opp
{
       char o[30][5];
};

combo test1[110];
opp test2[110];
int nc[110];
int nd[110];
int nn[110];
char input[110][110];
char o[200];
int t;

using namespace std;

int combine(int i,int j)
{
    char a,b;
    int k,p;
    a=input[i][j];
    b=input[i][j-1];
    for(k=0;k<nc[i];k++)
    {
                        if(((test1[i].c[k][0]==a)&&(test1[i].c[k][1]==b))||((test1[i].c[k][0]==b)&&(test1[i].c[k][1]==a)))
                        {
                                     input[i][j-1]=test1[i].c[k][2];
                                     for(p=j;p<strlen(input[i]);p++)
                                     input[i][p]=input[i][p+1];
                                     return(j-1);
                        }
    }
    return j;
}

int oppose(int i,int j)
{
    int k,p,q;
    char a=input[i][j];
    char b;
    for(k=0;k<nd[i];k++)
    {
                       for(p=0;p<j;p++)
                       {
                                       b=input[i][p];
                                       if(((test2[i].o[k][0]==a)&&(test2[i].o[k][1]==b))||((test2[i].o[k][0]==b)&&(test2[i].o[k][1]==a)))
                                       {
                                                                                                   
                                                  for(q=j+1;q<=strlen(input[i]);q++)
                                                  input[i][q-j-1]=input[i][q];
                                                  input[i][q-j-1]='\0';
                                                  return 0;
                                                  
                                       }
                       }
    }
    return j;
}                                     

int main()
{
 
char string[1000];
    
FILE *fd1,*fd2;
fd1=fopen("input.in","r");
fd2=fopen("output.out","w");

int count=0,i,j,k;
char *str,*token;
char c1;
void *fd;

fd=fgets(string,1000,fd1);

while(fd!=NULL)
{
        if(count==0)
        {
                    t=atoi(string);
        }
        else
        {
            j=0,k=0;
            for(i=0,str=string;;str=NULL)
            {
                                         token=strtok(str," \n");
                                         if(token==NULL)break;
                                         
                                         if(isdigit(token[0]))
                                         {
                                                             if(i==0)nc[count-1]=atoi(token);
                                                             else if(i==1)nd[count-1]=atoi(token);
                                                             else if(i==2)nn[count-1]=atoi(token);
                                                             i++;
                                         }
                                         
                                         else
                                         {
                                             if(i==1)
                                             {
                                                                             sprintf(test1[count-1].c[j],"%s",token);
                                                                             j++;                                                                            
                                             }
                                             else if(i==2)   
                                             {
                                                                          sprintf(test2[count-1].o[k],"%s",token);k++;
                                             }
                                             else if(i==3)
                                             sprintf(input[count-1],"%s",token);
                                             
                                             
                                         }
            }
        }
count++;
fd=fgets(string,1000,fd1);

}
fclose(fd1);
int f;
for(i=0;i<t;i++)
{
                j=1;
                while(input[i][j]!='\0')
                {
                                    j=combine(i,j);
                                    //cout<<j<<" "<<strlen(input[i])<<" "<<input[i]<<endl;
                                    j=oppose(i,j);
                                    //cout<<j<<input[i]<<endl;
                                    j++;
                }
                o[0]='[';f=0;
                for(j=0;j<strlen(input[i]);j++)
                {
                      o[3*j+1]=input[i][j];
                      o[3*j+2]=',';
                      o[3*j+3]=' ';
                      f=3*j+1;
                }
                o[++f]=']';
                o[++f]='\0';
                //cout<<o<<endl;
                //cout<<input[i]<<endl;
                               
                fprintf(fd2,"Case #%d: %s\n",i+1,o);                    
               
}
 
fclose(fd2);
    
}                   


