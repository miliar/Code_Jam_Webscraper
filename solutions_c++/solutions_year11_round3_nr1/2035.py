# include <iostream>
# include <fstream>
# include <stdlib.h>
# include <string.h>
# include <math.h>
using namespace std;

//int y=0;
//int temp[2][300];
//int sum,x,st,i,j;

/*
void numcalc(char num[])
{
 int i=0,j=0,k=0;
 for(;k<strlen(num);k++)
 {
  if (num[k]==' ')
  {temp[i][j]=-1;i++;j=0;}
  else
  temp[i][j++]=num[k]-48;
 } 
 for(i=0;i<2;i++)
  {
    for(j=0;temp[i][j]!=-1;j++)
    {
    cout<<temp[i][j];
 //   exit(0);
    }
    cout<<"\n";
  }
  


 sum=0;
  i++;
  do
  {
   temp[j]=num[i]-48;
   j++;
   i++;
  }
  while(num[i]>47&&num[i]<58);
  i-=1;
  for(x=0;x<i;x++)
  cout<<temp[x];
 exit(0);
  for(x=i;x>-1;x--)
  
  sum+=pow(10,x-i)*temp[x];
i+=1;
return sum;
}

}
*/


int main()
{
 
 ifstream fin("A-small-attempt0.in");
 char name[200][200],num[30];
 char case1[3];
 int f,start,cases=0,r,c,i=0,j=0,k;
 fin.getline(case1,3);
 cases=10*(case1[0]-48)+case1[1]-48;
 //cout<<cases;
 //exit(0);
 ofstream fout("output.txt");
 for(start=0;start<cases;start++)
 {
 f=0;
 // i=-1;j=0;sum=0;
 fin.getline(num,800);
 //cout<<"\n\n line read @ start ="<<start;
 //cout<<num;
 r=num[0]-48;
 //cout<<r;
// exit(0);
  

c=num[2]-48;
// x++;
// cout<<"\n after parsing nums"; 
//cout<<"\n"<<r<<" "<<c;
 //exit(0);
 for(i=0;i<r;i++) 
 fin.getline(name[i],800);
 //fin.close();
/*
 for(j=0;j<r;j++)
 {
  for(k=0;k<c;k++)
  cout<<name[j][k];
  cout<<"\n";
 }
exit(0);
*/
 for(j=0;j<r;j++)
 {
  for(k=0;k<c;k++)
  {
   if(name[j][k]=='#')
   {
    if (name[j][k+1]=='#'&&name[j-1][k]=='#'&&name[j-1][k+1]=='#')
    {
     name[j][k]='\\';name[j][k+1]='/';name[j-1][k]='/';name[j-1][k+1]='\\';
    }
   }
  }
 }
  
/*
for(j=0;j<r;j++)
 {
  for(k=0;k<c;k++)
  cout<<name[j][k];
  cout<<"\n";
 }


exit(0); 
*/

for(j=0;j<r;j++)
{
 for(k=0;k<c;k++)
 {
  if (name[j][k]=='#')
  {
   f=1;
   break;
  }
 }
}
 fout<<"Case #"<<start+1<<":\n";
 if (f==1) 
 fout<<"Impossible\n";
 else
 {
  for(j=0;j<r;j++)
  {for(k=0;k<c;k++)
  fout<<name[j][k];
  fout<<"\n";
  }
 }

} 
fin.close();
fout.close();
 return 0;
}
