#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stdio.h>

using namespace std;

#define CLEAR(x,with) memset(x,with,sizeof(x))  
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
	int N;
	string A;
	getline(cin, A);
	stringstream ss(A);
	ss >> N;
	for(int c=1; c<=N; c++)
	{
		cout << "Case #" << c << ": ";
		string number;
		vector<int> numbers2;
		getline(cin, number);

		for(int i=(int)number.size()-1; i>=0; i--)
		{
			for(int j=(int)number.size()-1; j>i; j--)
			{
				if(number[i] < number[j])
				{
					char temp = number[i];
					number[i] = number[j];
					number[j] = temp;
					vector<int> numbers;
					for(int k=i+1; k<(int)number.size(); k++)
						numbers.push_back((int)(number[k] - '0'));
					sort( all(numbers) );
					for(int k=i+1; k<(int)number.size(); k++)
						number[k] = numbers[k-i-1] + '0';
					goto endend;
				}
			}
		}
		// nothing found
		for(int k=0; k<(int)number.size(); k++)
			numbers2.push_back((int)(number[k] - '0'));
		sort( all(numbers2) );
		for(int k=0; k<(int)numbers2.size(); k++)
		{
			if(numbers2[k] == 0)
				continue;
			else
			{
				int temp = numbers2[k];
				numbers2[k] = numbers2[0];
				numbers2[0] = temp;
				break;
			}
		}
		for(int k=0; k<(int)number.size(); k++)
			number[k] = numbers2[k] + '0';
		cout << number[0] << "0";
		for(int i=1; i<(int)number.size(); i++) cout << number[i];
		goto endendend;
endend:;
		for(int i=0; i<(int)number.size(); i++) cout << number[i];
endendend:;
		cout << endl;
	}

	return 0;
}
