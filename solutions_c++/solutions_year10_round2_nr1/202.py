#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <hash_set>
#include <ppl.h>
using namespace std;
using namespace Concurrency;
using namespace stdext;

int a[1000]={0};


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream is("input.txt");
	ofstream os("output.txt");
	int T;
	is >> T;
	for (int i=1; i<=T; ++i)
	{
		int N, M;
		__int64 ans=0;
		is >> N >> M;
		hash_set<string> dirs;
		//string s;
		//getline(is, s);
		dirs.insert("");
		for (int d = 0; d<N; ++d){
			string s;
			is >> s;
			//std::getline(is, s);
			s+='/';
			int j = s.length();
			int k = 0;
			while (k >= 0){
				dirs.insert(s.substr(0,k));
				k = s.find('/', k+1);
			}
		}
		for (int d = 0; d<M; ++d){
			string s;
			is >> s;
			s+='/';
			int j = s.length();
			int k = 0;
			while (k >= 0){
				if (dirs.find(s.substr(0,k)) == dirs.end()){
					dirs.insert(s.substr(0,k));
					++ans;
				}
				k = s.find('/', k+1);
			}
		}

		os << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}

