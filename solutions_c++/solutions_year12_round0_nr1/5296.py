#include <fstream.h>
#include <string.h>

int main()
{
	ifstream fin("1.in");
	ofstream fout("1.out");
	
	char str[101], sout[101];
	//abcdefghijklmnopqrstuvwxyz
	//yhesocvxduiglbkrztnwjpfmaq
	
	char alphabet[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	                
 	int N, i, j, a;
	
	fin >> N;
	fin.getline(str, sizeof(str));
	
	for (i = 0; i<N; i++)
	{
		fin.getline(str, sizeof(str));
		j = 0;
		while ((j < 101) && ((int)str[j] > 0))
		{
			a = (int)str[j];
			if (a != 32) sout[j] = alphabet[a - 97]; else sout[j] = ' ';
			j++;
		}
		sout[j] = '\0';
		
		fout << "Case #" << i+1 << ": " << sout << endl;
	}
	
	fin.close();
	fout.close();
}