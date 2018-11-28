#include<iostream>
#include<conio.h>
#include<string>
#include<iomanip>
using std::string;
using namespace std;
int count=0;
void check(string a,string b,int i,int j)
{
      if(b[j]!='\0')
      {
         int prev_pos=i-1;
         do
         {
           prev_pos=a.find(b[j],prev_pos+1);
           if(b[j+1]=='\0' && prev_pos!=-1)
           {
               ::count++;
               //cout<<"here: "<<prev_pos;    
           }
           else if(prev_pos!=-1)
           {
               //cout<<prev_pos<<endl;
               check(a,b,prev_pos,j+1);               
           }
         }while(prev_pos!=-1);
    }
}

int main()
{
   int n,i;
   string input;
   string name("welcome to code jam");
   cin>>n;
   getchar();
   int j[n];
   for(i=0;i<n;i++)
   {
      getline(cin,input);
      check(input,name,0,0);
      j[i]=::count;
      ::count=0;
   }
   for(i=0;i<n;i++)
   {
      cout<<"Case #"<<i<<" "; 
      cout.fill('0');
      cout.width(4);     
      cout<<j[i];
      cout<<endl;
   }
   getch();
   return 0;  
}
