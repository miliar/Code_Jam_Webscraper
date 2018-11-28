#include<iostream>
//#include<conio.h>

using namespace std;

int main()
{
    char conv[]={"yhesocvxduiglbkrztnwjpfmaq"};
    int T;
    char G[30][101];
    char p;
    cin>>T;
    int i,j;
    gets(G[0]);
    for ( i=0;i<T;++i)
        gets(G[i]);
    for ( i=0;i<T;++i)
    {
           cout<<"Case #"<<i+1<<": ";
           for ( j=0;G[i][j]!='\0';++j )
           {
               if ( G[i][j]!=' ' )
                  {p=conv[G[i][j]-97];
               cout<<p;}
               else
                   cout<<' ';
           }
           cout<<endl;
    }         
    //getch();
}


//97
