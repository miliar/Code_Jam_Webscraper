
#include<iostream>
#include<string>
#include<fstream>
#include<stdio.h>

using namespace std;

int decode_map[26] = {0};
void prepare_decode_map()
{
	char  encode_str[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi \
				rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd \
				de kr kd eoya kw aej tysr re ujdr lkgc jv ";
	char  decode_str[] = "our language is impossible to understand \
				there are twenty six factorial possibilities \
				so it is okay if you want to just give up" ;

	for ( int i = 0; i < 26; i++)
	{
		decode_map[i] = -1;
	}
	
	int i = 1	;
	int len = strlen(encode_str);
	while(i < len )
	{
		// Check if it a lowercase alphabet
		if (encode_str[i] >= 'a' && encode_str[i] <= 'z' ) 
		{
			// Populate the decode_map
			if ( -1 == decode_map[encode_str[i] -'a' ])
			{
				decode_map[encode_str[i] -'a'] = decode_str[i] -'a';
			}
		}
		++i;
	}

	/*for ( int i = 0 ; i < 26; i++)
	{
		printf("\n decode_map[%d]: %d",i,decode_map[i]);
	}*/
	// Found all the mappings except q and z, since it is onto mapping
	// they are maping of each other
	decode_map[16] = 25;
	decode_map[25] = 16;
}


void decode_message(const char * encdStr, char * decodeStr)
{
	strcpy(decodeStr,encdStr);
	int len = strlen (decodeStr);
	for ( int i = 0; i < len; i++)
	{	
		char char_to_convert = decodeStr[i];
		// not a space
		if ( char_to_convert != ' ')
		{
			decodeStr[i]  =  decode_map[char_to_convert - 'a'] + 'a' ; 
		}
	}
	cout << " decoded message " << decodeStr <<endl;

}

int main(int argc, char** argv)
{
	prepare_decode_map();
	int total_inputs = 0;
	
	if ( argc < 2 ) 
	{
		cout << " Usage SpeakingTongues.exe inputFileName";
		exit(-1);
	}
	string filename = argv[1];
	ifstream inFile;
	ofstream outFile;
	inFile.open(filename.c_str());
	outFile.open("I:\\CodJam\\out-Googlers.txt");
	
	if(inFile.is_open())
	{
		string line;
		// First line is no of inputs
		getline(inFile,line);
		total_inputs  = atoi(line.c_str());
		int count = 1;
		while(inFile.good() && count <= total_inputs)
		{
			char buf[512] ={0};
			char message[101] = {0};
			getline(inFile,line);
			decode_message(line.c_str(),message);
			sprintf(buf,"Case #%d: %s \n",count,message);
			if ( outFile.is_open() && outFile.good())
			{
				outFile <<buf;
			}
			count++;
		}
		inFile.close();
		outFile.close();
	
	}	

}