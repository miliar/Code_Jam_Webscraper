#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream ifile("A-small-attempt0.in");
	ofstream ofile("out.txt");
	string str = "yhesocvxduiglbkrztnwjpfmaq";
	string inStr;

	int loop_cnt = 0;

	ifile >> loop_cnt;
	getline(ifile, inStr);
	for(int i=0;i<loop_cnt;++i)
	{
		getline(ifile, inStr);
		string res = "";
		for(int i=0;i<inStr.size();++i)
		{
			if(inStr[i] != ' ')
			{
				char c = inStr[i];
				res += str[c-'a'];
			}
			else
			{
				res += ' ';
			}
		}
		ofile << "Case #" << i+1 << ": " << res << endl;
	}

	ifile.close();
	return 0;
}