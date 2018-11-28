#include <iostream>
#include <string>

using namespace std;

const int maxN = 100;
const int maxLen = 500;
const char pattern[] = "welcome to code jam";
const size_t pLen = sizeof(pattern)-1;
char s[maxLen+1];
int F[maxLen+1][pLen+1];

int main()
{
	int N;
	cin >> N;
	cin.ignore(maxLen,'\n'); // skipping end-of-line
	for(int t=1; t<=N; t++){
		/************************************
			Input Data
		*************************************/
		//cout << L << ' ' << D << ' ' << N << endl;
		//getline(cin,s,'\n'); // ignore eoln
		//getline(cin,s,'\n');
		cin.getline(s,maxLen+1);
		/************************************
			Solve the Problem
		*************************************/
		size_t len = strlen(s);
		for(size_t L=0; L<=len; L++)
			F[L][0] = 1;
		for(size_t L=1; L<=pLen; L++)
			for(size_t K=L+1; K<pLen; K++)
				F[L][K] = 0;
		for(size_t L=1; L<=len; L++)
		{
			for(size_t K=1; K<=pLen; K++)
			{
				F[L][K] = ((s[L-1]==pattern[K-1]? F[L-1][K-1] : 0) + F[L-1][K]) % 10000;
				//printf_s(" %04d", F[L][K]);
			}
			//printf_s("\n");
		}
		/************************************
			Output Results
		*************************************/
		//cout << "Case #" << t << ":" << endl;
		printf_s("Case #%d: %04d\n", t, F[len][pLen]);
		/* Debug
		*/
	}
	return 0;
}

