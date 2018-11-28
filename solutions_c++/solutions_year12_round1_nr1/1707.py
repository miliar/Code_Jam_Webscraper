#include <iostream>
#include <stdlib.h>
#include <string>
#include<math.h>
#include<stdio.h>
#include<vector>
using namespace std;



vector<int> outputBinary(unsigned int n,int a)
{
  vector<int> k;

  int remainder;



  for(int i=0;i<a;i++)
    {
      	    remainder = n%2;
	    n=n/2;    
	    k.push_back(remainder); 


    }
  return k;

}



class prob
{
public:
  prob(int k)
  {
    a=k;
    data=new int[a+2];
    


  }

  int a;
  int * data;
  double p;
  



};

int main()
{

  int num;
  cin>>num;
  
  
  double * result=new double[num];
  
  for(int i=0;i<num;i++)
    {

      int a,b;
      cin>>a;
      cin>>b;
      b=b-a;
      double *p=new double[a];
      for(int j=0;j<a;j++)
	cin>>p[j];
      
      int k=pow(2,a);
 
      vector<prob> pr;
 
      for(int j=0;j<k;j++)
	{
	  prob* pa=new prob(a);
	  vector<int> s=outputBinary(j,a);
	  pa->data[1]=a+b+2;
	  pa->data[0]=b+1;
	  for(int q=0;q<a;q++)
	    {
	      if(s[q]==0)
		{
		  pa->data[q+2]=b+1+2*(a-q);


		}
	      if(s[q]==1)
		{
		  pa->data[0]=a+b+b+2;
		  pa->data[q+2]=b+1+2*(a-q);
		  for(q++;q<a;q++)
		    {
		      pa->data[q+2]=b+1+2*(a-q)+a+b+1;


		    }
	      
		}

	    }

	  double probability=1;
	  for(int q=0;q<a;q++)
	    {
	      if(s[q]==0)
		probability*=p[q];
	      if(s[q]==1)
		probability*=1-p[q];



	    }
	  pa->p=probability;

	  pr.push_back(*pa);
	  delete pa;
	  
	  
	}
 
      
      double* times=new double[a+2];
      for(int j=0;j<a+2;j++)
	times[j]=0;
      for(int j=0;j<k;j++)
	{
	  for(int q=0;q<a+2;q++)
	    times[q]+=pr[j].data[q]*pr[j].p;
	  


	}
      
      result[i]=times[0];
      for(int j=1;j<a+2;j++)
	{

	  if(times[j]<result[i])
	    result[i]=times[j];
	}
    }


  //  delete [] result;
      
      for(int i=0;i<num;i++)
	{	cout<<"Case #"<<i+1<<": ";
	  printf("%.6f",result[i]);
	  cout<<endl;
	}

  return 0;


}
