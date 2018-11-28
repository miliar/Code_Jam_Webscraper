#include<iostream>
#include<math.h>
#include<fstream>
#include<string>
using namespace std;

int main()
{
ifstream enter("small.txt");
ofstream exit("out.txt");
int N;
enter >> N;
for(int p=0; p<N ; p++)
{
int max, key, let;

enter >> max >> key >> let;
if (let > max*key)
{
exit << "Case #" << p+1 << ": " << "impossible";
}
else {
	int freq[let];

	for(int i=0; i<let ; i++)
	{
	enter >> freq[i];
    }
int current=1, output=0, count;
int length=let;
	int min,minat;
	for(int i=0;i<(length-1);i++)
	{
		minat=i;
		min=freq[i];

      for(int j=i+1;j<(length);j++) //select the min of the rest of freq
	  {
		  if(min>freq[j])   //ascending order for descending reverse
		  {
			  minat=j;  //the position of the min element 
			  min=freq[j];
		  }
	  }
	  int temp=freq[i] ;
	  freq[i]=freq[minat];  //swap 
	  freq[minat]=temp;

		
	}
current=1; 
count=1;
for(int i=let-1; i>=0 ; i--)
	{
	output= output + current * freq[i];
	count++;
	if(count>key)
	{
	count=1;
	current ++;
	}
	
	}
exit << "Case #" << p+1 << ": " << output << endl;
   }
} 
}


