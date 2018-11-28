#include<iostream>
#include<fstream>
#include<string.h>
#include<cctype>
#include<stdlib.h>
using namespace std;

char decode(char google_char) {
 char decoded_char = google_char;
	switch (toupper(google_char))
	{
	case 'Y' : decoded_char =  'A';
	break;
	case 'N' : decoded_char =  'B';
	break;
	case 'F' : decoded_char =  'C';
	break;
	case 'I' : decoded_char =  'D';
	break;
	case 'C' : decoded_char =  'E';
	break;
	case 'W' : decoded_char =  'F';
	break;
	case 'L' : decoded_char =  'G';
	break;
	case 'B' : decoded_char =  'H';
	break;
	case 'K' : decoded_char =  'I';
	break;
	case 'U' : decoded_char =  'J';
	break;
	case 'O' : decoded_char =  'K';
	break;
	case 'M' : decoded_char =  'L';
	break;
	case 'X' : decoded_char =  'M';
	break;
	case 'S' : decoded_char =  'N';
	break;
	case 'E' : decoded_char =  'O';
	break;
	case 'V' : decoded_char =  'P';
	break;
	case 'Z' : decoded_char =  'Q';
	break;
	case 'P' : decoded_char =  'R';
	break;
	case 'D' : decoded_char =  'S';
	break;
	case 'R' : decoded_char =  'T';
	break;
	case 'J' : decoded_char =  'U';
	break;
	case 'G' : decoded_char =  'V';
	break;
	case 'T' : decoded_char =  'W';
	break;
	case 'H' : decoded_char =  'X';
	break;
	case 'A' : decoded_char =  'Y'; 
	break;
	case 'Q' : decoded_char =  'Z';
	}

	return tolower(decoded_char);

}

int main(int argc,char* argv[]) {
if (argc < 2) {
cout 
<< "Please provide input file, quitting..." << endl;
return(1);}
ifstream fin;
fin.open(argv[1]);
if(!fin.is_open()){
cout << "Error opening " << argv[1] << ", quitting..."<<endl;
return(1);}
int cases;
string line;
getline(fin,line);
cases = atoi(line.c_str());
for(int i=0;i<cases;i++){
getline(fin,line);
cout <<"Case #"<<i+1<<": "; 
for(int ch = 0;ch<line.length();ch++)cout << decode((char)line[ch]);
cout << endl;
}

return(0);
}
