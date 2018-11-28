#include <iostream>
#include <hash_set>
#include <ctype.h>

char existing[1000][200000];
char created[1000][200000];

using namespace __gnu_cxx;

char *begin_p;
char *new_p;
bool last;

std::string GetUntilSlash(char *p) {
	char *p2 = p;
	while (*p2 != '/' && *p2 != '\0') ++p2;
	return std::string(begin_p, p2 - begin_p);
}

std::string ExtractDir() {
	std::string str = GetUntilSlash(new_p);
	if (begin_p[str.size()] == '\0')
		last = true;
	else {
		last = false;
		new_p = begin_p + str.size() + 1;
		if (*new_p == '\0')
			last = true;
	}
	return str;
}

int main() {
	int nCases;
	std::cin >> nCases;
	int i;
	for (i = 0; i < nCases; ++i) {
		int nExisting, nCreated;
		std::cin >> nExisting;
		std::cin >> nCreated;
//		std::cout << "Got counts" << std::endl;
		int nTrulyCreated = 0;
//		std::cout << "GOT HERE (1)" << std::endl;		
		for (int j = 0; j < nExisting; ++j) {
			int k;
			do {
//				std::cout << "Reading line..." << std::endl;
				std::cin.getline(existing[j], 150000);
//				std::cout << "Got existing line: " << existing[j] << std::endl;
				for (k = 0; ; ++k)
					if (!isspace(existing[j][k]))
						break;
			} while (existing[j][k] == '\0');
		}
		for (int j = 0; j < nCreated; ++j) {
			int k;
			do {
//				std::cout << "Reading line..." << std::endl;
				std::cin.getline(created[j], 150000);
//				std::cout << "Got created line: " << created[j] << std::endl;
				for (k = 0; ; ++k)
					if (!isspace(created[j][k]))
						break;
			} while (created[j][k] == '\0');

		}
		hash_set<std::string> setExisting;
		hash_set<std::string> setCreated;
		for (int j = 0; j < nExisting; ++j) {
			begin_p = new_p = existing[j]; last = false; ExtractDir();
			while (!last) {
				std::string str(ExtractDir());
//				std::cout << "hasdir " << str << std::endl;
				setExisting.insert(str);
			}
		}
		
		for (int j = 0; j < nCreated; ++j) {
			begin_p = new_p = created[j]; last = false; ExtractDir();
			while (!last) {
				std::string str(ExtractDir());
//				std::cout << "mkdir " << str << std::endl;
				if (setExisting.insert(str).second)
					++nTrulyCreated;
			}
		}
		std::cout << "Case #" << (i + 1) << ": " << nTrulyCreated << std::endl;
		
	}
}
