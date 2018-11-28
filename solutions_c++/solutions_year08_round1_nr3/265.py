//KIA at Full speed ^_^
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;


int main(){
	FILE* in = fopen("C.in","r");
	FILE* out = fopen("C.out","w");
	int TestCase = 0;
	int A[30] = {5,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};
	fscanf(in, "%d\n", &TestCase);
	for(int i = 0; i < TestCase; i++)
	{	
		long long Answer = 0;
		long double rez, m = 3 + sqrt((double)5);
		rez = m;
		long Num;
		fscanf(in, "%d\n", &Num);
		/*for(long r = 1; r < Num; r++){
			rez *= m;
		//	rez = rez - 1000.0 * floor(rez / 1000.0);
		}
		Answer = floor(rez);
		Answer %= 1000;
		*/
		fprintf(out, "Case #%d: %.3d\n", i+1, A[Num-1]);
	}
	return 0;
}
