#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	
	char transfer(char a);
	ofstream fo("output.txt");
	ifstream fi("data.txt");
	
	string lines;
    getline(fi,lines);
    int numbers;
	if(lines.size()>1)
	    numbers=(lines[0]-'0')*10 + (lines[1]-'0')*1;
	for(int i=0;i<numbers;i++)
	{
		string str="";
		getline(fi,str,'\n');
		cout << str << endl;
		string str2=str;
		for(int j =0;j<str.size();j++)
		{
			str2[j] = transfer(str[j]);
		}
		cout << str2 << endl;
		fo << "Case #" << i+1 << ":" << " " << str2 << endl;
	}
	fi.close();
	fo.close();
	return 0;

}
char transfer(char a)
{
	switch (a)
	{
	  case 'a':
         return 'y' ;
	  case 'b':
		 return 'h';
	  case 'c':
         return 'e' ;
	  case 'd':
		 return 's';
	  case 'e':
         return 'o' ;
	  case 'f':
		 return 'c';
	  case 'g':
         return 'v' ;
	  case 'h':
		 return 'x';
	  case 'i':
         return 'd' ;
	   case 'j':
         return 'u' ;
	  case 'k':
		 return 'i';
	  case 'l':
         return 'g' ;
	  case 'm':
		 return 'l';
	  case 'n':
         return 'b' ;
	  case 'o':
		 return 'k';
	  case 'p':
         return 'r' ;
	  case 'q':
		 return 'z';
	  case 'r':
		  return 't';
	   case 's':
		 return 'n';
	  case 't':
         return 'w' ;
	  case 'u':
		 return 'j';
	  case 'v':
		  return 'p';
	  case 'w':
		 return 'f';
	  case 'x':
		  return 'm';
	  case 'y':
		 return 'a';
	  case 'z':
		  return 'q';
	}
	
}