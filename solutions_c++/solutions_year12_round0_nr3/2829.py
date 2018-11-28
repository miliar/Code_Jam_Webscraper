#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;

long int lines,answer,a,b,i=1,num,k,backup;
long int numctr,temp1;
long int num1,num2,j,decc;
long int digits,counter=0,decarray[5000],decarray1[5000];
long int cnt=0,temp,count,array[1000],rarray[1000],newarray[1000];

void compare11()
{
 decc=1;
 for(cnt=0;cnt<counter;cnt++)
 {
  if(decarray[cnt]==num1 && decarray1[cnt]==num2)
  {
	decc=0;
  }
 }
}

void normalise()
{
num2=0;
 for(cnt=1;cnt<=digits;cnt++)
 {
  rarray[cnt]=newarray[cnt-1];
 }
temp=1;
for(cnt=1;cnt<digits;cnt++)
temp=temp*10;

for(cnt=1;cnt<=digits;cnt++,temp=temp/10)
num2=num2+(temp*rarray[cnt]);

}
void rotate()
{
 
 temp=rarray[digits];
 newarray[0]=temp;
 for(cnt=1;cnt<digits;cnt++)
 {
  newarray[cnt]=rarray[cnt];
 }
}

void finddigits()
{
 digits=0;
 int ctri=0,xa=num;
 while(num>9)
 {
	array[ctri]=num%10;
	num=num/10;
	ctri++;
 }
 array[ctri]=num;
 ctri++;
 digits=ctri;
 for(ctri=0;ctri<=digits;ctri++)
 {
 	rarray[ctri]=array[digits-ctri];
 }

}
	
int main()
{

 ifstream infile ("input.in");
 ofstream outfile;
 outfile.open ("out.txt");
 infile>>lines;
 cout<<lines;
 while(lines>0)
 {
	answer=0;
	counter=0;
	outfile<<"Case #"<<i<<": ";
	infile>>a;
	infile>>b;
	for(j=a;j<=b;j++)
	{
		num1=j;
		num2=j;
		num=j;
		numctr=0;
		cout<<endl;
		finddigits();
		for(k=0;k<digits;k++)
		{
			rotate();
			normalise();
			compare11();

			if(num2<num1 && a<=num2 && b>=num1 && num1/num2<10 && decc==1 )
			{
			 cout<<num2<<" "<<num1<<endl;
				answer++;
				decarray[counter]=num1;
			
				decarray1[counter]=num2;
				counter++;
			}
		}			
	}
	outfile<<answer<<"\n";
	lines--;
	i++;
 }
 outfile.close();
}
