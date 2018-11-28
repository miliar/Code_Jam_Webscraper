#include<iostream>
#include<string.h>
//#include<conio.h>
#include<string>

using namespace std;

main()
{
      int l,d,n;
      cin>>l>>d>>n;
      
      char a[5050][50];
      for(int i=0;i<d;i++)
      cin>>a[i];
      
         
      char c,k;
      char b[26];
      string str;
      int count=0;
      
      int l1=n;
      while(n--)
      {
      cin>>str;
      count=0;
      for(int k=0;k<d;k++)
      {
              int f=0,p=0;
              for(int i=0;i<l;i++)
              {
              c=str[p++];
              if(c=='(')
              {while((c=str[p++])!=')')
                 f=f+(c-a[k][i]?0:1);
              }
              else
              { 
               f=f+(c-a[k][i]?0:1);
              }
                 
              
              } 
               
               
               if(f==strlen(a[k]))
                count++;
                }
                cout<<"Case #"<<l1-n<<": "<<count<<endl;
                }
                        
      
      
              //getch();     
}
