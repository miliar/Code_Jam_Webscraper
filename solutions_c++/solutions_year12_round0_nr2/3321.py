#include <iostream>
#include <vector>
#include <stdlib.h>
#include <Windows.h>

using namespace std;

void main()
{
	FILE* Input = fopen("B-large.in","r");
	FILE* Output = fopen("out.txt","w+");

	int T = 0;

	int _N = 0;
	int _S = 0;
	int _P = 0;
	int _ti = 0;
	int mod;
	int subb;

	vector<int> N;
	vector<int> S;
	vector<int> P;
	vector<int> ti;
	vector<vector<int>> t;
	int num_s;
	int answer;

	fscanf(Input, "%d\n", &T);
	
	for(int i=0; i<T; i++)
	{
		
		num_s  = 0;
		answer = 0;
		ti.clear();

		fscanf(Input, "%d %d %d", &_N, &_S, &_P);

		for(int j=0; j<_N; j++)
		{
			fscanf(Input, "%d", &_ti);
			ti.push_back(_ti);
		}

		N.push_back(_N);
		S.push_back(_S);
		P.push_back(_P);
		t.push_back(ti);
		if(_P==1)
		{
			for(int j=0;j<_N;j++)
			{
			if(t[i][j]>=1)answer++;
			}
		}
		else{
		for(int j=0; j<_N; j++)
		{
			
			if(t[i][j]>=(_P*3)-2)
			{
				answer++;
			}
			else if(t[i][j] == (_P*3)-3 || t[i][j] == (_P*3)-4)
			{
				num_s++;
			}

		}

		if(num_s > _S)
		{
			answer += _S;
		}
		
		else answer += num_s;
		}
		

		fprintf(Output,"Case #%d: %d\n",i+1,answer);
		}
		
	

	
	}


	//cout << N[0] << "," << S[0] << "," << P[0] << ",";


	//for(int i=0; i<t[0].size(); i++)
	//{
	//	cout << t[0][i] << ",";
	//}

