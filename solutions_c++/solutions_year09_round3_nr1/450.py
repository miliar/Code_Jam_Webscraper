#include<iostream>
#include<string>
using namespace std;

int rindex(char in)
{
	if ( in >= '0' && in <= '9' )
		return in-'0';
	else
		return in-'a'+10;
}

void main()
{
	int testcase;
	cin >> testcase;
	for(int t=0; t < testcase; t++) {
		string input;
		string output;
		cin >> input;
		output=input;

		int inputsize = input.size();
		int base=0;
		int value[36];
		for(int i=0;i<36;i++)
			value[i]=-1;

		value[ rindex(input[0]) ] = 1;
		output[0] = 1;
		for(int i=1;i < inputsize;i++) {

			if( value[ rindex(input[i]) ]  >= 0 ) {
				output[i] = value[ rindex(input[i]) ];
			} else {

				value[ rindex(input[i]) ] = base;
				output[i] = base;
				if ( base == 0 )
					base = 2;
				else
					base++;
			}

		}
		//output
		if ( base == 0 )
			base = 2;

		long long result=0;
		for(int i=0;i < inputsize;i++) {
			result = result*base + output[i];
		}
		cout << "Case #" << t+1 << ": " << result << endl;
	}
}