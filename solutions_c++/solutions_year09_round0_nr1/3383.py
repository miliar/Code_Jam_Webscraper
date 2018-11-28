#include<iostream.h>
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
void main()
{
 clrscr();
 char ch;
 char str[500], strl[9],strd[9],strn[9],*strt;
 char matrix[4200][15];   //Need to check
 int i,j,k,l,d,n,t,count,temp,sl,slt;
 ifstream indata;
 ofstream outdata("A-small.out");
 indata.open("A-small.in");

indata.getline(str,500,'\n');
sl = strlen(str);
i=0;
j=0;
slt=0;
strt=str;
while(strt[i] !=' ' )
{
 strl[j]=strt[i];
 i++; j++;slt++;
}
strl[j]='\n';

l=atoi(strl);
//cout<<"l="<<l<<endl;
//getch();

j=0;i++;slt++;

while(strt[i] != ' ')
{
 strd[j]=strt[i];
 i++; j++;slt++;
}

strd[j]='\n';
d=atoi(strd);
//cout<<"d="<<d<<endl;
//getch();

j=0;i++;slt++;
while( slt < sl )
{

 strn[j]=strt[i];
 i++; j++;slt++;
}
strn[j]='\n';
n=atoi(strn);
//cout<<"n="<<n<<endl;
//getch();


strn[j]='\n';
n=atoi(strn);

temp=0;
for(i=0;i<d;i++)
{
 indata.getline(str,500,'\n');
 for(j=0;j<l;j++)
 {
 matrix[i][j]=strt[temp++];
 cout<<matrix[i][j];
 }
 cout<<endl;
 temp=0;
}

//cout<<"l="<<l<<"d="<<d<<"n="<<n<<endl;
//getch();

for(int z=0;z <n; z++)
{
 indata.getline(str,500,'\n');
count=0;
for (i=0;i<d;i++)
{
  temp=0;
  k=0;
   for(t=0;t<l;t++)
  {
   strt=str;
//    cout<<"i="<<i<<"t="<<t<<endl;
//    getch();
//    cout<<"strt[k]"<<strt[k]<<endl;
//    getch();
  if(strt[k] =='(')
   {
    while(strt[k++] != ')')
    {
      if(strt[k]==matrix[i][t])
       {
       temp++;
       while(strt[k++] != ')');
       k--;
       }
    }
   }
   else if(strt[k]==matrix[i][t])
	  {
	  temp++;
	  k++;
	  }

}
 if(temp == l)
  count++;
//  cout<<"count"<<count<<endl;
//  getch();
  }
//  cout<<"cout"<<count<<endl;
 outdata<<"Case #"<<z+1<<": "<<count<<endl;
// getch();
}

indata.close();
outdata.close();

}