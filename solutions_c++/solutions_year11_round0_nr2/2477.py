#include <iostream>

using namespace std;

		int N, C, D;
		const int maxC=36, maxD=28, maxN=100;
		char AC[maxC][3], AD[maxD][2], series[maxN];
		char res[maxN];
		int nres;
char Combine(int nres, char c)
{
	if(nres>0)
	for(int i=0; i< C; i++)
		if( (AC[i][0]==res[nres-1] && AC[i][1]==c) || (AC[i][1]==res[nres-1] && AC[i][0]==c) )
			return AC[i][2];
	return '\0';
}

bool isOpposed(char c)
{
	for(int i=0; i<D; i++)
		for(int j=0; j<nres; j++)
			//if( (AD[i][0]==c && counts(AD[i][1]>0) || (AD[i][1]==c && counts(AD[i][0]>0) )
			if( (AD[i][0]==c && AD[i][1]==res[j]) || (AD[i][1]==c && AD[i][0]==res[j]) )
				return true;
	return false;
}

int main()
{
	//cout << "Hello!!!" << endl;
	//return 0;
	int T;

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		cin >> C;
		for(int i=0; i<C; i++)
			cin >> AC[i][0] >> AC[i][1] >> AC[i][2];
		cin >> D;
		for(int i=0; i<D; i++)
			cin >> AD[i][0] >> AD[i][1];
		cin >> N;
		for(int i=0; i<N; i++)
			cin >> series[i];
		/************************************
		*	Solve the Problem
		*************************************/
		nres=0;
		res[nres++]=series[0];
		for(int i=1; i<N; i++)
		{
			char c=series[i];
			char p;
			// Try to combine
			if((p=Combine(nres,c))!='\0')
				res[nres-1]=p;
			else if(isOpposed(c))
				nres=0;
			else
				res[nres++]=c;
		}
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": [";
		if(nres>0) 
			cout << res[0];
		for(int i=1; i<nres; i++)
			cout << ", " << res[i];
		cout << ']' << endl;
	}

	return 0;
}
