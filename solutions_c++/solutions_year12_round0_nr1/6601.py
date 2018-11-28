#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void parseInput(string file);
void translate(vector<string> v);
void print(vector<string> v);

int num_cases;
vector<string> input;
vector<string> output;

int main(int argc, char* argv[]) {

  parseInput(argv[1]);
  
  //cout << "Num cases: " << num_cases << endl;
  //print(input);
  //cout << "input size: " <<input.size() << endl;

  translate(input);
  
  print(output);

  return 0;
}

void parseInput(string file) {
	
	string buffer;
	
	ifstream myfile(file.c_str());
	if (myfile.is_open()) {
		
		myfile >> buffer;
		num_cases = atoi(buffer.c_str());
		if ( num_cases == 0 ) {
			cerr << "What? No test cases?" << endl;
			exit(1);
		}
		//eat newline
    getline(myfile,buffer);
		
		for ( int i = 0 ; i < num_cases ; i++ ) {
      getline(myfile,buffer);
      input.push_back(buffer.c_str());
		}
		myfile.close();
	}
	else {
		cerr << "Problem opening file " << file << "." << endl;
		exit(1);
	}
}

void translate(vector<string> v) {
  
  for ( int i = 0 ; i < v.size() ; i++ ) {
    output.push_back("");
    for ( int j = 0 ; j < v[i].size() ; j++ ) {
      switch ( tolower(v[i][j]) ) {
        case 'y':
            output[i] += "a";
            break;
        case 'n':
            output[i] += "b";
            break;
        case 'f':
            output[i] += "c";
            break;
        case 'i':
            output[i] += "d";
            break;
        case 'c':
            output[i] += "e";
            break;
        case 'w':
            output[i] += "f";
            break;
        case 'l':
            output[i] += "g";
            break;
        case 'b':
            output[i] += "h";
            break;
        case 'k':
            output[i] += "i";
            break;
        case 'u':
            output[i] += "j";
            break;
        case 'o':
            output[i] += "k";
            break;
        case 'm':
            output[i] += "l";
            break;
        case 'x':
            output[i] += "m";
            break;
        case 's':
            output[i] += "n";
            break;
        case 'e':
            output[i] += "o";
            break;
        case 'v':
            output[i] += "p";
            break;
        case 'z':
            output[i] += "q";
            break;
        case 'p':
            output[i] += "r";
            break;
        case 'd':
            output[i] += "s";
            break;
        case 'r':
            output[i] += "t";
            break;
        case 'j':
            output[i] += "u";
            break;
        case 'g':
            output[i] += "v";
            break;
        case 't':
            output[i] += "w";
            break;
        case 'h':
            output[i] += "x";
            break;
        case 'a':
            output[i] += "y";
            break;
        case 'q':
            output[i] += "z";
            break;
        default:
            output[i] += " ";
      } //end case
      
    } //end j loop
    
  } //end i loop
  
}

void print(vector<string> v) {
  
  for ( int i = 0 ; i < v.size() ; i++ ) {
    cout << "Case #" << i+1 << ": " << v[i] << endl;
  }
  
}
