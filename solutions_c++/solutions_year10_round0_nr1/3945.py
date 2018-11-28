//#include<conio.h>
#include<iostream.h>
#include<math.h>
  int call(int,long int);


  void main()
	{
	  int t,i,n,j,result;
	  long int k;
	  //clrscr();
	  cin>>t;
	  for(i=0;i<t;i++)
	  {  cin>>n>>k;
		 result=call(n,k);
		  cout<<"Case #"<<i+1<<":";
		  if(result) {cout<<" ON"<<endl;}
		  else {cout<<" OFF"<<endl;}


		}



	//getch();
	}


	int call(int a,long int b)
{
 long int x,y,r=0,k=2;
 x=pow(2,a);
 y=x;

 while((y-1)<=b)
	{
		  if((y-1)==b)
		  {return(1);}
		  else { y=x*(k++);}
	}
		return(r);
}
