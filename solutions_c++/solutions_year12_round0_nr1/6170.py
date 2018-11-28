#include <iostream>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>


using namespace std;


class Speaking{

	
	string output;
	public :
		Speaking(string);
		~Speaking ();
		string Speak ();

};


Speaking::Speaking (string input) {

	output = input;

}

Speaking::~Speaking () {

  delete &output[0];

}

string Speaking::Speak(){

	
	 int length = output.length();

	 for(int i = 0 ; i < length ; i++ )
	 {
			if(output[i] == 'a'){
				output[i] = 'y';
			}
			else if (output[i] == 'b'){
				output[i] = 'h';
			}else if (output[i] == 'c'){
				output[i] = 'e';
			}else if (output[i] == 'd'){
				output[i] = 's';
			}else if (output[i] == 'e'){
				output[i] = 'o';
			}else if (output[i] == 'f'){
				output[i] = 'c';
			}else if (output[i] == 'g'){ 
				output[i] = 'v';
			}else if (output[i] == 'h'){
				output[i] = 'x';
			}else if (output[i] == 'i'){
				output[i] = 'd';
			}else if (output[i] == 'j'){
				output[i] = 'u';
			}else if (output[i] == 'k'){
				output[i] = 'i';
			}else if (output[i] == 'l'){
				output[i] = 'g';
			}else if (output[i] == 'm'){
				output[i] = 'l';
			}else if (output[i] == 'n'){
				output[i] = 'b';
			}else if (output[i] == 'o'){
				output[i] = 'k';
			}else if (output[i] == 'p'){
				output[i] = 'r';
			}else if (output[i] == 'q'){ 
				output[i] = 'z';
			}else if (output[i] == 'r'){
				output[i] = 't';
			}else if (output[i] == 's'){
				output[i] = 'n';
			}else if (output[i] == 't'){
				output[i] = 'w';
			}else if (output[i] == 'u'){
				output[i] = 'j';
			}else if (output[i] == 'v'){
				output[i] = 'p';
			}else if (output[i] == 'w'){
				output[i] = 'f';
			}else if (output[i] == 'x'){
				output[i] = 'm';
			}else if (output[i] == 'y'){
				output[i] = 'a';
			}else if (output[i] == 'z'){ 
				output[i] = 'q';
			}
	 }



	return output;
}

int main  ()
{
  int method = 0;
  int i = 0;
  vector<string> inputAll;

  if(method = 0 ){
  cin >> i;
	  

		for( int j = 0 ; j <= i; j ++){

		  char input [256];

		 cin.getline(input,256);
		  inputAll.push_back(input);
	  }
  }



  if(method = 1 ){
   ifstream  myfile;
	  myfile.open ("A-small-attempt.in");
	  myfile >> i;

	  for( int j = 0 ; j <= i; j ++){

		  string input;

		  getline(myfile,input);
		  cout << input ;
		  inputAll.push_back(input);
	  }

	  myfile.close();
  }


   vector<string>::iterator iter;
   int k = -1;
   ofstream writeme;
   writeme.open ("out.txt");
   writeme.clear();
   for (iter = inputAll.begin() ; iter != inputAll.end(); iter++ )
   {
		k++;

		if(k > 0){

		string show = *iter; 
		Speaking *myspeak = new Speaking(show);
		writeme << "Case #"<< k << ": " << myspeak->Speak() << endl;

		}
	
   }

   writeme.close();
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
*/

  cin >> i;

  return 0;

}

