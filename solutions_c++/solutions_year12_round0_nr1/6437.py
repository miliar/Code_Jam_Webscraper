#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;

void main()
{

	map <char,char> lang;
	map<char,char>::iterator iter;
	
	lang['y']='a';
	lang['n']='b';
	lang['f']='c';
	lang['i']='d';
	lang['c']='e';
	lang['w']='f';
	lang['l']='g';
	lang['b']='h';
	lang['k']='i';
	lang['u']='j';
	lang['o']='k';
	lang['m']='l';
	lang['x']='m';
	lang['s']='n';
	lang['e']='o';
	lang['v']='p';
	lang['z']='q';
	lang['p']='r';
	lang['d']='s';
	lang['r']='t';
	lang['j']='u';
	lang['g']='v';
	lang['t']='w';
	lang['h']='x';
	lang['a']='y';
	lang['q']='z';
		
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("out.txt");
	
	int n;//testcases
	in>>n;
	int j=0;

	string input;
	 getline(in,input); // Saves the line in STRING.
 while(j<n)
 {
	
	 
        while(!in.eof()) // To get you all the lines.
		{  
	        getline(in,input);
			if(input.length()<=1)
				continue;
		out<<"Case #"<<j+1<<": ";
		
		for(int i=0;i<input.length();i++)
		{
			
			if(input[i]==' ')
			{
				out<<" ";
				
			}
			else
			{
				out<<lang.find(input[i])->second;
			}
			
		}
		out<<endl;
		++j;
	}

	
}
	in.close();
	out.close();

}