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

//Returns the lower case representation of a char, if such char is an upper case char.
char toLowerCase(char car)
{
	if((car>='A')&&(car<='Z')) return car+('a'-'A');
	else return car;
}

//Defines the bijective mapping.
void initialize_table(char* translation_table, int length)
{
	translation_table['a'-'a']='y';//
	translation_table['b'-'a']='h';//
	translation_table['c'-'a']='e';//
	translation_table['d'-'a']='s';//
	translation_table['e'-'a']='o';//
	translation_table['f'-'a']='c';//
	translation_table['g'-'a']='v';//
	translation_table['h'-'a']='x';//
	translation_table['i'-'a']='d';//
	translation_table['j'-'a']='u';//
	translation_table['k'-'a']='i';//
	translation_table['l'-'a']='g';//
	translation_table['m'-'a']='l';//
	translation_table['n'-'a']='b';//
	translation_table['o'-'a']='k';//
	translation_table['p'-'a']='r';//
	translation_table['q'-'a']='z';//
	translation_table['r'-'a']='t';//
	translation_table['s'-'a']='n';//
	translation_table['t'-'a']='w';//
	translation_table['u'-'a']='j';//
	translation_table['v'-'a']='p';//
	translation_table['w'-'a']='f';//
	translation_table['x'-'a']='m';//
	translation_table['y'-'a']='a';//
	translation_table['z'-'a']='q';//
}

//Takes a string text, and returns a string containing the traslation.
string traslation(const string text, char* translation_table)
{
	int length(text.length());
	string aux_cad;
	char lower_car;
	
	aux_cad.resize(length);
	
	for(register unsigned int cnt=0; cnt<length; cnt++)
	{
		lower_car=toLowerCase((char)text[cnt]);
		//Only english letters are processed.
		if((lower_car>='a')&&(lower_car<='z'))
			aux_cad[cnt]=translation_table[lower_car-'a'];
		else 
			aux_cad[cnt]=text[cnt];
	}
	
	return aux_cad;
}

//If a file name is sent by argument, for example 'file.txt', then we use it as input file, and return the
//output in the file 'file_output.txt'.
//Otherwise, we look for the file 'input.txt' to take it as input, and we then return the output in 'output.txt'.
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
		int table_size('z'-'a'+1);
		char* translation_table(new char[table_size]);
		
		
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
	
	//Set the translation mapping.
	initialize_table(translation_table,table_size);
	
	//Work the input file.
	input_file.open(input_file_name.c_str(),ios::in);
	
	getline(input_file,strNumCases,(char)10);
	numCases=toInt(strNumCases);
	
	lines=new string[numCases];
	
	for(register unsigned int cnt=0; cnt<numCases; cnt++)
	{
		getline(input_file,lines[cnt],(char)10);
		lines[cnt]=traslation(lines[cnt],translation_table);
	}
	
	input_file.close();
	
	//Write the output file.
	output_file.open(output_file_name.c_str(),ios::out);
	
	for(register unsigned int cnt=0; cnt<numCases; cnt++)
		output_file<<"Case #"<<cnt+1<<": "<<lines[cnt]<<"\n";
	
	output_file.close();
	
	delete[] translation_table;
	translation_table=0;
	delete[] lines;
	lines=0;
	//cin.get();
}
