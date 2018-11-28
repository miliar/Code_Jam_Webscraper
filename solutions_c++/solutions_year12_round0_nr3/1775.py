#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;


int main()
{
	   ifstream in;
	   in.open("C-small-attempt0.in");
	   ofstream out;
       out.open ("Answer.txt");
	   

int T;
in>>T;
for(int i=0;i<T;i++)
{    
	out<<"Case #"<<i+1<<": ";
	int result=0;
	int A;
	int B;
	int n;
	int m;
	vector <int>ms;
	int temp;
		  
	in >>A;
	in >>B;
	temp=A;
		  float length=0;
		  while(temp!=0)
	          {   
		   length++;
	       temp=temp* pow(10,-1.0);
	          }
	 for(n=A;n<B;n++)
	   {  
		   ms.erase(ms.begin(),ms.end());
		  for(float x=1;x<(int)length;x++)
		  {
			 float temp1 = n *pow(10,-x);
			 int temp2 =n *pow(10,-x);
			  temp1= temp1-temp2;
			  temp1= (temp1 * pow(10,x));
			  temp1=(int)(temp1+0.5);
			  temp1 = temp1 *pow(10,length-x);
			  m = temp1+temp2;

			  int length2=0;
			  int anotherm=m;
			  while(anotherm!=0)
	          { 
		       length2++;
			   anotherm=anotherm* pow(10,-1.0);
              }
			  bool check=true;
			  
			  for(int j=0;j<ms.size();j++)
			  {
				  if(ms[j]==m)
				  {
					  check =false;
					  break;
				  }
				  else
					  check =true;
			  }
			  if(check)
			  ms.push_back(m);
			  if(n<m && m<=B && m>A && A<=n && (int)length==length2 && m!=n && check )
				  result++;
			  check =true;

		  }      
	  }


	if(i!=T-1)
	{
	out<<result<<endl;
	ms.erase(ms.begin(),ms.end());
	}
	else
    out<<result;
	ms.erase(ms.begin(),ms.end());
	}
return 0;
	 
}
  
