#include<fstream>
#include<string.h>
#include<iostream>
using namespace std;
main()
{
      fstream fout;
      fout.open("barsha.txt");
      int n,i,j;
      char str1[105];
      char a[]={"yhesocvxduiglbkrztnwjpfmaq"};
      cin>>n;
      getchar();
      for(j=1;j<=n;j++)
      {   
         fout<<"Case #"<<j<<": ";
         gets(str1);
         for(i=0;i<strlen(str1);i++)
            {
            if(str1[i]==' ')
               fout<<' ';
            else
               fout<<a[str1[i]-97];
            }
         fout<<"\n";
      }
}
