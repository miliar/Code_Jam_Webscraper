#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <list>
#include <cmath>
#include <string>

using namespace std;

class Dir {
public:
	map<string, Dir> subdirs;

	int create(char* path)
	{
		int count = 0;

		Dir* cur = this;

		char *dir = strtok(path, "/");
		while (dir != NULL) {
			map<string, Dir>::iterator result = cur->subdirs.find(dir);
			if (result != cur->subdirs.end()) {
				cur = &result->second;
			} else {
				cur->subdirs[dir] = Dir();
				cur = &cur->subdirs[dir];
				count++;
			}
			dir = strtok(NULL, "/");
		}

		return count;
	}
};

void processCase(istream& in, ostream& out)
{
	int n, m;
	in >> n >> m;

	Dir root;
	char buffer[1024];
	in.getline(buffer, 1024);

	// Read existing
	for (int i=0; i<n; i++) {
		in.getline(buffer, 1024);
		root.create(buffer);
	}

	// Read to-create
	int count = 0;
	for (int i=0; i<m; i++) {
		in.getline(buffer, 1024);
		count += root.create(buffer);
	}

	// Print result
	int result = count;
	out << result;
}

int main()
{
	ifstream in("A-large.in");
	//ostream& out = cout;
	ofstream out("A-large.out", std::ios_base::out | std::ios_base::binary);

	int nCases;
	in >> nCases;
	char tmp[2];
	in.getline(tmp, 2);
	for (int i=0; i<nCases; i++) {
		out << "Case #" << (i+1) << ": ";
		processCase(in, out);
		out << endl;
	}

	out.flush();
}
