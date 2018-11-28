//============================================================================
// Name        : GCJ200801.cpp
// Author      : liudapeng
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

char* s[100];
char* q[1000];

char buf[2048];

int main() {
	ifstream in("C:/Documents and Settings/刘大澎/桌面/larger.in");
	ofstream out("C:/Documents and Settings/刘大澎/桌面/larger.out");
	int n = 0;
	int n_searcher = 0;
	int n_query = 0;
	in >> n;
	for (int z = 0; z < n; ++z) {
		in >> n_searcher;
		in.getline(buf, 2048);
		for (int i = 0; i < n_searcher; ++i) {
			in.getline(buf, 2048);
			s[i] = new char[strlen(buf) + 1];
			strcpy(s[i], buf);
//			cout << buf << endl;
		}
		in >> n_query;
		in.getline(buf, 2048);
		for (int i = 0; i < n_query; ++i) {
			in.getline(buf, 2048);
			q[i] = new char[strlen(buf) + 1];
			strcpy(q[i], buf);
//			cout << buf << endl;
		}
		int j = 0;
		int count = 0;
		bool flag = false;
		while(j < n_query) {
			flag = true;
			int max = 0;
			for(int m = 0; m < n_searcher; m++) {
				int p = j;
				for(; p < n_query; p++)
					if(0 == strcmp(s[m], q[p]))
						break;
				if(max < p)
					max = p;
			}
			j = max;
			count++;
		}
		if(flag)
			count--;
		cout << "Case #" << z + 1 << ": " << count << endl;
		out << "Case #" << z + 1 << ": " << count << endl;
		
		for (int i = 0; i < n_searcher; ++i) 
			delete s[i];
		for (int i = 0; i < n_query; ++i)
			delete q[i];
	}
	
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
