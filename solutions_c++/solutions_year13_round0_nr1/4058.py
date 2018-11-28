//============================================================================
// Name        : TicTacToe.cpp
// Author      : Rahul Verma
// Version     : 1.0
// Copyright   : none
// Description : none
//============================================================================

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

string replaceChar(string str, char ch1, char ch2) {
  string temp=str;
	for (int i = 0; i < str.length(); ++i) {
    if (str[i] == ch1)
      temp[i] = ch2;
  }

  return temp;
}
string getStatus(string *input){
    for(int i=0;i<4;i++){
		if(replaceChar(input[i],'T','X')=="XXXX")
			return "X won";

	}
	for(int i=0;i<4;i++){
			if(replaceChar(input[i],'T','O')=="OOOO")
				return "O won";
		}
	for(int i=0;i<4;i++){
		if((input[0][i]=='X'||input[0][i]=='T')&&(input[1][i]=='X'||input[1][i]=='T')&&(input[2][i]=='X'||input[2][i]=='T')&&(input[3][i]=='X'||input[3][i]=='T')){
			return "X won";
		}
	}
	for(int i=0;i<4;i++){
			if((input[0][i]=='O'||input[0][i]=='T')&&(input[1][i]=='O'||input[1][i]=='T')&&(input[2][i]=='O'||input[2][i]=='T')&&(input[3][i]=='O'||input[3][i]=='T')){
				return "O won";
			}
		}
	if((input[0][0]=='X'||input[0][0]=='T')&&(input[1][1]=='X'||input[1][1]=='T')&&(input[2][2]=='X'||input[2][2]=='T')&&(input[3][3]=='X'||input[3][3]=='T')){
		return "X won";
	}
	if((input[0][0]=='O'||input[0][0]=='T')&&(input[1][1]=='O'||input[1][1]=='T')&&(input[2][2]=='O'||input[2][2]=='T')&&(input[3][3]=='O'||input[3][3]=='T')){
			return "O won";
	}

	if((input[0][3]=='X'||input[0][3]=='T')&&(input[1][2]=='X'||input[1][2]=='T')&&(input[2][1]=='X'||input[2][1]=='T')&&(input[3][0]=='X'||input[3][0]=='T')){
			return "X won";
		}
	if((input[0][3]=='O'||input[0][3]=='T')&&(input[1][2]=='O'||input[1][2]=='T')&&(input[2][1]=='O'||input[2][1]=='T')&&(input[3][0]=='O'||input[3][0]=='T')){
			return "O won";
	}

	for(int i=0;i<4;i++){
		for(int x=0;x<4;x++){
		      if(input[i][x]=='.'){
		    	  return "Game has not completed";
		      }
		}

	}
	return "Draw";
}


int main() {




	  ifstream in("a.in");
	  stringstream buffer;
	  buffer << in.rdbuf();
	  string test = buffer.str();

	  size_t pos1 = 0;
	  size_t pos2;

	  pos2=test.find('\n',0);
	  string num=test.substr(0,pos2);
      pos1 = pos2+1;
      stringstream ss;
	  ss<<num;
	  int T;
	  ss>>T;


	  string *inputs=new string[4*T];

string temp;
       cout<<endl<<T;
	    for (int x=0,y=0; x<(T*4)+T; x++){

	        pos2 = test.find("\n", pos1);
	        //search for the bar "|". pos2 will be where the bar was found.

	        temp= test.substr(pos1, (pos2-pos1)); //make a substring, wich is nothing more
	        if(temp.length()==4)
	        {
	        inputs[y]=temp;
	        y++;
	        }
	        //than a copy of a fragment of the big string.
	        pos1 = pos2+1; // sets pos1 to the next character after pos2.
	                         //so, it can start searching the next bar |.
	    }






	string *results=new string[T];
	string inputToPass[4];

	for(int i=0;i<T;i++){
		for(int y=0;y<4;y++)
			inputToPass[y]=inputs[(4*i)+y];

		results[i]=getStatus(inputToPass);
        cout<<endl<<"Case #"<<i+1<<": "<<results[i];
	}

	ofstream myfile ("a.out");
	  if (myfile.is_open())
	  {
		for(int i=0;i<T;i++){
		myfile<<"Case #"<<i+1<<": "<<results[i];
		if(i!=T-1)
			myfile<<'\n';
		}
	     myfile.close();
	  }
	  else cout << "Unable to open file";

return 0;
}

