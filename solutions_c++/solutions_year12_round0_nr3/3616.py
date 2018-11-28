#include<stdio.h>
#include<fstream>
using std::ofstream;
using std::ifstream;
using std::ios;
int main()
{
	int cases_no,min,max,number,reflection,reflection1,counter;
	int tenth,units,hundreds;
	ifstream in("C-small-attempt1.in",ios::in);
	ofstream out("output.txt",ios::out);
	if ( ! in ) 
		printf("error in openning ip file");
	if ( ! out ) 
		printf("error in openning op file");
	
	in>>cases_no;
	for(int i=0;i<cases_no;i++)
	{
		counter=0;
		in>>min>>max;
		
		if(!((min/10)==0 && (max/10)==0))
		{
			for(number=min;number<max;number++)
			{
				if((number/10)==0)
					break;
				else if((number/100)==0)
				{
					tenth=number/10;
					units=number%10;
					reflection=(units*10)+tenth;
					if(reflection <= max && reflection!=number && reflection > number )
					{
						counter++;
					}
				}
				else if((number/1000)==0)
				{
					hundreds=number/100;
					tenth=(number%100)/10;
					units=(number%100)%10;
					reflection=(units*100)+(hundreds*10)+tenth;
					reflection1=(tenth*100)+(units*10)+hundreds;
					if(reflection <= max && reflection != number && reflection > number)
					{
						counter++;
					}
					if(reflection1 <= max && reflection1 != number && reflection1 > number)
					{
						counter++;
					}
				}
			}
		}

		out<<"Case #"<<i+1<<": "<<counter<<'\n';
	}
	return(0);
}