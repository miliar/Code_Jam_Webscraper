#include <iostream>
#include <fstream>
#include <string>
#include <cmath>;
#include <math.h>;
using namespace std;
int main () 
{
	int convert_ascii [28] = {24,6,2,15,10,-3,15,16,-5,11,-2,-5,-1,-12,-4,2,9,2,-5,3,-11,-6,-17,-11,-24,-9};

	string Num_iterations;
	ifstream infile; 
	infile.open ("A-small-attempt1.in");
    getline(infile,Num_iterations); // Saves the line in STRING.
	string Line = " "; 
	int N =0 ;
	int Conv = 0 ; 
	int Length = 0 ;  
	int Num = int(Num_iterations[0])-21; 
	ofstream outputFile("Out.txt");
    N = Num;
	while (N>0)
	   {
		   outputFile << "Case #"<<Num-N+1<<":"<<" ";
	       getline(infile,Line);
		   //	checkCase 
		   Length = Line.length();
		   int L=Length;
		   int j = 0 ; 

		  while (Length!=0 )

		   {  j = L-Length;
			   // check if space 
			   if ( int (Line[j]) == 32 ) 
			   {  
				   outputFile <<" ";
			   }
			   else
			   {
					   if (int (Line [j])>=65 & int (Line [j])<=90)
						 { Conv = 65 ; 
						}
						else
						{
						Conv = 97;
						} 
			  outputFile << char ( convert_ascii[int (Line [j])-Conv]+int (Line [j]));
			   // add letter 
			  // outputFile <<"A";
			
		    }
			      Length--;
		  }
		  
		   outputFile <<endl ;

	     N--;
	   }
	



return 0 ; 
}