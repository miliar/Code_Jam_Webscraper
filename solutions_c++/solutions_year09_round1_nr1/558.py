// vim:ts=4:sw=4:cindent:
#define __STDC_FORMAT_MACROS
#include "base.hh"

string to_base(int num, int base)
{
	const char c[] = "0123456789";
	string ret;

	while (num >= base) {
		int digit = num % base;
		ret.append(c + digit, 1);
		num /= base;
	}

	ret.append(c + num, 1);

	return string(ret.rbegin(), ret.rend());
}

map<string, bool> happy_cache;
set<string> happy_loop_break;

bool is_happy(int num, int base)
{
	string str = to_base(num, base);

	if (happy_cache.find(str) != happy_cache.end()) {
		// we have an answer for this string.
		return happy_cache[str];
	}

	if (happy_loop_break.find(str) == happy_loop_break.end()) {
		happy_loop_break.insert(str);
	} else {
		// oops, this is a loop.
		happy_cache[str] = false;
		return false;
	}

	int sum = 0;
	for (size_t i = 0; i < str.size(); i++) {
		int digit = ((str.c_str())[i]) - '0';
		sum += digit * digit;
	}

	if (sum == 1) {
		happy_cache[str] = true;
		return true;
	}

	bool ret = is_happy(sum, base);
	happy_cache[str] = ret;
	return ret;
}

void do_problem()
{
	int T;
	read_int(T);
	finish_line();

	for (int i = 0; i < T; i++) {
		string text;
		read_line(text);

		vector<int> bases;
		istringstream iss(text);
		while (!iss.eof()) {
			string piece;
			iss >> piece;
			bases.push_back(boost::lexical_cast<int>(piece));
		}

		int j;

		for (int j = 2; j < 0x7fffffff; j++) {
			size_t happy_in = 0;
			BOOST_FOREACH(int base, bases) {
				happy_loop_break.clear();
				happy_cache.clear();
				if (is_happy(j, base)) {
					happy_in++;
				} else {
					break;
				}
			}

			if (happy_in == bases.size()) {
				output_case("%d\n", j);
				break;
			}
		}

		if (j == 0x7fffffff) {
			throw runtime_error("Can't find a small enough number.");
		}
	}
}

