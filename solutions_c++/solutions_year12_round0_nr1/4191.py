#include <iostream>

// basic file operations
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
enum{
	a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,z,w
};
char letters[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','w'};
void main()
{
	ifstream in ("input.in");
	ofstream out("output.out");

	int T;
	int N;
	
	in>>T;
	string str;
	getline(in,str);

	for(int Case = 1;Case<=T;Case++)
	{

		getline(in,str);
		for(int i=0;i<str.length();i++)
		{
			switch (str[i])
			{
			case 'a':
				str[i] = 'y';
				break;
			case 'b':
				str[i] = 'h';
				break;
			case 'c':
				str[i] = 'e';
				break;
			case 'd':
				str[i] = 's';
				break;
			case 'e':
				str[i] = 'o';
				break;
			case 'f':
				str[i] = 'c';
				break;
			case 'g':
				str[i] = 'v';
				break;
			case 'h':
				str[i] = 'x';
				break;
			case 'i':
				str[i] = 'd';
				break;
			case 'j':
				str[i] = 'u';
				break;
			case 'k':
				str[i] = 'i';
				break;
			case 'l':
				str[i] = 'g';
				break;
			case 'm':
				str[i] = 'l';
				break;
			case 'n':
				str[i] = 'b';
				break;
			case 'o':
				str[i] = 'k';
				break;
			case 'p':
				str[i] = 'r';
				break;
			case 'q':
				str[i] = 'z';
				break;
			case 'r':
				str[i] = 't';
				break;
			case 's':
				str[i] = 'n';
				break;
			case 't':
				str[i] = 'w';
				break;
			case 'u':
				str[i] = 'j';
				break;
			case 'v':
				str[i] = 'p';
				break;
			case 'x':
				str[i] = 'm';
				break;
			case 'y':
				str[i] = 'a';
				break;
			case 'z':
				str[i] = 'q';
				break;
			case 'w':
				str[i] = 'f';
				break;
			default:
				break;
			}


		}
			out<<"Case #"<<Case<<": "<<str<<endl;
	}
	in.close();
	out.close();
}