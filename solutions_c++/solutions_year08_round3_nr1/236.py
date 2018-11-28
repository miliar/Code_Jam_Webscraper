#include <iostream>
#include <fstream>
#include <map>
#include <iomanip>
using namespace std;

ifstream fin;
ofstream fout;

int N, P, K, L;
int *fa;
char line[1024];

struct ltstr
{
  bool operator()(string s1, string s2) const
  {
    return strcmp(s1.c_str(), s2.c_str()) < 0;
  }
};

map<string, int, ltstr> servers;


int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}

int main()
{
	int i, j, k, h;
	double re;
	fin.open("A-large.in");
	fout.open("A-large.out");

	fin >> N;
	fin.getline(line, 1024);
	
	for(i = 0; i < N; i ++)
	{
		fin >> P;
		fin >> K;
		fin >> L;
		fin.getline(line, 1024);

		cout << P << ' ' << K << ' ' << L << endl;
		
		fa = new int[L];

		for(j = 0; j < L; j ++) 
		{
			fin >> fa[j];
	//		cout << fa[j] << ' ' ;
		}
		cout << endl;
		fin.getline(line, 1024);

		qsort(fa, L, sizeof(int), compare);

	/*	for(j = 0; j < L; j ++)
		{
			cout << fa[j] << ' ' ;
		}
		cout << endl;
*/
		re = 0;


		for(j = 0; j < L; j ++)
		{
			re += fa[j] * (j / K + 1);
		}
		
		cout <<  "case #" << i + 1 << ": " << fixed << setprecision(0) <<re << endl;
		fout <<  "Case #" << i + 1 << ": " << fixed << setprecision(0) <<re << endl;
		//fout << "Case #" << i + 1 << ": " << re << endl;
		delete[] fa;
			
	}

	return 0;
}