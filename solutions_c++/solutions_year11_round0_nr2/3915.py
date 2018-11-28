#include <iostream>
using namespace std;
#include<fstream>
#include <string>
void main(){
	string infile,outfile;
	ifstream source;
	ofstream target;
	infile = "B-small-attempt4.in";
	outfile = "output.txt";
	source.open(infile.c_str());
	target.open(outfile.c_str());
	int C,D,N;
	char ch_combine,ch_base1,ch_base2;
	char ch_oppose1, ch_oppose2;
	char ch[11];
	bool flag_combine1 ;
	bool flag_combine2 ;
	bool flag_oppose1 ;
	bool flag_oppose2;
	char output[101];
	int j=0,k=1;
	int outputcounter=1;
	int T;
	source >> T;
	for ( int e = 1; e<=T;e++)
	{
		flag_combine1 =false;
		flag_combine2 = false;
		flag_oppose1 = false;
		flag_oppose2=false;
		j=0;
		k=1;
		ch_oppose1 = 'Ì';
		ch_oppose2 = '!';
		ch_combine = '@';
		ch_base1 = '#';
		ch_base2 = '*';
		outputcounter=1;

	source >> C;
	if( C == 1)
	{
		source >> ch_base1;
		source >> ch_base2;
		source >> ch_combine;
	}

	source >> D;

	if ( D == 1)
	{
		source >> ch_oppose1;
		source >> ch_oppose2;
	}

	source >> N;

	for ( int i =0; i < N; i ++)
	{
		source >> ch[i];
		output[outputcounter] = ch[i];

		

		if ( ((ch[i] == ch_base1 ) && flag_combine2) || ( (ch[i] == ch_base2 ) && flag_combine1))
		{
			outputcounter = outputcounter-1;
			output[outputcounter] = ch_combine;
			if ( i -k == 1)
			{
				flag_oppose1 = false;
				flag_oppose2 = false;
			}
			ch[i] = 'Ì';
		}


		
		if ((( ch[i] == ch_oppose1) && flag_oppose2) || ((ch[i] == ch_oppose2) && ( flag_oppose1)))
		{
			outputcounter =0;
			
				flag_combine1 = false;
				flag_oppose1 = false;
				flag_oppose2 = false;
				flag_oppose1 = false;
				ch[i] = '%';
			
		}
		
			
		

		if (( ch[i] == ch_base1) || ( ch[i] == ch_base2))
		{
			if ( ch[i] == ch_base1) flag_combine1 = true;
			if ( ch[i] == ch_base2) flag_combine2 = true;
			j=i;
		}
		else
			{flag_combine1 =false;
		flag_combine2 = false;
		}	


		if (( ch[i] == ch_oppose1) || ( ch[i] == ch_oppose2))
		{
			if ((ch[i] == ch_oppose1) && !(flag_oppose1 == true))
			{
				flag_oppose1 = true;
				k =i;
			}
			if ((ch[i] == ch_oppose2) && !(flag_oppose2 == true))
			{
				flag_oppose2 = true;
				k = i;
			}
		}

		outputcounter++;

		
		}

	/*if( (output[outputcounter] == ch_base1) )
	{
		if ( output[outputcounter-1] == ch_base2 )
			output[outputcounter-1] = ch_combine;
	}
	else 
		if ((output[outputcounter] == ch_base2) &&( output[outputcounter-1] == ch_base1))
			output [ outputcounter-1] = ch_combine;
			*/
	target << "Case #"<<e<<": [" ;
	for ( int h =1; h <outputcounter; h++)
	{	
		target << output[h];
		if ( ! ((outputcounter-h) == 1) )
			target <<", ";
	}
	target <<"]" << endl;

	
	}
	}

	
	