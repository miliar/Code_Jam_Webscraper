#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main()
{
    int arr[26][15],l,d,n,i,j,k,p,nt,f,now;
    char words[5000][16],str[400],stk[400];
    cin>>l>>d>>n;
    nt=n;
     for(i=0;i<d;i++)
     {
      cin>>words[i];     
     }

    while(n>0)
    {

     for(i=0;i<26;i++)
        for(j=0;j<15;j++)
           arr[i][j]=0;

     cin>>str;
     p=0;
     for(i=0;i<strlen(str);i++)
     {
        if(str[i]=='(')
        {
           
           for(j=i+1,k=0;str[j]!=')';j++,k++)
           stk[k]=str[j];
           
           i=j;
           
           for(j=0;j<k;j++)
           arr[stk[j]-97][p]=1;
           p++;
        }
        else
        {
            arr[str[i]-97][p]=1;
            p++;
        }
     }
     now=0;
     for(i=0;i<d;i++)
     {
         f=0;
         for(j=0;j<l;j++)
         {
             if(arr[words[i][j]-97][j]==0)
             {
              f=1;
              break;
             }
         }
         if(f==0)
         now++;
     }
     cout<<"Case #"<<nt-n+1<<": "<<now<<endl;
     
     n--;
     
    }
//    getch();
    return 0;
}
