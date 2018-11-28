#include <iostream>
#include <vector>

using namespace std;


struct Combine
{
	Combine(char a1, char b1, char c1):a(a1), b(b1), c(c1) { } 
	
	char a;
	char b;
	char c;
};

struct Oppose
{
	Oppose(char x1, char y1): x(x1), y(y1) { }
	
	char x;
	char y;
};


char canCombine(const vector<Combine>& comb, char a, char b)
{
	for(int i = 0; i < comb.size(); ++i)
	{
		if((comb[i].a == a && comb[i].b == b) || (comb[i].a == b && comb[i].b == a))
		{
			return comb[i].c;
		}
	}

	return ' ';
}

bool isOppose(const vector<Oppose>& opp, char x, char y)
{
	for(int i = 0; i < opp.size(); ++i)
	{
		if((opp[i].x == x && opp[i].y == y) || (opp[i].x == y && opp[i].y == x))
		{
			return true;
		}
	}

	return false;
}

int main()
{

	int n;

	cin >> n;

	for(int i = 0; i < n; ++i)
	{
		int C, D, N;

		char a1, b1, c1, x1, y1;
		char input;
		string str;

		vector<Combine> combine;
		vector<Oppose> oppose;

		cin >> C;
		for(int j = 0; j < C; ++j)
		{
			cin >> a1 >> b1 >> c1;

			combine.push_back(Combine(a1, b1, c1));
		}

		cin >> D;
		for(int j = 0; j < D; ++j)
		{
			cin >> x1 >> y1;

			oppose.push_back(Oppose(x1, y1));
		}

		cin >> N;
		for(int j = 0; j < N; ++j)
		{
			cin >> input;

			bool comOrOpp = false;
			if(str.size() > 0)
			{
				char combineout = canCombine(combine, input, str[str.size() - 1]);
				if(combineout != ' ')
				{
					str[str.size() - 1] = combineout;
					comOrOpp = true;
				}
			}
			if(!comOrOpp)
			{
				for(int k = 0; k < str.size(); ++k)
				{
					if(isOppose(oppose, str[k], input))
					{
						str.clear();
						comOrOpp = true;
					}
				}
			}
			if(!comOrOpp) str.push_back(input);
		}
		

		cout << "Case #" << i + 1 << ": [";
		for(int j = 0; j < str.size(); ++j)
		{
			cout << str[j];
			if(j != str.size() - 1)
				cout << ", ";
		}
		cout << "]" << endl;
	}

	return 0;
}
		
		
			
