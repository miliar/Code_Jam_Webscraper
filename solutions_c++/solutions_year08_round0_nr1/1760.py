#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <stdexcept>

std::string change_ext(const std::string &name, const std::string &ext) 
{
	std::string::size_type pos = name.find_last_of('.');
	if (pos != std::string::npos) {
		std::string ret = name;
		ret.replace(pos, name.length() - pos, ext);
		return ret;
	} else throw std::runtime_error("change_ext: no extencion found.");
}

int main(int argc, char **argv)
{
	if (argc < 2) {
		std::cout << "usage: " << argv[0] << " file." << std::endl;
		return 1;
	}

	std::ifstream in(argv[1]);
	if (!in.good()) {
		std::cout << "error: unable to open file " << argv[1] << "." << std::endl;
		return 2;
	}

	std::ofstream out(change_ext(argv[1], ".out").c_str());
	if (!out.good()) {
		std::cout << "error: unable to open file for output." << std::endl;
		return 3;
	}

	unsigned int cases;
	in >> cases;
	for (unsigned int i = 0; i < cases; ++i) {
		typedef std::map<std::string, unsigned int> engine_map;
		engine_map engines;
		unsigned int count, switches = -1;
		std::string name;

		in >> count;
		in.ignore();
		for (unsigned int j = 0; j < count; ++j) {
			getline(in, name);
			engines[name] = 0;
		}

		typedef std::vector<std::string> query_vector;
		query_vector queries;

		in >> count;
		in.ignore();
		for (unsigned int j = 0; j < count; ++j) {
			getline(in, name);
			queries.push_back(name);
			++engines[name];
		}

		for (engine_map::iterator it = engines.begin(); it != engines.end(); ++it) {
			if (!it->second) {
				switches = 0;
				break;
			}
		}

		if (switches) {
			count = engines.size();
			switches = 0;
			unsigned int key = -1;
			for (query_vector::iterator it = queries.begin(); it != queries.end(); ++it) {
				if (engines[*it] != key) {
					engines[*it] = key;
					--count;
				}
				if (!count) {
					count = engines.size() - 1;
					switches++;
					engines[*it] = --key;
				}
			}
		}

		out << "Case #" << (i + 1) << ": " << switches << std::endl;
	}
}
