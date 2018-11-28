#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <stdio.h>

using namespace std;

int main(int argc, char ** argv)
{
	int N;
	ifstream f(argv[1]);
	f >> N ;
		
	string text;
	getline(f,text);
	for(int n=0; n<N; ++n)
	{
		vector<int> A;
		vector<int> Ap;

		string welcome="welcome to code jam";
		int wSize = welcome.size();
		getline(f,text);
		
		A.resize(wSize+1);
		Ap.resize(wSize+1);

		Ap[0]=1;
		for(int i=0; i<text.size(); ++i)
		{
			for(int j=0; j<wSize; ++j)
			{
				A[j]+=Ap[j];
				if(welcome[j]==text[i]) {A[j+1]+=Ap[j];}
			}
			A[wSize]+=Ap[wSize];
			Ap.swap(A);
			for(int j=0; j<wSize+1; ++j)
			{
				A[j]=0;
				Ap[j]%=10000;
			}
		}
		//cout << "Case #" << n+1 << ": " << Ap[wSize]%10000 << endl;
		printf("Case #%d: %04d\n",n+1,Ap[wSize]%10000);
	}


	return 0;
}
