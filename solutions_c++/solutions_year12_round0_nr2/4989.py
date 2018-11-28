#include <iostream>
#include <string>
#include <fstream>

using namespace std;

//This function checks if a file exists.
bool file_existence(char* file_name=0)
{
	ifstream file;
	bool existence(false);
	
	file.open(file_name,ios::in);
	existence=file.good();
	file.close();
	
	return existence;
}

//Returns the int representation of the text of a string.
int toInt(const string text)
{
	int aux_int(0);
	int length(text.length());
	for(register unsigned int cnt=0; cnt<length; cnt++) aux_int=10*aux_int+((int) text[cnt]-48);
	
	return aux_int;
}

int getMaximumDancers(string& test)
{
	int numDancers(0);
	int numSurprising(0);
	int threshold(0);
	int multiple(0);
	int remainder(0);
	unsigned int length(test.length());
	int* totalPoints(0);
	//This array will store how many of each case are in the table:
	//Case [0]= true, true
	//Case [1]= false, true
	//Case [2]= false, false
	//Case [3]= false, false, but without posibility of representing a surprising triplet. i.e. the points sum 0.
	int quantity_in_each_state[4]={0,0,0,0};
	//The counter.
	register unsigned int cnt=0;
	
	//Get the number of dancers;
	for(cnt=0; (test[cnt]!=' ')&&(cnt<length); cnt++) numDancers=10*numDancers+((int) test[cnt]-48);
	//Get the number of surprising triplets;
	for(cnt=cnt+1; (test[cnt]!=' ')&&(cnt<length); cnt++) numSurprising=10*numSurprising+((int) test[cnt]-48);
	//Get the threshold for the best result of the dancers;
	for(cnt=cnt+1; (test[cnt]!=' ')&&(cnt<length); cnt++) threshold=10*threshold+((int) test[cnt]-48);
	
	totalPoints=new int[numDancers];
	
	//Recover the total points of all the dancers.
	for(register unsigned int cnt2=0; cnt2<numDancers; cnt2++)
	{
		totalPoints[cnt2]=0;
		for(cnt=cnt+1; (test[cnt]!=' ')&&(cnt<length); cnt++) totalPoints[cnt2]=10*totalPoints[cnt2]+((int) test[cnt]-48);
	}
	
	//Get the quantities in each state.
	for(cnt=0; cnt<numDancers; cnt++)
	{
		if(totalPoints[cnt]==0) 
		{
			if(threshold==0) quantity_in_each_state[0]++;
			else quantity_in_each_state[3]++;
		}
		else if (totalPoints[cnt]==1)
		{
			if(threshold<=1) quantity_in_each_state[0]++;
			else quantity_in_each_state[3]++;
		}
		else
		{
			multiple=totalPoints[cnt]/3;
			remainder=totalPoints[cnt]%3;
			switch(remainder)
			{
				case 0:	if(multiple>=threshold) quantity_in_each_state[0]++;
						else if(multiple+1>=threshold) quantity_in_each_state[1]++;
						else quantity_in_each_state[2]++;
						break;
				case 1:	if(multiple+1>=threshold) quantity_in_each_state[0]++;
						else quantity_in_each_state[2]++;
						break;
				case 2:	if(multiple+1>=threshold) quantity_in_each_state[0]++;
						else if(multiple+2>=threshold) quantity_in_each_state[1]++;
						else quantity_in_each_state[2]++;
						break;
				default:break;
			}
		}
	}
	
	delete[] totalPoints;
	totalPoints=0;
	
	if(numSurprising>numDancers-quantity_in_each_state[3]) return 0;
	else if(numSurprising<quantity_in_each_state[1]) return quantity_in_each_state[0]+numSurprising;
	else return quantity_in_each_state[0]+quantity_in_each_state[1];
}

int main(int numArgs, char** args)
{
	//Check if the arguments seem rigth.
	if(numArgs>2)
	{
		printf("The only parameter accepted is the file name.\n");
		return 0;
	}
	
	//VARS
		int numCases(0);
		string strNumCases;
		string* lines(0);
		int* results(0);
		
		//Files streams and names.
		string input_file_name;
		ifstream input_file;
		string output_file_name;
		ofstream output_file;
	
	
	//Get the inpput files names, depending on the number of arguments sent.
	if(numArgs==1)
	{
		input_file_name="input.txt";
		output_file_name="output.txt";
	}
	else
	{
		input_file_name=args[1];
		output_file_name=input_file_name;
		output_file_name.replace(input_file_name.size()-3,3,"_output.out");
	}
	
	//Check if the input file exists.
	if(file_existence((char*)input_file_name.c_str())==false)
	{
		printf("The input file does not exists.\n");
		return 0;
	}
	
	//Work the input file.
	input_file.open(input_file_name.c_str(),ios::in);
	
	getline(input_file,strNumCases,(char)10);
	numCases=toInt(strNumCases);
	//getline(input_file,strNumCases);
	
	lines=new string[numCases];
	results=new int[numCases];
	
	for(register unsigned int cnt=0; cnt<numCases; cnt++)
	{
		getline(input_file,lines[cnt],(char)10);
		//getline(input_file,strNumCases);
		results[cnt]=getMaximumDancers(lines[cnt]);
	}
	
	input_file.close();
	
	//Write the output file.
	output_file.open(output_file_name.c_str(),ios::out);
	
	for(register unsigned int cnt=0; cnt<numCases; cnt++)
		output_file<<"Case #"<<cnt+1<<": "<<results[cnt]<<"\n";
	
	output_file.close();
	
	delete[] lines;
	lines=0;
	//cin.get();
}