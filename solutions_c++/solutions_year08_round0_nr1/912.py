#include <iostream>
#include <fstream>

using namespace std;

long min_switches(int eng, int qsize, int * q) {
	int switches = 0;
	char * f = new char[eng];

	int fl = 0;
	for (int i=0; i<eng; i++)
		f[i] = 0;

	for (int i=0; i<qsize; i++)
		if (f[q[i]] == 0) {
			f[q[i]] = 1;
			fl++;
			if (fl == eng) {
				switches++;
				fl = 1;
				for (int i=0; i<eng; i++)
					f[i] = 0;
				f[q[i]] = 1;
			}
		}

	delete [] f;
	return switches;
}

int main (int argc, char * argv[]) {
	char fn[100];

	if (argc < 2)
		return 1;

	sprintf(fn,"%s.in",argv[1]);
	ifstream fin(fn);
	sprintf(fn,"%s.out",argv[1]);
	ofstream fout(fn);


	int cases;
	int engines;
	char * eng[101];
	int qsize;
	int * query = new int [1001];

	for (int i=0; i<101; i++)
		eng[i] = 0;

	fin >> cases;

	for (int i=1; i<=cases; i++) {
		fin >> engines;

		char tmp[5];
		fin.getline(tmp,4);

		for (int j=0; j<engines; j++) {
			if (!eng[j])
				eng[j] = new char[110];
			fin.getline(eng[j],109);
		}
		fin >> qsize;
		fin.getline(tmp,4);

		for (int j=0; j<qsize; j++) {
			char q[110];
			fin.getline(q,109);
			for (int k=0; k<engines; k++)
				if (strcmp(eng[k],q)==0) {
					query[j] = k;
					break;
				}
		}

		fout << "Case #" << i <<": " << min_switches(engines, qsize, query) << endl;
	}

	for (int i=0; i<101; i++)
		if (eng[i])
			delete [] eng[i];

	delete [] query;

	fin.close();
	fout.close();
	
	return 0;
}
