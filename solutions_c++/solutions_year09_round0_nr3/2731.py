#include <fstream>
#include <iostream>
#include <string>

int recursive_occurrences(int target_character, int check_character, int current_occurrences, std::string target_line, std::string check_line)
{
	if(target_character >= target_line.size())
	{
		current_occurrences++;
		if(current_occurrences > 9999)
			current_occurrences = 0;
		return current_occurrences;
	}
	if(check_character >= check_line.size())
		return current_occurrences;

	if(tolower(target_line[target_character]) == tolower(check_line[check_character]))
		current_occurrences = recursive_occurrences(target_character + 1, check_character + 1, current_occurrences, target_line, check_line);
	return recursive_occurrences(target_character, check_character + 1, current_occurrences, target_line, check_line);

}

int main( int argc, char* argv[] )
{
	if ( argc != 3 )
    {
		std::cerr << "Usage: " << argv[0] << " infile outfile\n";
		return 1;
    }
  
	std::ifstream istr( argv[1] );
	if ( !istr )
    {
		std::cerr << "Could not open " << argv[1] << std::endl;
		return 1;
    }

	std::ofstream ostr( argv[2] );
	if( !ostr )
	{
		std::cerr << "Could not open " << argv[2] << std::endl;
		return 1;
	}

	std::string check_case = "welcome to code jam";
	std::string in_line;
	//read number of lines in input, unnecessary as getline is in while statement, so ignore
	getline( istr, in_line );
	int case_num = 1;
	//read each line of input, and output appropriate number of occurrences of "welcome to code jam"
	while( getline( istr, in_line ) )
	{
		int number_of_occurrences = 0;  //keep track of number of occurrences
		number_of_occurrences = recursive_occurrences(0, 0, 0, check_case, in_line);
		ostr << "Case #" << case_num << ": ";
		if(number_of_occurrences < 1000)
			ostr << 0;
		if(number_of_occurrences < 100)
			ostr << 0;
		if(number_of_occurrences < 10)
			ostr << 0;
		ostr << number_of_occurrences << std::endl;
		case_num++;
	}						

	return 0;
}