#include <iostream>
using namespace std;

int main()
{
  char s[501];
  char pattern[20];
  int map[20][501];
  int i,ii,p;
  int nTestCase;
  int ans;

  scanf("%d",&nTestCase);
  
  pattern[1]='w';
  pattern[2]='e';
  pattern[3]='l';
  pattern[4]='c';
  pattern[5]='o';
  pattern[6]='m';
  pattern[7]='e';
  pattern[8]=' ';
  pattern[9]='t';
  pattern[10]='o';
  pattern[11]=' ';
  pattern[12]='c';
  pattern[13]='o';
  pattern[14]='d';
  pattern[15]='e';
  pattern[16]=' ';
  pattern[17]='j';
  pattern[18]='a';
  pattern[19]='m';
   
  cin.getline(s,100); 
  for (p=1;p<=nTestCase;p++)
  {
     cin.getline(s,500);
	 for (i=0;i<=500;i++)
	 {
	   map[0][i]=1;
	 }

	 for (i=1;i<=19;i++)
	 {
	   for (ii=1;ii<=500;ii++)
	   {
	   map[i][ii]=0;
	   }
	 }

	 for (i=0;i<strlen(s);i++)
	 {
	   for (ii=1;ii<=19;ii++)
	   {
	     if (s[i]==pattern[ii])
		 {
		   if (i==0)
		   {
		     if (ii==1)
		       {
			   map[ii][i]=1;
			   }
		   }
		   else
		   {
		     map[ii][i]=map[ii][i-1]%10000+map[ii-1][i-1]%10000;
			 map[ii][i]=map[ii][i]%10000;
		   }
		 }
		 else
		 {
		   if (i==0)
		   {
		     map[ii][i]=0;
		   }
		   else
		   {
		     map[ii][i]=map[ii][i-1];
		   }
		 }
	   }
	 }
	 /*
	 for (i=1;i<=19;i++)
	 {
	   for (ii=0;ii<strlen(s);ii++)
	   {
	   cout<<map[i][ii]<<" ";
	   }
	 cout<<endl;
     }
	 */
	 cout<<"Case #"<<p<<": ";
	 ans = map[19][strlen(s)-1];
	 if (ans<10)
	 {
	 cout<<"000"<<ans<<endl;
	 }
	 else if (ans<100)
	 {
	 cout<<"00"<<ans<<endl;
	 }
	 else if (ans<1000)
	 {
	 cout<<"0"<<ans<<endl;
	 }
	 else
	 {
	 cout<<ans<<endl;
	 }
	 
  }
return 0;
}