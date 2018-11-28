#include<iostream.h>
#include<conio.h>
#include<fstream.h>

int main()
{ 
 fstream fid,fid1;
 int i=0,num;
 char input[27]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
 char outpt[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',' '};
 fid.open("A-small-attempt3.in",ios::in | ios::out);
 fid1.open("output.txt",ios::in | ios::out);
 char output[200],sent[50][200],osent[50][200];
 while(!fid.eof())
 { 
  fid.getline(output,120);
  if(i==0)
  {
   num=atoi(output);
   cout<<num<<'\n';
  }
  else
  {
   strcpy(sent[i-1],output);
   puts(sent[i-1]);
  } 
  i++;
 }
 int c,j,k;
 c=i;
 cout<<"START : "<<'\n';
 for(i=0;i<num;i++)
 {
  puts(sent[i]);
 }
 for(i=0;i<num;i++)
 {
  for(j=0;j<(strlen(sent[i]));j++)
  {
   for(k=0;k<26;k++)
   {
    if(sent[i][j]==input[k])
    {
     osent[i][j]=outpt[k];
     cout<<sent[i][j]<<" "<<osent[i][j]<<" "<<i<<" "<<j<<" ";
     cout<<k<<'\n';
    }
    if(sent[i][j]==' ')
    {
     osent[i][j]=' ';
    }
   }
  }
 } 
 cout<<"DONE : "<<'\n';
 for(i=0;i<num;i++)
 {
  fid1<<"Case #"<<i+1<<": ";
  for(j=0;j<strlen(osent[i]);j++)
  {                             
   cout<<osent[i][j];
   fid1<<osent[i][j];
  }
  fid1<<'\n';
  cout<<'\n';
 }
 fid.close();
 fid1.close();
 getch();
}
