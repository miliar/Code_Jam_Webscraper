#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int T;
	fin>>T;
	for(int t = 1; t<=T; t++)
	{
		int C = 0;
		fin >> C;
		char comblist[26][26] = {};
		for(int c = 1; c<= C; c++)
		{
			char temp1, temp2, temp3;
			fin >> temp1;
			fin >> temp2;
			fin >> temp3;
			comblist[temp1 - 'A'][temp2- 'A'] = temp3;
			comblist[temp2 - 'A'][temp1- 'A'] = temp3;
		}
		int D;
		fin >> D;
		char dellist[26][26] = {};
		for(int d = 1; d <= D; d++)
		{
			char temp1, temp2;
			fin >> temp1;
			fin >> temp2;
			dellist[temp1 - 'A'][temp2- 'A'] = 'A';
			dellist[temp2 - 'A'][temp1- 'A'] = 'A';
		}

		//==go read input 
		int N;
		fin >> N;
		char* result = new char [N+1];
		int p = 0;
		char curr; 
		int appearedlist[26] = {0};
		for(int n = 1; n <= N; n++)
		{
			fin >> curr;
			if( p == 0)
			{
				result[p] = curr;
				appearedlist[curr- 'A']++;
				p++;
			}
			else
			{
				if( comblist[curr - 'A'][result[p-1] - 'A'] !=0  || comblist[result[p-1] - 'A'][curr - 'A'] !=0 )   // if in the combine list
				{
					appearedlist[comblist[curr - 'A'][result[p-1] - 'A']] ++;
					appearedlist[result[p-1] - 'A'] --;
					result[p-1] = comblist[curr - 'A'][result[p-1] - 'A'];
				}
				else 
				{
					bool clear = false;   // if in the del list. 
					for(int i = 0; i < 26; i++)
					{
						if(appearedlist[i] > 0 && (dellist[i][curr - 'A'] == 'A' || dellist[curr- 'A'][i] == 'A'))
						{
							p = 0;
							for(int j = 0; j < 26; j++) appearedlist[j] = 0;
							clear = true;
							break;
						}
						
					}
					if (!clear)
					{
						result[p] = curr;
						p++;
						appearedlist[curr - 'A'] += 1;
					}
				}
			}
		}
		result[p] = '\0';
		fout << "Case #" << t << ": [";
		if(p == 0)
			fout << "]" << endl;
		else
		{
			for(int k = 0; k < p -1; k++)
			{
				fout << result[k] <<", ";
			}
			fout<< result[p-1] << "]" <<endl;
		}
		delete[] result;
	}
	return 0;
}