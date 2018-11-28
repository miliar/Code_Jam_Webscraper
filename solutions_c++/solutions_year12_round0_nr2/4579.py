#include<iostream>
#include<string>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{	
	int cases,input;	
	
	ifstream infile("B-large.in",ios::in);
	ofstream outfile("output2.txt",ios::out);
	if (infile.fail() || outfile.fail())
	{
		cout <<"Error opening files" <<endl;
		return 1;
	}
	
	infile >> cases;
	int numGooglers, numSurprising, atLeast,count1,count2,num;//count1 - normal, count2 - surprising
	for(int j=0; j<cases; j++)
	{	
		int temp;
		count1 = count2 = 0;
		infile >> numGooglers;		
		infile >> numSurprising;		
		infile >> temp;	
		atLeast = temp;	
		
		for(int i=0; i<numGooglers; i++) {
			infile >> input;
			num = int(round(double(input)/double(3)));			
			
			if ((input % 3) == 0){
					if(input == 0) continue;
					else if(num >= atLeast) count1++; 
					else if(num+1 == atLeast) count2++; 
				}
			else if (input > 3*num){
					if(num+1 >= atLeast) count1++; 					
				}
			else if (input < 3*num){
					if(num >= atLeast) count1++; 
					else if(num+1 == atLeast) count2++; 
				}
		}		
		if(count2 > numSurprising) {
			count2 = numSurprising;			
		} 
		if(atLeast < 1) {
			count1 = numGooglers; count2 = 0;
		}
		
		outfile << "Case #" <<j+1<<": "<< count1+count2  <<endl;
	}
	
	infile.close();
	outfile.close();
	return 0;
}


