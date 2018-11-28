#include <iostream>
#include <string>
#include <fstream>
#include <sstream> //For the stringstream class.
#include <stdarg.h> //For the indefinite arguments
#include <iomanip>

using namespace std;


struct	instanceType
{
	string&		operator[](int index)
	{
		return lines[index];
	}
	
	instanceType()
	{
	}
	
	string	lines[4];
};


struct	resultType
{
	resultType(int r)
	{
		result=r;
	}
	
	resultType()
	{
		result=-1;
	}
	
	int		result;
};


//****************************************


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
int toInt(const string& text)
{
	int number;
	stringstream value (stringstream::in | stringstream::out);
	//Insert the string with the value in the string-stream interface.
	value<<text;
	//Get the nomber in int format;
	value>>number;
	return number;
}


//Get the integer values from the stream in the different arguments.
void getIntVars(stringstream& values, int num, ...) 
{
	va_list list;
	int* arg;
	
	va_start(list, num);

	for(register unsigned int cnt=0; cnt<num; cnt++)
	{
		arg = va_arg(list, int*);
		values>>*arg;
	}

	va_end(list);
}

//Get th double values from the stream in the different arguments.
void getDoubleVars(stringstream& values, int num, ...) 
{
	va_list list;
	double* arg;
	
	va_start(list, num);

	for(register unsigned int cnt=0; cnt<num; cnt++)
	{
		arg = va_arg(list, double*);
		values>>*arg;
	}

	va_end(list);
}


//Get the integer values from the stream in the array.
void getIntArr(stringstream& values, int num, int* arr)
{
	for(register unsigned int cnt=0; cnt<num; cnt++)
		values>>arr[cnt];
}

//Get the double values from the stream in the array.
void getDoubleArr(stringstream& values, int num, double* arr)
{
	for(register unsigned int cnt=0; cnt<num; cnt++)
		values>>arr[cnt];
}


//The solver.
resultType	solve(instanceType&	instance)
{
	resultType		solution;
	int				sum=0;
	bool			a_T(false);
	bool			a_dot(false);

	//Horizontal
	for(int cnt_r=0; cnt_r<4; cnt_r++)
	{
		sum=0;
		a_T=false;
		for(int cnt_c=0; cnt_c<4; cnt_c++)
		{
			switch((char)instance[cnt_r][cnt_c])
			{
				case 'X':sum+=1; break;
				case 'O':sum+=-1; break;
				case '.':a_dot=true; break;
				case 'T':a_T=true;  break;
			}
		}
		
		if((sum==4)||(sum==3 && a_T))	return resultType(0);
		if((sum==-4)||(sum==-3 && a_T))	return resultType(1);
	}
	
	//Vertical
	for(int cnt_c=0; cnt_c<4; cnt_c++)
	{
		sum=0;
		a_T=false;
		for(int cnt_r=0; cnt_r<4; cnt_r++)
		{
			switch((char)instance[cnt_r][cnt_c])
			{
				case 'X':sum+=1; break;
				case 'O':sum+=-1; break;
				case 'T':a_T=true;  break;
			}
		}
		
		if((sum==4)||(sum==3 && a_T))	return resultType(0);
		if((sum==-4)||(sum==-3 && a_T))	return resultType(1);
	}
	
	//Diagonals.
	sum=0;
	a_T=false;
	for(int cnt_d=0; cnt_d<4; cnt_d++)
	{
		switch((char)instance[cnt_d][cnt_d])
		{
			case 'X':sum+=1; break;
			case 'O':sum+=-1; break;
			case 'T':a_T=true;  break;
		}
	}
	if((sum==4)||(sum==3 && a_T))	return resultType(0);
	if((sum==-4)||(sum==-3 && a_T))	return resultType(1);
	
	sum=0;
	a_T=false;
	for(int cnt_d=0; cnt_d<4; cnt_d++)
	{
		switch((char)instance[cnt_d][3-cnt_d])
		{
			case 'X':sum+=1; break;
			case 'O':sum+=-1; break;
			case 'T':a_T=true;  break;
		}
	}
	if((sum==4)||(sum==3 && a_T))	return resultType(0);
	if((sum==-4)||(sum==-3 && a_T))	return resultType(1);
	
	
	return resultType((a_dot ? 3 : 2));
}


void	readInstace(ifstream& input_file, instanceType&	instance)
{
	for(int cnt=0; cnt<4; cnt++)
		input_file>>instance[cnt];
}


void	writeSolution(ofstream& output_file, resultType& solution, int numCase, bool winEOL=false)
{
	output_file<<"Case #"<<numCase<<": ";
	
	switch(solution.result)
	{
		case 0:output_file<<"X won"; break;
		case 1:output_file<<"O won"; break;
		case 2:output_file<<"Draw"; break;
		case 3:output_file<<"Game has not completed"; break;
	}
	
	output_file<<(winEOL ? "\r\n" : "\n");
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
		int				numCases(0);
		instanceType	instance;
		resultType*		solutions(0);
		bool			winEOL(true);
		
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
	//Read the number of cases.
	input_file>>numCases;
	//Get space for the solutions.
	solutions=new resultType[numCases];
	
	//*********************
	//*********************
	//INPUT
	
	//Solve the instances.
	for(int cnt_cases=0; cnt_cases<numCases; cnt_cases++)
	{
		readInstace(input_file, instance);
		solutions[cnt_cases]=solve(instance);
	}
	
	input_file.close();
	
	//*********************
	//*********************
	//OUTPUT
	
	//Write the output file.
	output_file.open(output_file_name.c_str(),ios::out);
	
	for(int cnt_solutions=0; cnt_solutions<numCases; cnt_solutions++)
		writeSolution(output_file, solutions[cnt_solutions], cnt_solutions+1, winEOL);
	
	output_file.close();
	
	//*********************
	//*********************
	
	delete[] solutions;
	solutions=0;
	
	//cin.get();
}







