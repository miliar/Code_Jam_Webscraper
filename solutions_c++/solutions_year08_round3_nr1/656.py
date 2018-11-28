#include<fstream>
#include<iostream>
# include<string.h>
# include<math.h>
# include<malloc.h>
# include<stdio.h>
# include<conio.h>

class TT
{

	int t;
	int p,k,l;
	long *a;
	
	char file_in[50];
	char file_out[50];
	

public:
	TT();
	void sort(long*,int);
	void calc();


};

using namespace std;

int main()
{

  TT o;
  o.calc();

}

TT::TT()
   {
	   	cout<<"Enter input file name:";
	cin>>file_in;
	cout<<"\nEnter output file name:";
	cin>>file_out;
   }

  
	   
void TT::calc()
{
    int i,j;
	int q,r,s;
	
    	
	int count=0;
	FILE *in_file;
	FILE *out_file;
	
	in_file=fopen(file_in,"r");
	out_file=fopen(file_out,"w");
      if(in_file==NULL)
        {
                cout<<" opening error" <<endl;

        }
	  else
	  {

         

		 
		  fscanf(in_file,"%d",&t);
		  for(i=0;i<t;i++)
		  {
			  
          fscanf(in_file,"%d",&p);
			
		  fscanf(in_file,"%d",&k);
		  
		  fscanf(in_file,"%d",&l);
		  cout<<p<<" "<<k<<" "<<l<<endl;

		  a=new long  [l];
		  for(j=0;j<l;j++)
		  {
			  fscanf(in_file,"%d",&a[j]);
			  cout<<a[j]<<" ";
		  }
		  cout<<endl;
          sort(a,l);
		  count=0;
		  j=l-1;
		  for(r=1; r<=p;r++)
		  {
			  for(s=0;s<k;s++)
			  {
				  if(j>=0)
				  {
			  count += a[j]*r;
			  j--;
				  }
			  }
		  }




			
				   
			fprintf(out_file,"Case #%d: %d\n",i+1,count);
			delete [] a;
			
	  }
	  }

	 fclose(in_file);
     fclose(out_file);
	  
}
void TT::sort(long *a,int n)
{
	int i,j;
	long t;
	for(i=0;i<n;i++)
	{
		for(j=0;j<(n-1);j++)
		{    
			if (a[j]>a[j+1])
			{
				t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
			}
		}
	}
	cout<<endl;
	for(i=0;i<n;i++)
		cout<<a[i]<<" ";
	cout<<endl;
}




       







