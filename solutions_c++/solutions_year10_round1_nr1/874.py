#include <iostream>
#include <fstream>
#include <string>

using namespace std;


inline char getPos(char* array, int x, int y, int N)
{
	return array[x*N + y];
}

inline void setPos(char* array, int x, int y, int N, char val)
{
	array[x*N + y] = val;
}


void Gravity(char* array, int N)
{
	for(int i=0; i<N; i++)
	{
		int curPos = N-1;
		for(int j=N-1; j>=0; j--)
		{
			char curVal = getPos(array, i, j, N);
			if(curVal == '.')
			{
				continue;
			}

			setPos(array, i, curPos, N, curVal);
			curPos--;
		}

		while(curPos >=0)
			setPos(array, i, curPos--, N, '.');
	}
}

bool Check(char* array, int N, int K, char val)
{
	if(K > N)
		return false;
	//水平
	for(int i=0; i<N; i++)
	{
		int curNum = 0;
		for(int j=0; j<N; j++)
		{
			char curVal = getPos(array, i, j, N);
			if(curVal == val){
				curNum++;

				if(curNum == K)
					return true;
			}else
				curNum = 0;
		}
	}

	//垂直
	for(int i=0; i<N; i++)
	{
		int curNum =0;
		for(int j=0; j<N; j++)
		{
			char curVal = getPos(array, j, i, N);
			if(curVal == val){
				curNum++;

				if(curNum == K)
					return true;
			}else
				curNum = 0;
		}
	}

	//斜线
	for(int i=K-1; i<2*N-K; i++)
	{
		if(i<N)
		{
			int curNum =0;
			for(int j=0; j< i+1; j++)
			{
				char curVal = getPos(array, i-j, j, N);
				if(curVal == val){
					curNum++;
					if(curNum == K)
						return true;
				}else
					curNum = 0;
			}
		}
		else
		{
			int curNum = 0;
			for(int j=i-N+1; j<N; j++)
			{
				char curVal = getPos(array, i-j, j, N);
				if(curVal == val){
					curNum++;
					if(curNum == K)
						return true;
				}else
					curNum = 0;
			}
		}
	}

	//另一个斜线
	for(int i=K-1; i<2*N-K; i++)
	{
		if(i<N)
		{
			int curNum =0;
			for(int j=N-i; j<N; j++)
			{
				char curVal = getPos(array, j, j+i-N, N);
				if(curVal == val){
					curNum++;
					if(curNum == K)
						return true;
				}else
					curNum = 0;
			}
		}
		else
		{
			int curNum =0;
			for(int j=0; j<2*N-i; j++)
			{
				char curVal = getPos(array, j, j+i-N, N);
				if(curVal == val){
					curNum++;
					if(curNum == K)
						return true;
				}else
					curNum = 0;
			}
		}
	}
	return false;
}

void main(int argc, char* argv[])
{
	if(argc != 3)
	{
		cout<<"parameter error"<<endl;
		exit(0);
	}
	
	ifstream txtReader(argv[1]);
	ofstream resWriter(argv[2]);

	int nCase;
	int N;
	int K;
	txtReader>>nCase;
	for(int i=1; i<=nCase; i++)
	{
		
		//get case
		txtReader>>N>>K;
		char* array = new char[N*N];
		string strLine;
		for(int lineId=0; lineId<N; lineId++){
			txtReader>>strLine;
			for(int colId =0; colId <N; colId++)
			{
				setPos(array, lineId, colId, N, strLine[colId]);
			}
		}

		Gravity(array, N);

		bool resSec = Check(array, N, K, 'R');
		bool blueSec = Check(array, N, K, 'B');
		string res;
		if(resSec)
		{
			if(blueSec)
				res = "Both";
			else
				res = "Red";
		}else
		{
			if(blueSec)
				res = "Blue";
			else
				res = "Neither";
		}


		resWriter<<"Case #"<<i<<": "<<res<<endl;
		delete []array;
	}

	txtReader.close();
	resWriter.close();
}