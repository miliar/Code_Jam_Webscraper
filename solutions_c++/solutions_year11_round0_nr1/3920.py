# include <iostream>
# include <fstream>
# include <string.h>

using namespace std;

int i=1;
char ip[1000];

int numcalc()
{
   char num[3];
   num[2]=ip[i];
    i+=1;
    if(ip[i]>47&&ip[i]<58)
    {
     num[1]=num[2];
     num[2]=ip[i];
     i+=1;
     if (ip[i]>47&&ip[i]<58) 
     {num[0]=num[1];num[1]=num[2];num[2]=ip[i];i+=1;}
     else
     num[0]='0';
    }
    else
    { num[1]='0';num[0]='0';}
      


return ((num[2]-48)*1+(num[1]-48)*10+(num[0]-48)*100);

}
    
int main()
{
 
 int x,t=0;
 // for robot O
 int po[1000]; // coz max no. of buttons in each test case = 10
 int o=1;
 int k=0;
 int pol=0; // limit of O positions

 // for robot B
 int pb[1000];
 int b=1;
 int l=0;
 int pob=0; // limit of B positions

 char order[1000]; 
 int m=0; 
 int cnt=0;
 int tot; 
 int val;

ifstream fin("A-large (1).in");
ofstream fout("output.txt");
cnt=0;

fin.getline(ip,800);

while(fin.getline(ip,800))
{

 m=0;b=1;o=1;k=0;l=0;pob=0;pol=0;i=0;
 for(;ip[i]!=' ';i++);  
 while(i<strlen(ip))
 {
  if (ip[i]=='O'||ip[i]=='B')
  { 
   order[m]=ip[i]; 
   m+=1;
   i+=1;
  }
  else if (ip[i]>47&&ip[i]<58)
  {
   val=numcalc();
   if (order[m-1]=='O')
   { po[k]=val; k+=1;}
   else 
   {
     pb[l]=val; 
     l+=1;
   }
  }
  else
  i+=1;
 }  
 int ase,ase1,ase2;
 x=0;t=0;
 while (x<m)
 {
  //cout<<"\n\n value of t : "<<t;
  ase =0;ase1=0;ase2=0;
  if (o!=po[pol])
  {
    if (o<po[pol]&&pol<k) 
    o+=1;
    else
    o-=1;
    ase1=2;
  }
  if (b!=pb[pob]&&pob<l)
  {
   if (b<pb[pob])
   b+=1;
   else
   b-=1;
   ase2=2;
  }
  if (order[x]=='O'&&o==po[pol]&&ase1!=2)
  { ase=1;x+=1;pol+=1; }
  else if (order[x]=='B'&&b==pb[pob]&&ase2!=2)
  { ase=1;x+=1;pob+=1;}
  if (ase!=0||ase1!=0||ase2!=0)
  t+=1; 
 }
 
 cout<<"\n Case #"<<cnt+1<<": "<<t;
 fout<<"Case #"<<cnt+1<<": "<<t<<"\n";
 cnt+=1;
}
cout<<"\n";
fin.close();
fout.close();
return 0;
} 
