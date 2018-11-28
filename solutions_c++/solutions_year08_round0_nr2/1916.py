#include<fstream>
#include<iostream>
# include<string.h>

class TT
{
	int n_ab;
	int n_ba;
	int *a_dept;
	int *b_arr;
	int *b_dept;
	int *a_arr;
	int t;
	int n;
	char file_in[50];
	char file_out[50];

public:
	TT();
	~TT();
	void calc();
	void sort(int*,int);


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

   TT::~TT()
   {

	   delete [] a_arr;
	   delete [] a_dept;
	   delete [] b_arr;
	   delete [] b_dept;
   }
	   
void TT::calc()
{
	int r1,r2;
	int hrs,mins;
	int m;
	char buffer[20];
	int flag;
	char w[2];
	char w1,w2,w3,w4;
	int j,k,l;
	int t1,t2,t3;
    ifstream in_file;
	in_file.open(file_in,ios::in |ios::binary);
	 ofstream out_file;
        out_file.open(file_out,ios::out|ios::binary);
      if(in_file==NULL)
        {
                cout<<" opening error" <<endl;

        }
	  else
	  {

         

		  in_file.getline(buffer,20);
		  n=atoi(buffer);
		  for(j=0;j<n;j++)
		  {
			  in_file.getline(buffer,20);
			  t=atoi(buffer);
			  in_file.getline(buffer,20);
			  
			  w1=buffer[0];
			  t1=atoi(&w1);
			  w2=buffer[1];
			  if(w2!=32)
			  {
				  t2=atoi(&w2);
				  n_ab=t1*10+t2;
				  w3=buffer[3];
				  w4=buffer[4];
			  }
			  else
			  {
				  n_ab=t1;
				  w3=buffer[2];
				  w4=buffer[3];
			  }
			  if(!(w4>=48)&&(w4<=57))
				  {
					  n_ba=atoi(&w3);
				  }
				  else
				  {
					  n_ba=((atoi(&w3))*10)+atoi(&w4);
				  }

				

			  a_dept=new int [n_ab];
			  b_arr=new int [n_ab];
			  b_dept=new int [n_ba];
			  a_arr=new int [n_ba];
			  for(k=0;k<n_ab;k++)
			  {
				  in_file.getline(buffer,20);
				  w1=buffer[0];
				  w2=buffer[1];
				  w3=buffer[3];
				  w4=buffer[4];
				  hrs=((atoi(&w1))*10)+atoi(&w2);
				  mins=((atoi(&w3))*10)+atoi(&w4);
				  a_dept[k]=(60*hrs)+mins;
				  w1=buffer[6];
				  w2=buffer[7];
				  w3=buffer[9];
				  w4=buffer[10];
				  hrs=((atoi(&w1))*10)+atoi(&w2);
				  mins=((atoi(&w3))*10)+atoi(&w4);
				  b_arr[k]=(60*hrs)+mins+t;
			  }
			  for(k=0;k<n_ba;k++)
			  {
				  in_file.getline(buffer,20);
				  w1=buffer[0];
				  w2=buffer[1];
				  w3=buffer[3];
				  w4=buffer[4];
				  hrs=((atoi(&w1))*10)+atoi(&w2);
				  mins=((atoi(&w3))*10)+atoi(&w4);
				  b_dept[k]=(60*hrs)+mins;
				  w1=buffer[6];
				  w2=buffer[7];
				  w3=buffer[9];
				  w4=buffer[10];
				  hrs=((atoi(&w1))*10)+atoi(&w2);
				  mins=((atoi(&w3))*10)+atoi(&w4);
				  a_arr[k]=(60*hrs)+mins+t;
			  }
			  sort(a_arr,n_ba);
			  sort(a_dept,n_ab);
			  sort(b_arr,n_ab);
			  sort(b_dept,n_ba);
			  r1=0;
			  r2=0;
			   for(k=0,m=0;k<n_ba && m<n_ab;)
			  {
				   if(a_arr[k]<=a_dept[m])
				   {
					   k++;
					   m++;
				   }
				   else
				   {
                       r1++;
					   m++;
				   }
			  }
			   while(m!=n_ab)
			   {
				   r1++;
				   m++;
			   }
			   for(k=0,m=0;k<n_ab && m<n_ba;)
			  {
				   if(b_arr[k]<=b_dept[m])
				   {
					   k++;
					   m++;
				   }
				   else
				   {
                       r2++;
					   m++;
				   }
			  }
			   while(m!=n_ba)
			   {
				   r2++;
				   m++;
			   }

			out_file<<"Case #"<<j+1<<": "<<r1<<" "<<r2<<"\n";
			
		  }
	  }

	  in_file.close();
	  out_file.close();
}



void TT::sort(int *a,int n)
{
	int i,j,t;
	cout<<endl;
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
}

       







