#include<iostream>
//#include<conio.h>
#include<math.h>
#include<algorithm>
using namespace std;
int check(int a,int b,int i)
{
	int arr[10],index=0;
    int f,d,count=0,temp=0,te=0,final=0;
    f=i;
    d=log10(i);
//    cout<<d<<" "<<i<<endl;
    int e[d],m=0,l[d],pp[d];
    while(f>0)
    {
              e[m]=f%10;
              l[m]=f%10;
              pp[m]=f%10;
              f=f/10;
              m++;
              }
  m--;
 
 int h;
 h=m;
 while(h--)
 {
            temp=l[0];
    for(int j=0;j<=m-1;j++)
    {
            l[j]=l[j+1];       
            }
    l[m]=temp;
    temp=0;
    for(int j=m;j>=0;j--)
    {
            temp=temp*10+l[j];
            }
    if((temp>=a&&temp<=b)&&l[m]!=0&&pp[m]!=0&&temp>i)
{
	if(!binary_search(arr,arr+index,temp))
{
    //cout<<i<<" "<<temp<<endl;
	arr[index]=temp;
index++;
final++;
} 
   
    }
}
return(final);
    }
int main()
{
    int a,b,count=0,n,h,t=0;
 cin>>n;
    h=0;
    while(h<n)
    {
count=0;
t=0;     
         h++;
    cin>>a>>b;
    for(int i=a;i<=b;i++)
    {
    if((t=check(a,b,i))>0)
    {
     
        //     cout<<i<<endl;
                    count+=t;
                    }
}
cout<<"Case #"<<h<<": "<<count<<endl;
}
//getch();
return(0);
    }
