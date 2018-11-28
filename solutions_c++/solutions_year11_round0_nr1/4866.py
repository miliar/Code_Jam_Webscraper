#include<conio.h>
#include<iostream.h>
int main()
{
 int i,j,k,l,push,n,oflag,bflag,x,flag,tim,p;
 int step;
 char a[100];
 int b[100];
 int result[100];
 printf("INPUT\n");
 cin>>tim;

 for(p=0;p<tim;p++)
 {
  j=0,step=0,k=1,l=1,push=0,oflag=0,bflag=0,x=0,flag=0;
  
  cin>>n;
  for(i=0;i<n;i++){cin>>a[i];cin>>b[i];}
  
  i=0;
  while(a[i]!='O' && i<n) i++;
  if(i>=n) oflag=1;
  while(a[j]!='B' && j<n) j++;
  if(j>=n) bflag=1;
  
  while(push<n)
  {
     if(oflag==0)
     {
          x=b[i];
          if(x>k)   k++;
          else
          { 
              if(x<k)  k--;
              else
              {
                  if(i<=j)
                  {
                   push++;flag=1;
                   do {i++;} while(a[i]!='O' && i<n);
                   if(i>=n) oflag=1;
                  }
              }
          }
     }
     if(bflag==0)
     {
          x=b[j];
          if(x>l)   l++;
          else
          { 
              if(x<l)  l--;
              else
              {
                  if(j<=i && flag==0)
                  {
                   push++;
                   do {j++;} while(a[j]!='B'  && j<n);
                   if(j>=n) bflag=1;
                  }
              }
          }
     }
     step++;flag=0;
  }
  result[p]=step;
 }
 for(p=0;p<tim;p++)
  cout<<"case #"<<(p+1)<<": "<<result[p]<<"\n";
 getch();
 return 0;
}
