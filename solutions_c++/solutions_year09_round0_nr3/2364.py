#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int m[1001][20];

int count(string input,int i,string s,int j)
{	
	int x=0;
	
	if(j==s.size())
	{
		x=1;
	}
	else if(i<input.size())
	{
		
		if(input[i]!=s[j])
		{
			m[i][j]=count(input,i+1,s,j) % 10000;
			x=m[i][j];
		}
		else
		{
			m[i][j]=((count(input,i+1,s,j+1)+count(input,i+1,s,j)) % 10000);
			x=m[i][j];
		}
	}
	
	
	return x;
}


int main (int argc, char * const argv[]) {
    // insert code here...
	string s;
	string inputstring;
	int i,j,k,N,c,c1,c2,c3,c4;
	
	ifstream myfile("/Users/Ashkan/Documents/Programming/Input/C-small-attempt0.in");
	ofstream output("/Users/Ashkan/Documents/Programming/Output/C-small-attempt0.out");
	
	s="welcome to code jam";
	if (myfile.is_open())
	{
		myfile >> N;
		std::getline(myfile,inputstring);
		for(i=1;i<=N;i++)
		{
			for(j=0;j<1001;j++)
				for(k=0;k<20;k++)
					m[j][k]=-1;
			
			std::getline (myfile, inputstring);
			c=count(inputstring,0,s,0);
			output <<"Case #"<<i<<":  ";
			
			c1=c %10;
			c=c/10;
			
			c2=c %10;
			c=c/10;
			
			c3=c%10;
			c=c/10;
			
			c4=c%10;
			
			output <<c4<<c3<<c2<<c1<<endl;
		}

		myfile.close();
		output.close();
		
	}
	else cout << "Unable to open file"; 	
    return 0;
}
