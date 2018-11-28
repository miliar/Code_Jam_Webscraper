#include <iostream>
#include <string.h>
#include <map>
using namespace std;

struct s_clean
{
	char a, b;
} clean[50];

int elements[256];

void check_combine(string &element_list, map<pair<char, char>, char> &combine)
{
	size_t size = element_list.size();
	if(size > 1 && combine[make_pair(element_list[size - 1], element_list[size - 2])])
	{
		char e = combine[make_pair(element_list[size - 1], element_list[size - 2])];
		
		elements[(int)element_list[size - 1]]--;
		elements[(int)element_list[size - 2]]--;
		elements[(int)e]++;
		
		element_list.replace(size - 2, 2, &e);
		check_combine(element_list, combine);
	}
}

void check_clean(string &element_list, int D)
{
	for(int i = 0; i < D; i++)
	{
		if(elements[(int)clean[i].a] && elements[(int)clean[i].b])
		{
			element_list.clear();
			memset(elements, 0, sizeof(elements));
		}
		return;
	}
}

int main(void)
{
	int T, C, D, N;
	char a, b, c;
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++)
	{
		map<pair<char, char>, char> combine;
		
		memset(elements, 0, sizeof(elements));
		
		cin >> C;
		for(int i = 0; i < C; i++)
		{
			cin >> a >> b >> c;
			combine[make_pair(a, b)] = c;
			combine[make_pair(b, a)] = c;
		}
		
		cin >> D;
		for(int i = 0; i < D; i++) cin >> clean[i].a >> clean[i].b;
		
		string element_list = "";
		cin >> N;
		for(int i = 0; i < N; i++)
		{
			char e;
			
			cin >> e;
			element_list += e;
			elements[(int)e]++;

			check_combine(element_list, combine);
			check_clean(element_list, D);
		}
		
		cout << "Case #" << numCase << ": [";
		if(element_list.size()) cout << element_list[0];
		for(size_t i = 1; i < element_list.size(); i++) cout << ", " << element_list[i];
		cout << "]" << endl;
	}
}
