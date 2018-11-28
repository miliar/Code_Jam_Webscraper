#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int Rotate(int num,int rotate)
{
	int len;
	string numstr,temp; 
	string buffer;
	while (rotate)
		{
			 // itoa(num%10, buffer , 10); // convert last digit to string 
		         temp= (num % 10)+48; // more efficient than above                               
			 numstr=temp+numstr;
			 num /=10; // last digit is lost using this division

			 rotate--;
		}
		// convert whatever is left in num into a char buffer
		while(num>0)
		{
			temp= (num%10)+48;
			buffer=temp+buffer;
			num /=10;
		}	
		numstr += buffer; // append the buffer to output string		

		len=numstr.size();		
		for(int i=0;i<len;i++)
	{
			num+=(numstr[i]-48)*pow(10,len-i-1);				
	}
			
	return num;
}
int Digits(int number)
{
	int digits=0;
	while (number) {
        number /= 10;
        digits++;
	    }
return digits;
	}
int main()
{
 long int A,B;
 int T,No,Dig;
 cin>>T;
 for(int i=0;i<T;i++)
	{
		cin>>A>>B;
		Dig=Digits(A);		
		No=0;
	if(Dig>1)
	for(int j=A;j<B;j++)
		for(int k=1;k<Dig;k++)
			if(Rotate(j,k)<=B && Rotate(j,k)>j){No++;}
	cout<<"Case #"<<i+1<<": "<<No<<endl;
	}		
		
return 0;
}
