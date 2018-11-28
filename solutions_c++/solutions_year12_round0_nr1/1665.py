#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
	 {
		 	ifstream in;
	   in.open("A-small-attempt3.in");
	   ofstream out;
  out.open ("Answer.txt");
	   int T;
	   string line;
	   in>>T;
	   getline (in,line);
for(int i=0;i<T;i++)
{
	out<<"Case #"<<i+1<<": ";
	getline (in,line);
	for(int x=0;x<line.size();x++)
	{
		if(line[x]== 'a' ) 
			out<<'y';
		if(line[x]== 'b' ) 
			out<<'h';
		if(line[x]==' ' ) 
			out<<" ";
		if(line[x]== 'c' ) 
			out<<'e';
		if(line[x]== 'd' ) 
			out<<'s';
		if(line[x]== 'e' ) 
			out<<'o';
		if(line[x]== 'f' ) 
			out<<'c';
		if(line[x]== 'g' ) 
			out<<'v';
		if(line[x]== 'h' ) 
			out<<'x';
		if(line[x]== 'i' ) 
			out<<'d';
		if(line[x]== 'j' ) 
			out<<'u';
		if(line[x]== 'k' ) 
			out<<'i';
		if(line[x]== 'l' ) 
			out<<'g';
		if(line[x]== 'm' ) 
			out<<'l';
		if(line[x]== 'n' ) 
			out<<'b';
		if(line[x]== 'o' ) 
			out<<'k';
		if(line[x]== 'p' ) 
			out<<'r';
		if(line[x]== 'q' ) 
			out<<'z';
		if(line[x]== 'r' ) 
			out<<'t';
		if(line[x]== 's' ) 
			out<<'n';
		if(line[x]== 't' ) 
			out<<'w';
		if(line[x]== 'u' ) 
			out<<'j';
		if(line[x]== 'v' ) 
			out<<'p';
		if(line[x]== 'w' ) 
			out<<'f';
		if(line[x]== 'x' ) 
			out<<'m';
		if(line[x]== 'y' ) 
			out<<'a';
		if(line[x]== 'z' ) 
			out<<'q';
	}
	if(i!=T-1)
	out<<endl;

}

	return 0;

  
     }
  
