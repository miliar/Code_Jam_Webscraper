//// Fig. 22.6: fig22_06.cpp
//// Printing an unsigned integer in bits.
//#include <iostream>
//using std::cout;
//using std::cin;
//using std::endl;
//
//#include <iomanip>
//using std::setw;
//
//void displayBits( unsigned ); // prototype
//
//int main()
//{
//	unsigned inputValue; // integral value to print in binary
//
//	cout << "Enter an unsigned integer: ";
//	cin >> inputValue;
//	displayBits( inputValue );
//	return 0;
//} // end main
//
//// display bits of an unsigned integer value
//void displayBits( unsigned value )
//{
//	const int SHIFT = 8 * sizeof( unsigned ) - 1;
//	const unsigned MASK = 1; //<< SHIFT;
//
//	cout << setw( 10 ) << value << " = ";
//
//	// display bits
//	for ( unsigned i = 1; i <= SHIFT + 1; i++ )
//	{
//		cout << ( value & MASK ? '1' : '0' );
//		value >>= 1; // shift value left by 1
//
//		if ( i % 8 == 0 ) // output a space after 8 bits
//			cout << ' ';
//	} // end for
//
//	cout << endl;
//} // end function displayBits


#include<iostream>
#include<fstream>
using namespace std;

bool check(unsigned int snapper,__int32 snaps);

void main()
{
	unsigned short number_of_inputs,count=1;
	char *input_file=new char[20];
	char *output_file=new char[20];

	strcpy(input_file,"A-large.in");
	strcpy(output_file,"output.txt");
	
	ifstream fin;
	fin.open(input_file);

	ofstream fout;
	fout.open(output_file);
	
	fin>>number_of_inputs;
	//cout<<number_of_inputs;

	while(number_of_inputs--!=0)
	{
		
		fout<<"Case #"<<count++<<": ";
		unsigned short snappers;
		__int32 snaps;//,temp_snaps;
		bool flag=true;

		fin>>snappers;
		fin>>snaps;

		//unsigned int *snap_array=new unsigned int[snaps];

		/*temp_snaps=snappers;


		while(temp_snaps--)
		{
			short c=snaps<<1; 
			if(c!=1)
			{
				flag=false;
				break;
			}
		}*/

		flag=check(snappers,snaps);
		
		if(flag==true)
			fout<<"ON";
		else
			fout<<"OFF";

		fout<<endl;
	}
}

bool check(unsigned int snapper,__int32 snaps)
{
		//unsigned int temp_snaps=snappers;
	__int32 SHIFT = 8 * sizeof(__int32)-1;
	__int32 MASK = 1 ;//<< SHIFT;

	for(unsigned i=1; i<=snapper; i++)
	{
		unsigned char flag= (snaps & MASK ? '1' : '0' );
		if(flag=='0')
		{
			return false;
		}
		snaps >>= 1; // shift value left by 1
	}
	return true;
}