#include<fstream>
#include<string.h>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int n ;
char Data[102];
int main()
{
	in >> n;
	int i,j;
	for(i=0;i<n+1;i++)
	{
		if(i>1)
		{
			out << "\n";
		}
		if(i>0)
			out << "Case #" << i << ": ";
		in.getline(Data,101);
		int a = strlen(Data);
		for(j=0;j<a;j++)
		{
			if(Data[j] == ' ')
				out << " ";
			if(Data[j] == 'a')
				out<<"y";
			if(Data[j] == 'b')
				out<<"h";
			if(Data[j] == 'c')
				out<<"e";
			if(Data[j] == 'd')
				out<<"s";
			if(Data[j] == 'e')
				out<<"o";
			if(Data[j] == 'f')
				out<<"c";
			if(Data[j] == 'g')
				out<<"v";
			if(Data[j] == 'h')//
				out<<"x";
			if(Data[j] == 'i')
				out<<"d";
			if(Data[j] == 'j')
				out<<"u";
			if(Data[j] == 'k')
				out<<"i";
			if(Data[j] == 'l')
				out<<"g";
			if(Data[j] == 'm')
				out<<"l";
			if(Data[j] == 'n')
				out<<"b";
			if(Data[j] == 'o')
				out<<"k";
			if(Data[j] == 'p')
				out<<"r";
			if(Data[j] == 'q')//xz
				out<<"z";//
			if(Data[j] == 'r')
				out<<"t";
			if(Data[j] == 's')
				out<<"n";
			if(Data[j] == 't')
				out<<"w";
			if(Data[j] == 'u')
				out<<"j";
			if(Data[j] == 'v')
				out<<"p";
			if(Data[j] == 'w')
				out<<"f";
			if(Data[j] == 'x')
				out<<"m";
			if(Data[j] == 'y')
				out<<"a";
			if(Data[j] == 'z')
				out<<"q";
		}
		for(j=0;j<a;j++)
			Data[j]=0;
	}
	return 0;
}