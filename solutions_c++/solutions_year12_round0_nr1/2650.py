/**
 * file: speaking_in_tongues.cpp
 * Author: Maoliang <kceiwH@gmail.com>
 * Created Time: Fri 13 Apr 2012 10:29:43 PM EDT
 * Description: 
 */

#include <iostream>
#include <map>

using namespace std;

string translate_to_plain(const string &_googlerese);
void build_dictionary();

map< char, char > googlerese_to_plain_dict;

int main(int argc, char *argv[])
{
	build_dictionary();

	int num_of_case;
	cin >> num_of_case;
	cin.ignore(3, '\n');

	string googlerese_text;
	for (int i = 0; i < num_of_case; ++i) {
		getline(cin, googlerese_text);
		cout << "Case #" << i + 1 << ": "
			<< translate_to_plain(googlerese_text) << endl;
	}
}

string translate_to_plain(const string &_googlerese)
{
	string plain;
	for (string::const_iterator it = _googlerese.begin(),
		it_end = _googlerese.end(); it != it_end; ++it) {
		map< char, char >::const_iterator map_it
			= googlerese_to_plain_dict.find(*it);
		if (map_it == googlerese_to_plain_dict.end()) {
			plain.append(1, *it);
		} else {
			plain.append(1, map_it->second);
		}
	}

	return plain;
}

void build_dictionary()
{
	googlerese_to_plain_dict['a'] = 'y';
	googlerese_to_plain_dict['b'] = 'h';
	googlerese_to_plain_dict['c'] = 'e';
	googlerese_to_plain_dict['d'] = 's';
	googlerese_to_plain_dict['e'] = 'o';
	googlerese_to_plain_dict['f'] = 'c';
	googlerese_to_plain_dict['g'] = 'v';
	googlerese_to_plain_dict['h'] = 'x';
	googlerese_to_plain_dict['i'] = 'd';
	googlerese_to_plain_dict['j'] = 'u';
	googlerese_to_plain_dict['k'] = 'i';
	googlerese_to_plain_dict['l'] = 'g';
	googlerese_to_plain_dict['m'] = 'l';
	googlerese_to_plain_dict['n'] = 'b';
	googlerese_to_plain_dict['o'] = 'k';
	googlerese_to_plain_dict['p'] = 'r';
	googlerese_to_plain_dict['q'] = 'z';
	googlerese_to_plain_dict['r'] = 't';
	googlerese_to_plain_dict['s'] = 'n';
	googlerese_to_plain_dict['t'] = 'w';
	googlerese_to_plain_dict['u'] = 'j';
	googlerese_to_plain_dict['v'] = 'p';
	googlerese_to_plain_dict['w'] = 'f';
	googlerese_to_plain_dict['x'] = 'm';
	googlerese_to_plain_dict['y'] = 'a';
	googlerese_to_plain_dict['z'] = 'q';
}

