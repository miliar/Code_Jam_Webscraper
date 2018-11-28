#include <fstream>
#include <map>
#include <string>


void load_map(std::map<char, char>& g, const std::string& is)
{
	for (size_t idx = 0; idx < is.length(); idx += 3)
	{
		g.insert(std::make_pair(is[idx+1], is[idx]));
	}
}

std::string apply_map(const std::string& istr, const std::map<char, char>& mm)
{
	std::string translated(istr);
	for (size_t idx = 0; idx < istr.length(); ++ idx)
	{
		std::map<char, char>::const_iterator it = mm.find(istr[idx]);
		if (it == mm.end())
		{
			translated[idx] = istr[idx];
		}
		else
		{
			translated[idx] = it->second;
		}
	}
	return translated;
}

int main(int argc, char** argv)
{
	std::string mapping("ay bn cf di ec fw gl hb ik ju ko lm mx ns oe pv qz rp sd tr uj vg wt xh ya zq");
	std::map<char, char> googlerese;
	load_map(googlerese, mapping);
	
	size_t num_lines;
	std::ifstream infile(argv[1], std::ifstream::in);
	std::ofstream ofile(argv[2], std::ofstream::out);
	infile >> num_lines;

	std::string istr("");
	getline(infile, istr);

	for (size_t idx = 0; idx < num_lines; ++ idx)
	{
		getline(infile, istr);
		std::string ostr(apply_map(istr, googlerese));
		ofile << "Case #";
		ofile << idx+1;
		ofile << ": ";
		ofile << ostr;
		ofile << std::endl;
	}
	infile.close();
	ofile.close();
}
