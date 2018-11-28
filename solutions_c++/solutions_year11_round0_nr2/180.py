
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

struct myPair
{
	char a;
	char b; 
};

struct triple
{
	char a;
	char b;
	char c;
};

bool isCombined(vector<triple> combine, myPair p, char & answer)
{
	for(int i = 0; i < combine.size(); i++)
	{
		if(p.a == combine[i].a)
		{
			if(p.b == combine[i].b)
			{
				answer = combine[i].c;
				return true;
			}
		}
		if(p.b == combine[i].a)
		{
			if(p.a == combine[i].b)
			{
				answer = combine[i].c;
				return true;
			}
		}
	}
	return false; 
}

bool isOpposed(vector<myPair> oppose, vector<char> elemList, char ch)
{
	vector<myPair> specific; 
	int i, j; 

	for(i = 0; i < oppose.size(); i++)
	{
		bool t = false;
		char cur;
		if(oppose[i].a == ch)
		{
			cur = oppose[i].b;
			t = true;
		}
		else if(oppose[i].b == ch)
		{
			cur = oppose[i].a;
			t = true;
		}

		if(t)
		{
			for(j = 0; j < elemList.size(); j++)
			{
				if(cur == elemList[j])
					return true;
			}
		}
	}
	return false; 

}

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	
	int i, j;
	int T; 

	string s; 
	
	

	in >> T; 
	for(i = 0; i < T; i++)
	{
		vector<char> retList;
		vector<myPair> oppose;
		vector<triple> combine;
		
		//string s;
		myPair p;
		triple tt; 

		int C, D, N;

		in >> C;
		
		for(j = 0; j < C; j++)
		{
			in >> s;
			tt.a = s[0];
			tt.b = s[1];
			tt.c = s[2];

			combine.push_back(tt); 
		}

		in >> D; 
		for(j = 0; j < D; j++)
		{
			in >> s;
			p.a = s[0];
			p.b = s[1];

			oppose.push_back(p);
		}

		in >> N;

		in >> s; 
		
		int end;
		char ch;
		for(j = 0; j < N; j++)
		{
			end = retList.size();
			if(end > 0)
			{
				p.a = s[j];
				p.b = retList[end - 1];

				if(isCombined(combine, p, ch))
				{
					retList[end - 1] = ch;
				}
				else if(isOpposed(oppose, retList, s[j]))
				{
					retList.clear();
				}
				else retList.push_back(s[j]);
			}
			else
				retList.push_back(s[j]);

		}
		
		
		out << "Case #" << i+1 << ": ["; 
		if(retList.size() > 0)
		{
		for(j = 0; j < retList.size() - 1; j++)
		{
			out<<retList[j] << ", ";
		}
		out << retList[j];
		}
		
		
		out << "]" << endl;

	}



	return 0; 
}
