#include <iostream>
#include <string>
#include <fstream>
using namespace std;

bool startoppose(string &_result, char first, char last);

int main()
{
	int testcase = 0;
	int C =0;
	int D =0;
	int N =0;
	string * combine;
	string * oppose;
	string stringcase;
	string result;

	ofstream f("save.txt");

	cin>>testcase;
	
	for(int i =0 ; i < testcase ; i++)
	{
		result.clear();
		cin>>C;
		
		combine = new string[C];
		for(int j=0; j < C; j++)
		{
			cin>>combine[j];
		}

		
		cin>>D;
		oppose = new string[D];
		for(int j=0; j < D; j++)
		{
			cin>>oppose[j];
		}
		cin>>N;
		cin>>stringcase;

		//작업 시작!
		for(int j=0 ; j < N; j++)
		{
			
			result.push_back(stringcase[j]);
			if(result.length() > 1)
			{
				//combine case
				for(int k = 0; k < C ; k++)
				{
					if( (result[result.size()-1] == combine[k][0] && result[result.size()-2] == combine[k][1]) || (result[result.size()-1] == combine[k][1] && result[result.size()-2] == combine[k][0]) )
					{
						result.erase(result.size()-1);
						result.erase(result.size()-1);
						result.push_back(combine[k][2]);
						
						break;
					}
				}

				//oppose case  selection 소트 형식으로 하자
				for(int k = 0; k < D ; k++)
				{
					bool check = false;
					if(startoppose(result,oppose[k][0],oppose[k][1]))
					{
						check = true;
					}
					else if(startoppose(result,oppose[k][1],oppose[k][0]))
					{
						check = true;
					}

					if(check)
					{
						break;
					}

				}
				
			}

			

		}
		f<<"Case #"<<i+1<<": [";
		for(int a = 0; a < result.length() ; a++)
		{
			if(a == result.size()-1)
			{
				f<<result[a];
			}
			else
			{
				f<<result[a]<<", ";
			}
			
		}
		f<<"]"<<endl;
	}

	
	return 0;
}

bool startoppose(string &_result, char first, char last)
{
	for(int m = 0; m < _result.size() ; m++)
	{
		if(_result[m] == first)
		{
			for(int m_m = m+1 ; m_m < _result.size() ; m_m++)
			{
				if(_result[m_m] == last)
				{
					_result.clear();
					return true;
				}
			}
		}
		if(_result[m] == last)
		{
			for(int m_m = m+1 ; m_m < _result.size() ; m_m++)
			{
				if(_result[m_m] == first)
				{
					_result.clear();
					return true;
				}
			}
		}
		
	}
	return false;
}