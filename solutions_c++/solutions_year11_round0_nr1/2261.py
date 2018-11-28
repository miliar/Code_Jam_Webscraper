#include<cstdio>
#include<conio.h>
#include<iostream>
#include<ctype.h>

using namespace std;

int i=0,j=0,k=0;
int O[110][110];
int B[110][110];
char Baton[110][110];
int posO=1,posB=1;
int t;

int n1[100];
int n2[100];

void move(char A,int count)
{
     if(A=='B')
     {
               if(posB<B[count][j])posB++;
               else if(posB>B[count][j])posB--;
     }
     
     if(A=='O')
     {
               if(posO<O[count][i])posO++;
               else if(posO>O[count][i])posO--;
     }

}

void press(char A,int count)
{
     if(A=='B')
     {
               if(posO!=O[count][i])move('O',count);
               j++;
               k++;
     }
     
     if(A=='O')
     {
               if(posB!=B[count][j])move('B',count);
               i++;
               k++;
     }

}

int main()
{

FILE *fd,*fd3;
char *str,*token;
void *fd1;
char string[30000];
int count=0;

fd=fopen("input.in","r");
fd3=fopen("output.out","w");
    
fd1=fgets(string,30000,fd);

int i1,j1,k1;
i1=0,j1=0,k1=0;

while(fd1!=NULL)
    {
        if(count==0)t=atoi(string);
        else
        {
             i1=0;k1=0;j1=0;
             for(str=string,i=0;;str=NULL,i++)
                  {
                                 
                                 token=strtok(str," \n");
                                 if(token==NULL)break;
                                 
                                 if(i!=0)
                                 {
                                 if(isalpha(token[0]))Baton[count-1][i1++]=token[0];
                                 else if(isdigit(token[0]))
                                 {                                 
                                          if(Baton[count-1][i1-1]=='O')O[count-1][j1++]=atoi(token);
                                          else if(Baton[count-1][i1-1]=='B')B[count-1][k1++]=atoi(token);
                                 }
                                 }
                                 
                  }
                  Baton[count-1][i1]='\0';
                  n1[count-1]=j1;
                  n2[count-1]=k1;
        }     
         
        fd1=fgets(string,30000,fd);
        count++;
}
fclose(fd);



int time;
int f;


count =0;

while(count<t)
{
i=0,j=0,k=0;f=1;
posO=1;posB=1;
for(time=1;;time++)
{
                  
                   f=1;
        
                   if((f==1)&&(Baton[count][k]=='O')&&(posO==O[count][i]))
                   {
                                                   press('O',count);//cout<<time<<" "<<"press O"<<endl;
                                                   f=0;
                   }
                   if((f==1)&&(Baton[count][k]=='B')&&(posB==B[count][j]))
                   {
                                                   press('B',count);//cout<<time<<" "<<"press B"<<endl;
                                                   f=0;
                   }
                   
                   if(f!=0)
                   {
                           if(posB!=B[count][j])move('B',count);//cout<<time<<" "<<"move B"<<endl;}
                           if(posO!=O[count][i])move('O',count);//cout<<time<<" "<<"move O"<<endl;}
                   }


if(k==strlen(Baton[count]))break;

}
fprintf(fd3,"Case #%d: %d\n",count+1,time);
count++;
}
fclose(fd3);

//getch();
}
