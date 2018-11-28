
#include <boost/lexical_cast.hpp>
#include <cassert>
#include <fstream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>

#include <iostream>
using std::cout;
using std::endl;

namespace parse {
	bool nextline(std::istream &data, std::string &str) {
		for (;;) {
			if (data.eof())
				return false;
			if (data.bad())
				throw std::runtime_error("nextline failed");
			std::getline(data, str);
			if (str.size())
				return true;
		}
	}
}

typedef std::map<char,char> trans_t;

std::string translate(const std::map<char,char> &m, const std::string &line) {
	std::string res(line.begin(), line.end());
	for (size_t i = 0; i < res.size(); i++) {
		trans_t::const_iterator match = m.find(res[i]);
		if (match != m.end())
			res[i] = match->second;
	}
	return res;
}

void init(trans_t &trans, const std::string &normal, const std::string &weird) {
	for (size_t i = 0; i < normal.size(); i++)
		trans[weird[i]] = normal[i];
}

int main(int argc, char ** argv) {

	std::vector<std::string> args(argv, argv+argc);
	std::ifstream data(args.at(1));

	trans_t trans;
	init(trans
		,"our language is impossible to understand"
		,"ejp mysljylc kd kxveddknmc re jsicpdrysi");
	init(trans
		,"there are twenty six factorial possibilities"
		,"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	init(trans
		,"so it is okay if you want to just give up"
		,"de kr kd eoya kw aej tysr re ujdr lkgc jv");
	trans['q'] = 'z';
	trans['z'] = 'q';

	std::string line;
	assert(parse::nextline(data, line));
	size_t sz = boost::lexical_cast<size_t>(line);

	for (size_t i = 0; i < sz; i++) {
		assert(parse::nextline(data, line));
// 		cout << "Case #" << (i+1) << ": " << line << endl;
		cout << "Case #" << (i+1) << ": " << translate(trans, line) << endl;
	}

	return 0;
}
