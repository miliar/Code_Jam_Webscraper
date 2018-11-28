#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main(int argc, char* argv[])
{
	char arr[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

	char arr2[] =  {'y', 'n',  'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};

	map<char, char> alphabet;
	for(int i = 0; i<26; i++)
	{
		alphabet[arr2[i]] = arr[i];
	}
	char* input = "A-small-attempt2.in";
	char* output;
	
	string line;
	ifstream myfile (input);

	ofstream myfileout ("A-small-attempt2.out");
	
	if (myfile.is_open())
	{
		getline (myfile,line);
		//cout << line << endl;
		int lineNo = atoi(line.c_str());
		output = (char*) malloc(sizeof(char)*lineNo*100); 
	
		int i = 1;
		while ( myfile.good())
		{
		  getline (myfile,line);	
		  
		  string::iterator it;
		  myfileout <<"Case #"<<i<<": ";
		  for ( it=line.begin() ; it < line.end(); it++ )
		  {
			  if(*it == ' ')
			  {
				myfileout << " ";
			  }
			  else
			  {
				 myfileout << alphabet.find(*it)->second;
			  }
		  }
		  myfileout<<"\n";
		  i++;
		  /*while( line.max_sizec_str()[i]!=)
		  {
			printf("%c", alphabet.find(line.c_str()[i])->second);
			i++;
		  }*/
		  
		  //output[i] = alphabet.find(line.c_str()[i]); 
		}
		myfile.close();
	}

  else cout << "Unable to open file"; 


  myfileout.close();

}