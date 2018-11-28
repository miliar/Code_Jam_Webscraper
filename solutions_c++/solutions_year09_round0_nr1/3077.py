# include <fstream>
# include <iostream>
# include <string>

using namespace std;

int main(int argc, char* argv[])
{
	int N, D, L;
	string first_line, input;
	string *words;
	int i_word, i_input, count;
	ifstream inFile;
	ofstream outFile;
	cout << argv[1] << endl;
	cout << argv[2] << endl;
    inFile.open(argv[1]);
	outFile.open(argv[2]);
	if (!inFile.is_open()) 
	{
		cerr << "Unable to open input file " << argv[1] << endl;
		exit(1);   // call system to stop
    }
	if (!outFile.is_open()) 
	{
		cerr << "Unable to open output file " << argv[2] << endl;
		exit(1);   // call system to stop
    }
    // Initialize
	getline(inFile,first_line);
	cout << first_line << endl;
	sscanf(first_line.data(), "%d %d %d\n", &L, &D, &N);
	cout << "L=" << L << endl;
	cout << "D=" << D << endl;
	cout << "N=" << N << endl;
	words = new string[D];

	// Process each word
	for (int i=0; i<D; i++)
	{
		getline(inFile, words[i]);
		//cout << words[i] << endl;
	}
    //cout << words[D-1] << endl;

	// Process each input 

	for(int i=0; i < N; i++)
	{
		getline(inFile, input);
		//cout << input << endl;
		count = 0;
		for (int w=0; w < D; w++)
		{
			i_word = 0;
			i_input = 0;
			
			while(i_word < L)
			{
				if (input.compare(i_input, 1, "(") == 0)
				{
					i_input++;
					while(input.compare(i_input, 1, ")") != 0)
					{
						if (input.compare(i_input, 1, words[w], i_word, 1) != 0)
							i_input++;
						else
							break;
					}
					if(input.compare(i_input, 1, ")") == 0)
						break;
					else
					{
						while(input.compare(i_input, 1, ")") != 0)
							i_input++;
						i_input++;
						i_word++;
					}
				}
				else
				{
					if (input.compare(i_input, 1, words[w], i_word, 1) == 0)
					{
						i_word++;
						i_input++;
					}
					else
						break;
				}
			}
			if (i_word == L)
				count++;
		}
		cout << "Case #" << i+1 << ": " << count << endl;;
		// Write output to file
		outFile << "Case #" << i+1 << ": " << count << endl;
	}

	inFile.close();
	outFile.close();
}

//problemA from practice round of last year.

/*
# include <fstream>
# include <iostream>
# include <string>

using namespace std;
*/
/* Reverse a string
 * input   - IN
 * output  - OUT
 * length  - IN
 */
/*
void reverse_string(const char * input, char * output, int length)
{
	for (int i=0; i<length; i++)
	{
		output[i] = input[length - i - 1];
	}
}
*/

/* Find a character in an array of characters of given length
 * c       - IN 
 * str     - IN
 * length  - IN
 */
/*
int find(char c, const char * str, int length)
{
  for (int i = length-1; i>=0; i--)
  {
    if (c==str[i])
      return(i);
  }
} 
*/

/* Convert a number in given language to decimal 
 * number         - IN - number in given language
 * number_digits  - IN - number of digits in number
 * lang           - IN - input language
 * base           - IN - base of lang
 */
/*
int langToDecimal(const char *number, const int number_digits, const char *lang, int base)
{
  int output = 0;
  int *decimal_array = new int [number_digits];
  int multiplier = 1;
  cout << "base = " << base << endl;
  for (int i = number_digits-1; i >=0; i--)
  {
     decimal_array[i] = find(number[i], lang, base);
  }
  for (int i=0; i<number_digits; i++)
  {
    output +=  multiplier * decimal_array[i] ;
    multiplier *= base;
  }
  return(output);
} 

int ndigits(int decimal, const char *lang, int base)
{
	int number_digits = 0;
	while (decimal >= base)
	{
		decimal = decimal/base;
		number_digits++;
	}
	number_digits++;
	return number_digits;
}
*/

/* Convert a decimal number to number in given language
 * decimal       - IN - input decimal number
 * lang          - IN
 * base			 - IN
 * number        - OUT
 */
/*
void decimalToLang(int decimal, const char *lang, int base, char *number)
{
    int remainder, quotient, sigbit=0;	
	while (decimal >= base)
	{
		quotient = decimal/base;
	    remainder = decimal - quotient*base;
	    decimal = quotient;
		number[sigbit] = lang[remainder];
		sigbit++;
	}
	number[sigbit] = lang[decimal];
} 

int main(int argc, char* argv[])
{
	int N, decimal, output_digits;
	string input, number, input_lang, output_lang;
	char *number_reverse;
	char *output_number;
	size_t pos1,pos2;
	ifstream inFile;
	ofstream outFile;
	cout << argv[1] << endl;
    inFile.open(argv[1]);
	if (!inFile.is_open()) 
	{
		cerr << "Unable to open input file" << endl;
		exit(1);   // call system to stop
    }
    // No. of test cases
	getline(inFile,input);
	N=atoi(input.data());
	cout << "No. of test cases = " << N << endl;
	// Process each input
	for (int i=0; i < N; i++)
	{ 
		getline(inFile, input);
		cout << input << endl;
        pos1 = input.find(" ");
		number = input.substr(0,pos1);
        cout << "Input number = " << number << endl;
		pos2 = input.find(" ", pos1+1);
		input_lang = input.substr(pos1+1,pos2-pos1-1);
		cout << "Input Language = " << input_lang << endl;
		output_lang = input.substr(pos2+1);
		cout << "Output Language = " << output_lang << endl;
		number_reverse = new char[pos1];
		reverse_string(number.data(), number_reverse, pos1);
		cout << "Reverse number = " << number_reverse << endl;
		decimal = langToDecimal(number_reverse, number.length(), input_lang.data(), input_lang.length());
		cout << "Input number in decimal = " << decimal << endl;
		output_digits = ndigits(decimal, output_lang.data(), output_lang.length());
		cout << "Number digits = " << output_digits << endl;
		output_number = new char(output_digits);
		decimalToLang(decimal, output_lang.data(), output_lang.length(), output_number);
		//cout << output_number[0] << endl;
		cout << "Output number = " << output_number << endl;
		cout << endl;
	}
	inFile.close();
}
*/
