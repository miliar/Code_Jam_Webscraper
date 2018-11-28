
#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

char getLettersForIndex(char x){
string str="yhesocvxduiglbkrztnwjpfmaq";
switch(x){
 case 'a':
  return str[0];
 case 'b':
	 return str[1];
 case'c':
	 return str[2];
 case 'd':
	 return str[3];
 case 'e':
	 return str[4];
 case 'f':
	 return str[5];
 case 'g':
	 return str[6];
 case 'h':
	 return str[7];
 case 'i':
	 return str[8];
 case 'j':
	 return str[9];
 case 'k':
	 return str[10];
 case 'l':
	 return str[11];
 case 'm':
	 return str[12];
 case 'n':
	 return str[13];
 case 'o':
	 return str[14];
 case 'p':
	 return str[15];
 case 'q':
	 return str[16];
 case 'r':
	 return str[17];
 case 's':
	 return str[18];
 case 't':
	 return str[19];
 case 'u':
	 return str[20];
 case 'v':
	 return str[21];
 case 'w':
	 return str[22];
 case 'x':
	 return str[23];
 case 'y':
	 return str[24];
 case 'z':
	 return str[25];
 default:
	return x;
}
}
int main(){

ifstream input;
ofstream output("out.txt");
input.open("A-small-attempt3.in");
int numberofcases;
string linestring;
string decryptedstring;
if(input.is_open())
{
  getline(input,linestring);
  numberofcases =atoi(linestring.c_str());
  char buffer[10000];
  cout<<"numberofcases is "<<numberofcases<<endl;
  for(int i=0;i<numberofcases;i++)
  {
   input.getline(buffer,10000,'\n');
   linestring=buffer;

   decryptedstring=linestring;
   for(int l=0;l<linestring.length();l++)
	 decryptedstring[l]=getLettersForIndex(linestring[l]);

   output<<"Case #"<<i+1<<": "<<decryptedstring;
   if(i!=numberofcases-1)
	    output<<endl;
  cout<<decryptedstring<<endl;
  }




}
}