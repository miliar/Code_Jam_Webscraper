#include <iostream>
#include <map>
#include <set>

using namespace std;

int createDirectories(set<string> &existing_directories, string const &dir)
{
	if(existing_directories.find(dir) != existing_directories.end())
		return 0;
	existing_directories.insert(dir);
	return 1 + createDirectories(existing_directories, dir.substr(0, dir.find_last_of("/")));
}

int main(int argc, char *argv[])
{
	int cases;
	cin >> cases;
	for(int ci = 0; ci < cases; ++ci)
	{
		int existing, non_existing;
		cin >> existing >> non_existing;
		set<string> existing_directories;
		existing_directories.insert(string(""));

		string input;
		for(int ei = 0; ei < existing; ++ei)
		{
			cin >> input;
			createDirectories(existing_directories, input);
		}

		int creations = 0;

		for(int ni = 0; ni < non_existing; ++ni)
		{
			cin >> input;
			creations += createDirectories(existing_directories, input);
		}

		cout << "Case #" << (ci + 1) << ": " << creations << endl;
	}

	return 0;
}
