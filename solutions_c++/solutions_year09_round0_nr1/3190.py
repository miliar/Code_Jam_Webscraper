#include<iostream>
#include<fstream>

using namespace std;

ifstream inf("A-large.in");
ofstream ouf("A-large.out");

char* getToken(int p)
{
 char s[p*28];    
 int i=0,set=0;
 
 while(p>0)
 {
  inf>>s[i];
  if(s[i]=='(')
  set=1;
  else
  if(s[i]==')')
  {
       p--;set=0; 
  }  
  else if(set==0) p--;
  i++;
 }
 s[i]='\0';
 return s;
}  

int main()
{
 int i,j,k,m,z;

 int l,d,n;
 inf>>l>>d>>n;

 char dic[d][l], a[n][l][26],*str=new char[50];
 int counter, ct[n][l], tab[d][l];

 for(i=0;i<d;i++)
 for(j=0;j<l;j++)
 inf>>dic[i][j];

 for(i=0;i<n;i++)
 {
     str = getToken(l);
     k=0;

     for(j=0;j<l;j++)
     {
	 m=0;

	 if( str[k]=='(' )
	 {
	  for(k++;str[k]!=')';k++)
	  a[i][j][m++] = str[k];
	  ct[i][j]=m;
	 }
	 else
	 {
	  a[i][j][0] = str[k];
	  ct[i][j]=1;
	 }

	 k++;

     }
 }

 for(i=0;i<n;i++)
 {
  for(j=0;j<d;j++)
  for(k=0;k<l;k++)
  tab[j][k]=0;

  for(j=0;j<l;j++)
  for(k=0;k<ct[i][j];k++)
  {
   for(z=0;z<d;z++)
   if( a[i][j][k] == dic[z][j] )
   tab[z][j]=1;
  }

  counter=0;
  for(j=0;j<d;j++)
  {
   z=0;
   for(k=0;k<l;k++)
   if(tab[j][k]==1)
   z++;
   if(z==l)
   counter++;
  }
  ouf<<"Case #"<<(i+1)<<": "<<counter<<endl;
 }
 return 0;
}
