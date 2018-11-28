#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
using namespace std;

const int MAX = 1100;
const int INFTY = (1<<30);

int nTestCases;
fstream	fin;
fstream fout;

int N;
int A[MAX];
int B[MAX];

inline bool intersect(int i, int j){
	if(A[i] > A[j]){
		if(B[i] > B[j])
			return false;
		else
			return true;
	}
	else{
		if(B[i] > B[j])
			return true;
		else
			return false;
	}
}


inline void init(){
	fin >> N;
	for(int i=0; i<N; i++)
		fin >> A[i] >> B[i];
}


void main()
{
	fin.open("z:\\input.txt", ifstream::in);
	fout.open("z:\\output.txt", ifstream::out);


	fin >> nTestCases;
	for(int testCase = 1; testCase <= nTestCases; testCase++){
		init();
		
		long long ans = 0;
		for(int i=0; i<N; i++){
			for(int j=i+1; j<N; j++){
				if(intersect(i,j))
					ans++;
			}
		}
		
		fout << "Case #" << testCase <<": " << ans << endl;
	}

	fin.close();
	fout.close();
}