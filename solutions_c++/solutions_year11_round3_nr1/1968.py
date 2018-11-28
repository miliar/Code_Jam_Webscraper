#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
	ifstream in;
	string s="A-small-attempt4.in";
	in.open(s.c_str());
	int t;
	ofstream out;
	string s1="A-small-attempt4.out";
	out.open(s1.c_str());
	in>>t;
	for(int i=0;i<t;i++)
	{
		int row;
		int column;
		in>>row;
		in>>column;
		int done = 1;
		int check =0;
		char **a;
		a= new char*[row];
		for(int j=0;j<row;j++)
		{
			char *b;
			b=new char[column];
			
			a[j] = b; 
		}
		
		for(int j=0 ; j< row ; j++)
		{
			for(int k=0; k<column ; k++)
			{
				in>>a[j][k];
			}
			
		}
		for(int j=0 ; j< row ; j++)
		{
			for(int k=0; k<column ; k++)
			{
				if(a[j][k] == '#')
				{
					a[j][k] = '/';
					
					//cout<<"k : "<<k<< "  column :"<<column;
					//cout<<endl<<"j: "<<j<<"  row : "<<row<<endl;
					if(k+1<column)
					a[j][k+1]= '\\';
					else
					check =-1;
					
					if(j+1<row)
					a[j+1][k]= '\\';
					else
					check = -1;
					
					if(j+1<row && k+1 < column)
					{
						a[j+1][k+1] ='/' ;
					}
					else 
					check = -1;
				}
			
			}
		}
		
		for(int j=0 ; j< row ; j++)
		{
			for(int k=0; k<column ; k++)
			{
				if(a[j][k]=='#')
				done = 0;
			}
			
		}
		//cout<<"check is "<<check<<endl;
		//cout<<"done is "<<done<<endl;
		out<<"Case #"<<i+1<<":"<<endl;
		if(check ==-1)
		out<<"Impossible"<<endl;
		else
		{
			for(int j=0 ; j< row ; j++)
			{
				for(int k=0; k<column ; k++)
				{
					out<<a[j][k];
				}
				out<<endl;
				
			}
		}
		
	}

	return 0;
}