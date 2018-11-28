#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <windows.h>

using namespace std;
#pragma warning(disable: 4996)

#define OUTPUTLOG2(X,Y)\
{\
	char msg[1024];\
	sprintf( msg, X, Y );\
	OutputDebugString(msg);\
}
#define OUTPUTLOG OutputDebugString

#define FOR(r,a,b) for(r=(a); r<(b); r++)
#define REP(r,b) for(r=0; r<(b); r++)
#define TRV(type,cnt,it) for(type::iterator it=(cnt).begin(); it!=(cnt).end(); it++)

class Dir
{
public:
	Dir(const char* dir_name) : name(dir_name){}
	string name;
	vector<Dir*> sub;

	Dir* find(const char* dir_name){
		int i;
		REP(i,sub.size()){
			if( sub[i]->name.compare(dir_name) == 0 )
				return sub[i];
		}
		return NULL;
	}
	Dir* add(const char* dir_name){
		Dir* d = new Dir(dir_name);
		sub.push_back(d);
		return sub[sub.size()-1];
	}
};

void main(int argc, char*argv[]) // usage: main.exe in.txt out.txt
{
	int i,j,k,l,m,n;

	ifstream fin(argv[1]);
	if( fin == NULL ){
		OUTPUTLOG2("cannot open in-file : %s\n", argv[1]);
		return;
	}
	FILE* fout = fopen(argv[2],"w");
	if( fin == NULL ){
		OUTPUTLOG2("cannot open out-file : %s\n", argv[2]);
		return;
	}

/////////////////////////////
	char line[1024];
	int CASE;
	fin >> CASE;
	for( int test_case = 1; test_case <= CASE; test_case++ ){
	/////////////////////////////
		int N,M;
		fin >> N;
		fin >> M;

		// make
		Dir* root = new Dir("/");
		Dir* cur = root, *next;

		REP(i,N){
			string tmp;
			fin >> tmp;
			vector<char> path(tmp.begin(), tmp.end());
			path.push_back('\0');
			int cpos = 1;
			cur = root;
			for( int j = 1; j < path.size(); j++ ){
				if( path[j] == '/' ){
					path[j] = '\0';
					if( (next = cur->find(&path[cpos])) == NULL ){
						cur = cur->add(&path[cpos]);
					}else{
						cur = next;
					}
					cpos = j+1;
				}
			}
			if( (next = cur->find(&path[cpos])) == NULL ){
				cur = cur->add(&path[cpos]);
			}else{
				cur = next;
			}
		}

		// search
		int result = 0;
		REP(i,M){
			string tmp;
			fin >> tmp;
			vector<char> path(tmp.begin(), tmp.end());
			path.push_back('\0');
			int cpos = 1;
			cur = root;
			for( int j = 1; j < path.size(); j++ ){
				if( path[j] == '/' ){
					path[j] = '\0';
					if( (next = cur->find(&path[cpos])) == NULL ){
						cur = cur->add(&path[cpos]);
						result++;
					}else{
						cur = next;
					}
					cpos = j+1;
				}
			}
			if( (next = cur->find(&path[cpos])) == NULL ){
				cur = cur->add(&path[cpos]);
				result++;
			}else{
				cur = next;
			}
		}
	/////////////////////////////
		fprintf(fout,"Case #%d: %d\n", test_case, result);
		if( fin.eof() ){
			if( test_case != CASE ){
				OUTPUTLOG( "in-file error:eof" );
			}
			break;
		}
	}

	OUTPUTLOG( "program end" );
}