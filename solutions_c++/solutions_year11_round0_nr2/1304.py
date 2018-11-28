#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;

int t,c,d,n,i,j;
char a[10000][3],b[10000][2],s[10000000];
int k=0;
char arr[10000000];
int top=0;

void searchc(char q,char r)
{
 int g,h;
 char sf='[';
// cout<<"\n"<<q<<" "<<r<<"\n";
// getch();
 for(g=0;g<c;g++)
  if( ((a[g][0]==q)&&(a[g][1]==r)) || ((a[g][0]==r)&&(a[g][1]==q)) )
   {
   top=top-2;
   //cout<<"match";
   arr[top]=a[g][2];
   top++;
   return ;
   }
  for(g=0;g<d;g++)
   if((b[g][0]==q)||(b[g][1]==q))
    {
     sf=q;
     break;
    }
  if(sf!='[')
   {
     if(b[g][0]==q)
      {
       for(h=0;h<top;h++)
         {
          if(b[g][1]==arr[h])
           {
            top=0;
            //cout<<"TOP=0";
            break;
           }
         }
      }
      if(b[g][1]==q)
       {
        for(h=0;h<top;h++)
         {
          if(b[g][0]==arr[h])
           {
            top=0;
            //cout<<"TOP=0";
            break;
           }
         }
       }
   }
}

int main()
{
    fstream in,out;
    in.open("in22.in");
    out.open("ou2.txt");
 in>>t;
 while(t!=0)
  {
   //read input
   in>>c;
   for(i=0;i<c;i++)
    in>>a[i][0]>>a[i][1]>>a[i][2];
   in>>d;
   for(i=0;i<d;i++)
    in>>b[i][0]>>b[i][1];
  in>>n;
   for(i=0;i<n;i++)
    in>>s[i];
  //reading input done
  top=0;
  arr[top]=s[0];
  top++;
  for(i=1;i<n;i++)
   {
    arr[top]=s[i];
    top++;
    searchc(arr[top-1],arr[top-2]);
   }
   cout<<"Case #"<<k+1<<":"<<" ";
   out<<"Case #"<<k+1<<":"<<" ";
   k++;
  cout<<"[";
  out<<"[";
  for(i=0;i<top;i++)
   {
   if(i!=top-1){
   cout<<arr[i]<<", ";
   out<<arr[i]<<", ";
   }
   else{
    cout<<arr[i];
    out<<arr[i];
   }
   }
  cout<<"]\n";
  out<<"]\n";
  top=0;
  t--;
  }
return 0;
}
