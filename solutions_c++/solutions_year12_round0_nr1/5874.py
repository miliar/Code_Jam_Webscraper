
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

char letters[26] = { /*a*/'y', /*b*/'h', /*c*/'e', /*d*/'s', /*e*/'o', /*f*/'c', /*g*/'v',
	                 /*h*/'x', /*i*/'d', /*j*/'u', /*k*/'i', /*l*/'g', /*m*/'l', /*n*/'b',
					 /*o*/'k', /*p*/'r', /*q*/'z', /*r*/'t', /*s*/'n', /*t*/'w', /*u*/'j',
					 /*v*/'p', /*w*/'f', /*x*/'m', /*y*/'a', /*z*/'q'};

string translateGooglerese(string const & s)
{
	string result(s.length(), ' ');
	for (unsigned int i = 0; i < s.length(); ++i)
	{
		if (s[i] != ' ')
			result[i] = letters[static_cast<int>(s[i] - 'a')];
	}
	return result;
}

int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "Usage: " << argv[0] << " <in-file> <out-file>" << endl;
		return 0;
	}

	ifstream ifs(argv[1]);
	ofstream ofs(argv[2]);

	string line;
	unsigned int nbTests = 0;
	// read nb tests
	ifs >> nbTests;
	getline(ifs, line);

	//solve each test cases
	for (unsigned int i = 0; i < nbTests; ++i)
	{
		string s;
		getline(ifs, s);
		string result = translateGooglerese(s);
		ofs << "Case #" << (i+1) << ": " << result << endl;
	}
	ifs.close();
	ofs.close();

	return 0;
}

