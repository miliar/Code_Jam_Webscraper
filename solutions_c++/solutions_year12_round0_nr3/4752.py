#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
    freopen("C:\\Users\\pankaj\\Desktop\\codejam\\out.txt","w",stdout);
    freopen("C:\\Users\\pankaj\\Downloads\\C-small-attempt0.in","r",stdin);
    
 int a,b,t,counths=0;
 int array[10],counter=0,counter2=0,num=0,countmain=0;;
 cin>>t;
 while(t--)
 {
     countmain=0;
 cin>>a>>b;
 counths++;
 for(int i=a;i<b;i++)
 {
     int j=i;
     counter=0;
     while(j!=0)
     {
     array[counter]=j%10;
     j=j/10;
     counter++;
     }
     counter2=counter;
     while(counter2!=1)
     {
         counter2--;
         int temp=array[0];
         num=0;
         int p=1;
         for(int k=0;k<=counter-2;k++)
         {
         array[k]=array[k+1];
       num=p*array[k]+num  ;
       p=p*10;
         }    
         array[counter-1]=temp;
         num=p*array[counter-1]+num  ;
         if(temp>0)
         {
             if(num>i&&num<=b)
             countmain++;
         }
     }
 }
 cout<<"Case #"<<counths<<": "<<countmain<<endl;
} 
//system("pause");
    return 0;
}
