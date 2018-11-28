#include<stdio.h>
#include<iostream.h>
int main()
{
char an[]="yhesocvxduiglbkrztnwjpfmaq";
int v;
cin>>v;
scanf("\n");
for(int i=0;i<v;i++)
{
char *ent=new char[300];

gets(ent);
int k=0;
while(ent[k]!='\0')
{
if(ent[k]!=' ')
ent[k]=an[ent[k]-97];
k++;
}
cout<<"Case # "<<i+1<<":";
puts(ent);

}
return 0;
}
