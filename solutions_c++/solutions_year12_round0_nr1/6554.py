#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main (int argc, char * const argv[]) {
	string readfromfile;
	string testString = " ";
	int count = 1;
	
	ifstream r_file("A-Small-attempt1.in.txt");
			
	getline(r_file, readfromfile);
	
	while (!r_file.eof()){
			
		cout << "Case #" << count << ": ";
		getline(r_file, readfromfile);
		
			
	    for (int i = 0; i < readfromfile.length(); i ++ ){
		    if      (readfromfile[i] == 'y')  cout << "a"; 
		    else if (readfromfile[i] == 'n')  cout << "b"; 
		    else if (readfromfile[i] == 'f')  cout << "c"; 
		    else if (readfromfile[i] == 'i')  cout << "d"; 
		    else if (readfromfile[i] == 'c')  cout << "e"; 
		    else if (readfromfile[i] == 'w')  cout << "f"; 
		    else if (readfromfile[i] == 'l')  cout << "g"; 
		    else if (readfromfile[i] == 'b')  cout << "h"; 
		    else if (readfromfile[i] == 'k')  cout << "i"; 
		    else if (readfromfile[i] == 'u')  cout << "j"; 
		    else if (readfromfile[i] == 'o')  cout << "k"; 
		    else if (readfromfile[i] == 'm')  cout << "l"; 
		    else if (readfromfile[i] == 'x')  cout << "m"; 
		    else if (readfromfile[i] == 's')  cout << "n"; 
		    else if (readfromfile[i] == 'e')  cout << "o"; 
		    else if (readfromfile[i] == 'v')  cout << "p"; 
		    else if (readfromfile[i] == 'z')  cout << "q"; 
		    else if (readfromfile[i] == 'p')  cout << "r"; 
		    else if (readfromfile[i] == 'd')  cout << "s"; 
		    else if (readfromfile[i] == 'r')  cout << "t"; 
		    else if (readfromfile[i] == 'j')  cout << "u"; 
		    else if (readfromfile[i] == 'g')  cout << "v"; 
		    else if (readfromfile[i] == 't')  cout << "w"; 
		    else if (readfromfile[i] == 'h')  cout << "x"; 
		    else if (readfromfile[i] == 'a')  cout << "y"; 
		    else if (readfromfile[i] == 'q')  cout << "z"; 
		    else if (readfromfile[i] == ' ')  cout << " "; 
	    }// inner for loop
		
		count ++;			
	
	    cout << endl;
	
	} // while loop	
	
	r_file.close();
	
	return 0;
	
} // main












