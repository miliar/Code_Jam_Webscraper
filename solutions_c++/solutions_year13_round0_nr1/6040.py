#include<iostream>
#include<fstream>
using namespace std;
int main ()
{
ifstream in ("A-large.in");
ofstream out ("outputt.txt");
char x[4][4];
int counter=0 ;
int counter1=0 ;
int counter2=0 ;
int counter3=0 ;
int t ;
in>>t;
 for (int r=0 ; r<t;)
{ counter3=0 ;
	for (int i=0 ; i<4 ; i++)
	{
		for (int j=0;j<4;j++)
		{
			in>>x[i][j];
		}
	}
	/* ************************* */
	counter3=0 ;	
	for (int i=0 ; i<4 ; i++)
	{
			counter=0;
			counter1=0;
			 counter2=0 ;
			
		for (int j=0;j<4;j++)
		{			
			if (x[i][j]=='X')
			{
				++counter;
			}
				if (counter==4)
				{out<<"Case #"<<r+1<<": ";
					out<<"X won"<<endl;
					goto aa;
				}
				
		 if (x[i][j]=='O')
			{
				++counter1;
			}
			if (counter1==4)
				{out<<"Case #"<<r+1<<": ";
					out<<"O won"<<endl;
						goto aa;
				}
		
		if (x[i][j]=='T')
		{
			++counter2;
		}
		if (x[i][j]=='.')
		{
			counter3=1;
		}
		
		}

	if (counter1>counter)
		{
			counter1=counter1+counter2;
			if (counter1==4)
			{out<<"Case #"<<r+1<<": ";
			out<<"O won"<<endl;
				goto aa;}
		}
		
		else if (counter>counter1) {
				counter=counter+counter2;
			if (counter==4)
			{out<<"Case #"<<r+1<<": ";
			out<<"X won"<<endl;
				goto aa;}
		}
		}
		/*********************/
			counter=0;
			counter1=0;
			 counter2=0 ;
		for (int i=0 ; i<4 ; i++)
	{
			counter=0;
			counter1=0;
			 counter2=0 ;
			
		for (int j=0;j<4;j++)
		{			
			if (x[j][i]=='X')
			{
				++counter;
			}
				if (counter==4)
				{out<<"Case #"<<r+1<<": ";
					out<<"X won"<<endl;
						goto aa;
				}
				
		 if (x[j][i]=='O')
			{
				++counter1;
			}
			if (counter1==4)
				{out<<"Case #"<<r+1<<": ";
					out<<"O won"<<endl;
						goto aa;
				}
		
		if (x[j][i]=='T')
		{
			++counter2;
		}
		
		
		}

	if (counter1>counter)
		{
			counter1=counter1+counter2;
			if (counter1==4)
			{out<<"Case #"<<r+1<<": ";
			out<<"O won"<<endl;
				goto aa;}
		}
		
		else if (counter>counter1) {
				counter=counter+counter2;
			if (counter==4)
			{out<<"Case #"<<r+1<<": ";
			out<<"X won"<<endl;
				goto aa;}
		}
		}
		
	/***************************/
	counter=0;
			counter1=0;
			 counter2=0 ;		
			
	for (int k=0 ; k<4 ;k++)
	{
		if (x[k][k]=='X')
		{
			++counter;
			if (counter==4)
				{out<<"Case #"<<r+1<<": ";
					out<<"X won"<<endl;
						goto aa;
				}
		}
	
	 if (x[k][k]=='O')
			{
				++counter1;
			
			if (counter1==4)
				{out<<"Case #"<<r+1<<": ";
					out<<"O won"<<endl;
						goto aa;
				}
			}
			
				if (x[k][k]=='T')
		{
			++counter2;
		}
			
				
	} 
		if (counter1>counter)
		{
			counter1=counter1+counter2;
			if (counter1==4)
		{out<<"Case #"<<r+1<<": ";
			out<<"O won"<<endl;
				goto aa ;}
		}
		
		else if (counter>counter1) {
				counter=counter+counter2;
			if (counter==4)
			{out<<"Case #"<<r+1<<": ";
			out<<"X won"<<endl;
				goto aa;}
		}
		
	
		counter=0;
			counter1=0;
			 counter2=0 ;		
			
	for (int k=1 ; k<=4 ;k++)
	{
		if (x[-1+k][4-k]=='X')
		{
			++counter;
			if (counter==4)
				{out<<"Case #"<<r+1<<": ";
					out<<"X won"<<endl;
						goto aa;
				}
		}
	
	 if (x[-1+k][4-k]=='O')
			{
				++counter1;
			
			if (counter1==4)
				{out<<"Case #"<<r+1<<": ";
					out<<"O won"<<endl;
						goto aa;
				}
			}
			
				if (x[-1+k][4-k]=='T')
		{
			++counter2;
		}
			
				
	} 
		if (counter1>counter)
		{
			counter1=counter1+counter2;
			if (counter1==4)
			{out<<"Case #"<<r+1<<": ";
			out<<"O won"<<endl;
				goto aa;}
		}
		
		else if (counter>counter1) {
				counter=counter+counter2;
			if (counter==4)
			{out<<"Case #"<<r+1<<": ";
			out<<"X won"<<endl;
				goto aa;}
		}
		
		if (counter1!=4 || counter !=4 )
		{
		if (counter3 != 0 )
			{out<<"Case #"<<r+1<<": ";
				out<<"Game has not completed"<<endl;
				goto aa;
			}
			out<<"Case #"<<r+1<<": ";
		out<<"Draw"<<endl;
	goto aa;
}
aa : ++r ;
}

}
