#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<string>
#include<vector>
using namespace std;
int main()
{
	int inc=0;
	ifstream file("i1.in");
	ofstream file2("o2.txt",ios::trunc);
	string s1,s2,s3;
	getline(file,s2);
	int h=atoi(s2.c_str());
	
	while(inc<h)
	{
		int v=0,k=0,l=0,m=0,n=0,q=0,r=0,s=0,t=0;
		char a='e';
		file2<<"Case #"<<++inc<<": ";
		char c[4][4];
		for(int z=0;z<=3;z++)
		{
		getline(file,s1);
		for(int y=0;y<=3;y++)
		{
			c[z][y]=s1[y];
			if(c[z][y]=='.')
			{
				v++;
			}
		}
	}
		
		
	    for(int z=0;z<=3;z++)
	    {
	    	for(int y=0;y<=3;y++)
	    	{
	    		if(c[z][y]=='X'||c[z][y]=='T')
	    		{
	    			k++;
	    		}
	    		if(c[z][y]=='O'||c[z][y]=='T')
	    		{
	    			m++;
	    		}
	    		if(c[y][z]=='X'||c[y][z]=='T')
	    		{
	    			l++;
	    		}
	    		if(c[y][z]=='O'||c[y][z]=='T')
	    		{
	    			n++;
	    		}
	    	}
	    	if(k==4||l==4)
	    	{
	    	a='x';	
	    	
	    	}
	    	else if(m==4||n==4)
	    	{
	    	a='o';	
	    	}
	    	k=0;l=0;m=0;n=0;
	    }
	        
	    	if(a=='e')
	    	{
	    	for(int z=0;z<=3;z++)
	    	{
	    		if(c[z][z]=='X'||c[z][z]=='T')
	    		{
	    			q++;
	    		}
	    		if(c[z][z]=='O'||c[z][z]=='T')
	    		{
	    			r++;
	    		}
	    		if(c[z][3-z]=='X'||c[z][3-z]=='T')
	    		{
	    			s++;
	    		}
	    		if(c[z][3-z]=='O'||c[z][3-z]=='T')
	    		{
	    			t++;
	    		}
	    	}
	    	if(q==4||s==4)
	    	{
	    		a='x';
	    	}
	    	else if(r==4||t==4)
	    	{
	    		a='o';
	    	}
	    }
	    if(a=='e')
	    {
	    	if(v==0)
	    	{
	    		a='d';
	    	}
	    	else
	    	{
	    		a='n';
	    	}
	    }
	    
		if(a=='x')
		file2<<"X won";
		else if(a=='o')
		file2<<"O won";
		else if(a=='d')
		file2<<"Draw";
		else if(a=='n')
		file2<<"Game has not completed";
		
		file2<<endl;
		getline(file,s2);
		
	}
}
