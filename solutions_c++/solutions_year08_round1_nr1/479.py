#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool sort_1(int E1, int E2){
	return E1 < E2;
}

bool sort_2(int E1, int E2){
	return E1 > E2;
}

int main(){
	FILE* in = fopen("A.in","r");
	FILE* out = fopen("A.out","w");
	int TestCase = 0;
	fscanf(in, "%d\n", &TestCase);
	for(int i = 0; i < TestCase; i++)
	{	
		int len = 0;
		vector <int> T1, T2;
		fscanf(in, "%d\n", &len);
		for(int j = 0; j < len; j++){
			int temp = 0;
			fscanf(in, "%d ", &temp);
			T1.push_back(temp);
		}
		for(int j = 0; j < len; j++){
			int temp = 0;
			fscanf(in, "%d ", &temp);
			T2.push_back(temp);
		}
		sort(T1.begin(), T1.end(), sort_1);
		sort(T2.begin(), T2.end(), sort_2);
		int Answer = 0;
		for(int j = 0; j < len; j++){
			int temp = 0;
			Answer += T1[j]*T2[j];
		}
		T1.clear();
		T2.clear();
		fprintf(out, "Case #%d: %d\n", i+1, Answer);
	}
	return 0;
}
