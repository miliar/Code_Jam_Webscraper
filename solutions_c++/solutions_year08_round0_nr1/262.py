// 
//	Alexandr Chupilko, 2008
//	
//	Explode of University
//

#include <iostream>	
#include <string>
#include <fstream>
#include <map>

using namespace std;

typedef map<string, bool> tNameSet;

void readNameSet(istream& in, tNameSet& ns)
{
	size_t s;
	string tmp;
	in >> s;
	getline(in, tmp);
	
	for(size_t j = 1; j <= s; j++)
	{
		getline(in, tmp); 
		ns[tmp] = true;
	}
}

void floodNameSet(tNameSet& ns)
{
	for(tNameSet::iterator p = ns.begin(); p != ns.end(); ++p)
	{
		(*p).second = true;
	}
}

int answerQuestion(istream& in, ostream& out)
{
	int q, set_v = 0, result = 0;
	string tmp;
	tNameSet ns;
	readNameSet(in, ns);
	in >> q;
	getline(in, tmp);
	for(int j = 1; j <= q; j++)
	{
		getline(in, tmp); 
		if(ns[tmp])
		{
			if(set_v == ns.size() - 1)
			{
				result++;
				set_v = 0;
				floodNameSet(ns);
			}
			ns[tmp] = false;
			set_v++;
		}
	}
	return result;
}

void answerQuestions(istream& in, ostream& out)
{
	size_t n;
	in >> n;
	for(size_t i = 1; i <= n; i++)
	{
		out << "Case #" << i << ": " << answerQuestion(in, out) << endl;
	}
}

int main(int argc, char* argv[])
{
	if(argc>3) {
		cerr << "Usage: <Input file> <Output file>" << endl;
		return EXIT_FAILURE;
	}
	char f_in[256], f_out[256];

	if (argc<3){strcpy_s(f_out,"A-large.out");}else{strcpy_s(f_out,argv[2]);};
	if (argc<2){strcpy_s(f_in,"A-large.in");}else{strcpy_s(f_in,argv[1]);};

	ifstream in(f_in);
	ofstream out(f_out);

	if (!in){
		cerr << "Bad Input file: " << f_in << endl;
		return EXIT_FAILURE;
	}
	if (!out){
		cerr << "Bad Output file: " << f_out << endl;
		return EXIT_FAILURE;
	}

	answerQuestions(in, out);

	return EXIT_SUCCESS;
}

