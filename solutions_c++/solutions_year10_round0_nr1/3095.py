#include<stdio.h>
#include <iostream>
#include <stack>

using namespace std;
FILE *fin=fopen("large.in","r");
FILE *fout=fopen("output3.out","w");

int n,no,h,count=0;
void bin (int); 
int main (void) 
{ 
fscanf (fin,"%d",&no);
int k; 
for(h=0;h<no;h++)
{
	fscanf (fin,"%d %d",&n,&k); 
	bin (k); 
	count=0;
}
} 

void bin (int num) 
{
	stack <int> s;
	int a=0;
while (num != 0 && count<n) 
{ 
	if(num % 2 ==1)
	a++;	
 	//printf ("%d",num % 2); 
  	count++;
  	num = num /2; 
} 
if(a!=n)
	{
		fprintf(fout,"Case #%d: OFF\n",h+1);
	}
	else
	  {
	  fprintf(fout,"Case #%d: ON\n",h+1);
	  
	  }

}