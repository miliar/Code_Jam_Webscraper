
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <iomanip>
#include <cmath>

 using namespace std;

int main()
{	 
	int T=0;
	ifstream archivoIn;	
	archivoIn.open("Input", ios::in);
	
	
	
	archivoIn >> T;
	if(T<1 || T>30)
	{
		cout << "ERROR" << endl;
	}

	char** entrada = new char*[T];
	for(int a=0; a<T; a++)
		entrada[a] = new char[101];

	char ab[101];
	archivoIn.getline(ab,101);
	
	for(int a=0; a<T; a++)
		archivoIn.getline(entrada[a],101);
		
	for(int a=0; a<T; a++)
		cout << entrada[a] << endl;		
		
	char** salida = new char*[T];
	for(int a=0; a<T; a++)
		salida[a] = new char[101];		

	for(int a=0; a<T; a++)
		for(int b=0; b<101; b++){
			
			
			if(entrada[a][b]=='e')
				salida[a][b]='o';
			else if(entrada[a][b]=='j')
				salida[a][b]='u';
			else if(entrada[a][b]=='p')
				salida[a][b]='r';
			else if(entrada[a][b]=='m')
				salida[a][b]='l';
			else if(entrada[a][b]=='s')
				salida[a][b]='n';
			else if(entrada[a][b]=='c')
				salida[a][b]='e';
			else if(entrada[a][b]=='k')
				salida[a][b]='i';
			else if(entrada[a][b]=='d')
				salida[a][b]='s';
			else if(entrada[a][b]=='x')
				salida[a][b]='m';
			else if(entrada[a][b]=='n')
				salida[a][b]='b';
			else if(entrada[a][b]=='h')
				salida[a][b]='x';
			else if(entrada[a][b]=='f')
				salida[a][b]='c';	
			else if(entrada[a][b]=='w')
				salida[a][b]='f';	
			else if(entrada[a][b]=='g')
				salida[a][b]='v';
			else if(entrada[a][b]=='v')
				salida[a][b]='p';	
			else if(entrada[a][b]=='l')
				salida[a][b]='g';
			else if(entrada[a][b]=='i')
				salida[a][b]='d';
			else if(entrada[a][b]=='r')
				salida[a][b]='t';		
			else if(entrada[a][b]=='b')
				salida[a][b]='h';	
			else if(entrada[a][b]=='t')
				salida[a][b]='w';
			else if(entrada[a][b]=='a')
				salida[a][b]='y';
			else if(entrada[a][b]=='o')
				salida[a][b]='k';	
			else if(entrada[a][b]=='y')
				salida[a][b]='a';
			else if(entrada[a][b]=='u')
				salida[a][b]='j';
			else if(entrada[a][b]=='z')
				salida[a][b]='q';
			else if(entrada[a][b]=='q')
				salida[a][b]='z';																																																																																										
			else
				salida[a][b]=' ';			
									
		}	
		
	ofstream archivoOut;
	archivoOut.open("Output", ios::out );
	
	for(int a=0; a<T; a++)
		archivoOut << "Case #" << a+1 << ": " << salida[a] <<endl;
	
	archivoOut.close();				
		
	return 0;
 	
}
