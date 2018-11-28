#include <iostream> 
#include <fstream>
#include <string>

#define TTMAX 30
#define GMAX  100 

using namespace std;

char pass(char);
void convert(string*,int size);


int main(){

	string line[GMAX];
	int input = 0,i = 0;
	int sayac = 0;
	/* Open file and read line*/
	ifstream encryptedText("A-small-attempt0.in");

	while ( 1 )
	{
		if(encryptedText.eof()) // if it is end of file, break the loop
			break;
	    getline(encryptedText, line[i]); // Get line
	    i++;
    }
	
	input = atoi(line[0].c_str()); // string to int
	encryptedText.close(); // Close file
	
	/* ### Open file and read line ###*/
	
	/* Get line, decryption it and write it to file*/
	
	
	for(int i = 1; i <= input; i++)
	{		
		convert(line,line[i].size());		
	}
	
	/* ### Get line, decryption it and write it to file ### */ 	
	cout<<endl;
	system("PAUSE");
	return 0;
}

char pass(char a){
	
	switch(a){
        case 'y':
            return 'a';
            break;
        case 'n':
            return 'b';
            break;
        case 'f':
            return 'c';
            break;
        case 'i':
            return 'd';
            break;
        case 'c':
            return 'e';
            break;
        case 'w':
            return 'f';
            break;
        case 'l':
            return 'g';
            break;
        case 'b':
            return 'h';
            break;
        case 'k':
            return 'i';
            break;
        case 'u':
            return 'j';
            break;
        case 'o':   
            return 'k';  
            break;
        case 'm':
            return 'l';
            break;
        case 'x':
            return 'm';
            break;
        case 's':
            return 'n';
            break;
        case 'e':
            return 'o';
            break;
        case 'v':
            return 'p';
            break;
        case 'z':
            return 'q';
            break;
        case 'p':
            return 'r';
            break;
        case 'd':
            return 's';
            break;
        case 'r': 
            return 't'; 
            break;
        case 'j':
            return 'u';
            break;
        case 'g':
            return 'v';
            break;
        case 't':
            return 'w';
            break; 
        case 'h':
            return 'x';
            break;
        case 'a':
            return 'y';
            break;
        case 'q':
            return 'z';
            break;
        default:
            return ' ';
    }
}

void convert(string *line,int size)
{	
	ofstream decryptionText("sifresiz.txt",ios::app);
	static int sayac;
	sayac++;
	decryptionText << "Case #"<<sayac<<": ";
	for(int i = 0; i < size; i++)
	{
		decryptionText << pass(line[sayac][i]);
	}
	decryptionText << endl;
	decryptionText.close();
}