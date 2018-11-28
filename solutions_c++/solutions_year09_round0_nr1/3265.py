#include<iostream>
#include<string>
#include<fstream>

using namespace std;


int main()
{

 ifstream infile;
 ofstream outfile;

 infile.open("input.txt");
outfile.open("output.txt");

 int numberofcaseletters;
 int lines;
 int numberofcases;
 char x;
 string language[25];
 string possibilities[25];
 

infile >> numberofcaseletters;
infile >> lines;
infile >> numberofcases;
infile.get(x);

for ( int i=0; i < lines; i++)
{
getline(infile, language[i]);
possibilities[i] = language[i];
}

for ( int j=0; j < numberofcases; j++)
{


for ( int k=0; k < numberofcaseletters; k++)
{
infile.get(x);
int counter2=0;
int test;

if ( k==0)
{
	test = lines;
}



if ( x == '(')
{
	while ( x != ')')
	{ 
		infile.get(x);
        
		for ( int h=0; h < test; h++)
		{ 
           if ( possibilities[h][k] == x)
		   {
			   
			   possibilities[counter2].swap(possibilities[h]);   
		      
			  counter2++;
		   }
		}
		
	}
}
else
{
        for ( int c=0; c < test; c++)
		{
           if ( possibilities[c][k] == x)
		   {
              possibilities[counter2] = possibilities[c];   
		   
			  counter2++;
		   }
		}
}


test = counter2;

if ( k == numberofcaseletters -1)
{
	outfile <<"Case #" << j+1 <<": " << counter2 << endl;
}

}

for ( int i=0; i < lines; i++)
{
possibilities[i] = language[i];
}

infile.get(x);

}




return 0;
}