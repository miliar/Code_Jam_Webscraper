#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int main(void)
{
	int L, D, N;
	bool valid[16][26];
	vector<string> knownWords;
	
	cin >> L >> D >> N;
	
	for(int i = 1; i <= D; i++)
	{
		string word;
		
		cin >> word;
		knownWords.push_back(word);
	}
	
	for(int i = 1; i <= N; i++)
	{
		memset(valid, 0, sizeof(valid));
		
		for(int j = 0; j < L; j++)
		{
			char aux;
			
			cin >> aux;
			if(aux == '(')
			{
				while(cin >> aux && aux != ')') valid[j][aux - 'a'] = true;
			}
			else valid[j][aux - 'a'] = true;
		}
		
		int numValids = D;
		vector<string>::iterator it = knownWords.begin(), end = knownWords.end();
		while(it != end)
		{
			for(int i = 0; i < L; i++)
			{
				if(!valid[i][it->at(i) - 'a'])
				{
					numValids--;
					break;
				}
			}
			
			it++;
		}
		cout << "Case #" << i << ": " << numValids << endl;
	}
}
