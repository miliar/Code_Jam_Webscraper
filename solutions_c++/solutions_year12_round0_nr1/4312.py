#include<iostream>
#include<cstdio>
using namespace std;


int main()
  {
   
    char *a="yhesocvxduiglbkrztnwjpfmaq";
    char line[102];
    int n,i,j;
    cin>>n;
    getchar();
    j=1;
    while(n--)
    {
               cin.getline(line,102);
               i=0;
               cout<<"Case #"<<j<<": ";
               while(line[i]!='\0')
               {
               if(line[i]==' ')cout<<' ';
               else
               cout<<a[line[i]-97];
               i++;
               }
               cout<<endl;
               j++;
               
    }
    //system("pause");
     return 0;
}
