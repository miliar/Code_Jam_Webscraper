\*This is a C++ file*/

#include<iostream.h>
#include <algorithm>
#include <vector>
#include<fstream.h>
#include<stdlib.h>


#define FILE_IN "C-small-attempt2.in"
const char *FILENAME = "output.txt";



main()
{
 int R,k,N;
 int a[10],sum=0,sum1=0,total=0,i,j, cnt=0,q;
 ifstream input;
 ofstream fout(FILENAME);
 input.open(FILE_IN,ios::in|ios::nocreate);

 if(!input)
	{
		cout<<endl<<"The file couldn't be found";
		exit(1);
	}

 input>>q;
 q=q*2;
 for(int l=1;l<=q;l=l+2)
	{
		cnt++;
		input>>R>>k>>N;
		
		for(i=0;i<N;i++)
        {
			input>>a[i];
			
		}
		
 
 sum=0;
 sum1=0;
 total=0;
 for(j=0;j<R;j++)
 {
  sum=a[0]+0;
  
  if(sum==k)
  {
   total=total+sum;
   std::rotate(a, a + 1, a + N);
  }
  else
  {
   if(N==1)
   {
	   total=total+a[0];
   }
   else
   {

   for(i=1;i<N;i++)
   {


     




    sum1=sum+a[i];
	if(sum1>k)
	{

     
	 
	 total=total+sum;
	 std::rotate(a, a + i, a + N);
	 break;
	}
	else if(sum1==k)
	{

     

	 total=total+sum1;
	 std::rotate(a, a + (i+1), a + N);
	 break;
    }
	else
	sum=sum1;
   }
   }
  }
 } 
 
 fout<<"Case #"<<cnt<<": "<<total<<"\n";
 sum=0;
 sum1=0;
 }
 input.close();
 fout.close();
 
 return 0;
}


