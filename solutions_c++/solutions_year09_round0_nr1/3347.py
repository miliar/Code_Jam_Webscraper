#include<fstream.h>
#include<conio.h>

int main()
 {
  clrscr();
  char fname[15];
  ifstream urfile;
  cout<<"enter file name...";
  cin>>fname;
  urfile.open(fname);
  if(!fname)
   {
    cout<<"cannot open file...";
    return 1;
   }
  int L=0,D=0,N=0,i,j,m;
  unsigned char ch;
  char A[80][80],test[300];
  while(1)
   {
    urfile.get(ch);
    if(ch==' ')
     break;
    L=L*10+ch-'0';
   }
  while(1)
   {
    urfile.get(ch);
    if(ch==' ')
     break;
    D=D*10+ch-'0';
   }
  while(1)
   {
    urfile.get(ch);
    if(ch==' ' || ch=='\n')
     break;
    N=N*10+ch-'0';
   }
  for(i=0;i<D;i++)
   {
    j=0;
    while(1)
     {
      urfile.get(A[i][j]);
      if(A[i][j++]=='\n')
       break;
     }
    A[i][j]='\0';
   }
  int f;
 for(int g=0;g<N;g++)
   {
    f=0;
    while(1)
     {
      urfile.get(test[f]);
      if(test[f]=='\n' || test[f]==EOF)
       {
	break;
       }
       f++;
     }
     test[f]='\0';
   int cas=0,k=0,flag=0;
  for(i=0;i<D;i++)
   {
    j=0;k=0;flag=0;
  while(test[j]!='\0' && !flag)
   {
     flag=1;
     if(test[j]=='(')
      {
       j++;
       while(test[j]!=')')
	{
	 if(A[i][k]==test[j])
	  {
	   k++;flag=0;
	   while(test[j++]!=')');
	   break;
	  }
	 j++;
	}
      }
      else
       {
	if(A[i][k]==test[j])
	 {
	  flag=0;
	  k++;
	  j++;
	 }
       }
    }
   if(!flag)
    cas++;
  }
  cout<<"Case #: "<<g+1<<"="<<cas<<'\n';
 }
  urfile.close();
  getch();
  return 0;
 }