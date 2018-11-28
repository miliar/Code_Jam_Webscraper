#include <fstream>
using namespace std;

int main()
{
	char code[] = "yhesocvxduiglbkrztnwjpfmaq";
	int T; char c;
	int lg,j;
	char line[150];
	ifstream fin("problem.in"); ofstream fout("problem.out");
	fin>>T;
	fin.get();
	for(int i = 1; i <= T; i++)
	{
		fin.get(line,107,'\n');
		fin.get();
		fout<<"Case #"<<i<<": ";
		lg = strlen(line);
		for(j = 0; j < lg; j++)
			if(line[j] == ' ')
				fout<<' ';
			else
				fout<<code[line[j] - 'a'];
		fout<<'\n';
	}
}