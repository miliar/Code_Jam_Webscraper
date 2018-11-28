#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int N, S, Q, X;
char Inputs[150];
string Input;

map< string, int > Engine2Number;
int Querie[1001];
int Search[1001];

void Init()
{
	S = 0;
	Q = 0;
	Engine2Number.clear();
}

void InputEngine()
{
	cin >> S;
	gets(Inputs);

	int EngineNumber = 0;
	
	for(int i = 0; i < S; i++ )
	{
		gets(Inputs);
		Input = Inputs;
		Engine2Number.insert( make_pair( Input, EngineNumber) );
		EngineNumber++;
	}

	/*//////////////////////////////////////////////////////////////////////////
	map<string,int>::iterator itr;
	for(itr = Engine2Number.begin(); itr != Engine2Number.end(); ++itr)
	{
		cout << itr->first << " : " << itr->second << endl;
	}
	//*/

}

void InputQueries()
{
	cin >> Q;
	gets(Inputs);

	map<string, int>::iterator itr;
	int Index = 0;
	for(int i = 0; i < Q; i++ )
	{
		gets(Inputs);
		Input = Inputs;
		itr = Engine2Number.find(Input);
		if( itr != Engine2Number.end() )
		{
			Querie[Index] = itr->second;
			Index++;
		}
	}

	Q = Index;

	/*//////////////////////////////////////////////////////////////////////////
	for(int i = 0; i < Q; i++ )
	{
		cout << "Querie[" << i <<"] : " << Querie[i] << endl;
	}
	//*/
}

void InputData()
{
	InputEngine();
	InputQueries();
}

void InitSelectEngine()
{
	for(int i = 0; i <= 1000; i++ )
	{
		Search[i] = 0;
	}
}

int MakeSelectEngine(int in)
{
	int Num = 1;
	for( int i = Q-1; i >= in ; i-- )
	{
		Search[Querie[i]] = Num;
		Num++;
	}
	
	int min = 9999;
	int minIndex;
	for( int i = 0; i < S; i++ )
	{
		if( Search[i] < min ) 
		{
			minIndex = i;
			min = Search[i];
		}
	}
	
	//cout << "Selected Engine : " << minIndex << endl;
	return minIndex;
}

int GetResult()
{
	int Index = 0;
	int result = 0;
	InitSelectEngine();
	int Engine = MakeSelectEngine(Index);
	while( Index < Q )
	{
		if( Querie[Index] == Engine )
		{
			InitSelectEngine();
			Engine = MakeSelectEngine(Index);
			result++;
		}
		else
		{
			Index++;
		}
	}

	return result;
}

int main()
{
	cin >> N;

	int Case = 1;

	while( N --> 0 )
	{
		Init();
		InputData();
		cout << "Case #" << Case << ": " << GetResult() << endl;

		Case++;
	}

	return 0;
}

