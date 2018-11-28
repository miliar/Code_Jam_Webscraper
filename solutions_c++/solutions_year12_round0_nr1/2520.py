#include <iostream>
#include <fstream>

using namespace std;

char map[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(int argc, char **argv) {
	
	ifstream in(argv[1]);

	int cases;
	in >> cases;

	char line[256];

	// Burn off the rest of the line
	in.getline(line,256);

	ofstream out(argv[2]);

	for(int i = 0; i < cases; ++i) {
		in.getline(line,256);

		for(int j = 0; line[j] != '\0'; ++j)
			if(line[j] != ' ')
				line[j] = map[(unsigned int)(line[j] - 'a')];
		
		out << "Case #" << i+1 << ": " << line << endl;
	}

	in.close();
	out.close();

	return 0;
}
