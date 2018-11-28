#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>



/* Code for magica

Use of base array*/
char base[8]={'Q','W','E','R','A','S','D','F'} ;
FILE *fp;

int isbase(char c)
{
    for(int i=0;i<8;i++)
    {
        if(c==base[i])
        return 1;
    }
    return 0;
}
char temp[101];
int tempc=0;
int tempmax=0;
char rel[37][3];
char op[37][2];
int opc=0;
int relcnt=0;
void init()
{
    for(int i=0;i<37;i++)
    {
        rel[i][0]=NULL;
        rel[i][1]=NULL;
        rel[i][2]=NULL;
        op[i][0]=NULL;
        op[i][1]=NULL;
    }
    opc=0;
    relcnt=0;
    tempc=0;
    tempmax=0;
    for(int j=0;j<101;j++)
    temp[j]=NULL;
}
void addrel()
{char str[20];
int k=0;
for(k=0;k<relcnt;k++)
{

  fscanf(fp,"%s",str);
rel[k][0]=str[0];
rel[k][1]=str[1];
rel[k][2]=str[2];
}
}
void addop()
{   int k=0;
    char str[20];
    for(k=0;k<opc;k++)
    { fscanf(fp,"%s",str);
      op[k][0]=str[0];
      op[k][1]=str[1];
    }
}
void hasrel()
{
    int k=0;
    char c=temp[tempc];
    int flag=0;
    for(k=0;k<relcnt;k++)
    {
        if(rel[k][0]==c)
        {flag=2;
            break;
        }
        if(rel[k][1]==c)
        {flag=1;
        break;
        }
    }
    if(flag!=0)
    {flag=flag-1;
    if(temp[tempc-1]==rel[k][flag])
    {
        temp[tempc--]=NULL;
        temp[tempc]=rel[k][2];
    }
    }
}
void hasop()
{
    int k=0;
    char c=temp[tempc];
    int flag=0;
    for(k=0;k<opc;k++)
    {
        if(op[k][0]==c)
        {flag=2;
            break;
        }
        if(op[k][1]==c)
        {flag=1;
        break;
        }
    }
    if(flag!=0)
    {flag=flag-1;
    for(int i=0;i<tempc;i++)
    {
        if(temp[i]==op[k][flag])
        {
            //cout<<"entering";
            for(int j=0;j<tempc;j++)
            temp[j]=NULL;

            tempc=-1;
            return;
        }
    }
    }
}
void output()
{
    for(int i=0;i<opc;i++)
    cout<<op[i]<<endl;
    for(i=0;i<relcnt;i++)

    cout<<rel[i]<<endl;
    cout<<endl;
}

int main()
{int n;
fp=fopen("google\\input.txt","r");

FILE* fd=fopen("google\\abc.txt","w");
char str[20];
fscanf(fp,"%s",str);
n=atoi(str);
//cin>>n;
for(int i=1;i<=n;i++)
{
    char c;
    init();
    //char str[20];
fscanf(fp,"%s",str);
relcnt=atoi(str);
//cout<<"Stsrt char"<<relcnt<<endl;
 //cin>>relcnt;
 addrel();
 fscanf(fp,"%s",str);
opc=atoi(str);
//cout<<"second char"<<opc<<endl;

 //cin>>opc;
 addop();
 fscanf(fp,"%s",str);
tempmax=atoi(str);

 //cin>>tempmax;
 int cnt=1;
 char bak[50];
 fscanf(fp,"%s",bak);
 //cin>>c;
 temp[tempc++]=bak[0];
 while(cnt<tempmax)
 {//cout<<cnt<<temp<<endl;
 //fscanf(fp,"%c",&c);
 //    cin>>c;
     temp[tempc]=bak[cnt];
     if(isbase(bak[cnt]))
     {
         hasrel();
         hasop();

     }
     tempc++;
     cnt++;
 }
//output();
fprintf(fd,"Case #%d: [",i);
 for(int l=0;l<tempc-1;l++)
 {
     fprintf(fd,"%c, ",temp[l]);
 }
 if(tempc>0)
 fprintf(fd,"%c]\n",temp[tempc-1]);
 else
 fprintf(fd,"]\n");

}
fclose(fp);
fclose(fd);
 return 0;
}


