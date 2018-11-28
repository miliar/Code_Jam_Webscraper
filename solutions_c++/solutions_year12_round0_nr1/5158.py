#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <cstdlib>
using namespace std;
typedef map<char, char> cmap_t;


int main(int argc, char* argv[])
{
	if(argc != 2) {
		cout << "usage: ./mapping file" <<endl;
		exit(0);
	}
	
	fstream fmap("map");
	fstream fin(argv[1]);
	
	if(fmap.is_open() == false || fin.is_open() == false) {
		perror("open");
		exit(0);
	}
	
	cmap_t cmap;
	string s1, s2;
	int i, len;
	
	fmap >> s1;
	fmap >> s2;
	
	len = s1.length();
	for(i = 0; i < len; i++) {
		cmap[s1[i]] = s2[i];
	}
	
	int n;
	char str[256];
	char *head;
	
	fin >> n;
	fin.getline(str, 256);
	
	for(i = 0; i < n; i++) {
		cout << "Case #" << i + 1 << ": ";
		fin.getline(str, 256);
		head = str;
		for(; *head != '\0'; head++)
		{
			if(*head == ' ') continue;
			*head = cmap[*head];
		}
		cout << str <<endl;
	}
}
