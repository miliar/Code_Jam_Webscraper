#include<stdio.h>
#include<vector>
using namespace std;
int main()
{
char comb[3];
char opp[2];
char list[10];
int c,d,n;
char ch;
int test,tc;
scanf("%d",&test);
for(tc=1;tc<=test;tc++)
{


scanf("%d",&c);
if(c==1)
{
scanf("%c",&ch);
scanf("%c",&comb[0]);
scanf("%c",&comb[1]);
scanf("%c",&comb[2]);
}
scanf("%d",&d);
if(d==1)
{
scanf("%c",&ch);
scanf("%c",&opp[0]);
scanf("%c",&opp[1]);
}
scanf("%d",&n);
scanf("%c",&ch);

int size=0;
scanf("%c",&list[0]);
for(int i=2;i<=n;i++)
{
scanf("%c",&ch);
if(c==1){
if(size>=0){
if(((list[size]==comb[0])&&ch==comb[1])||((list[size]==comb[1])&&ch==comb[0])){
list[size]=comb[2];
continue;
}}
}
if(d==1)
{
char flag=ch;
for(int j=0;j<=size;j++)
{
if(list[j]==opp[0]||list[j]==opp[1])
flag=list[j];
}
if((flag==opp[0]&&ch==opp[1])||(flag==opp[1]&&ch==opp[0])){
size=-1;
continue;
}
}

list[++size]=ch;
}
printf("Case #%d: ",tc);
printf("[");
for(int i=0;i<=size;i++){
printf("%c",list[i]);
if(i!=size)
printf(", ");
}
printf("]");

printf("\n");
}
}

