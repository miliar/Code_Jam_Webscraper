///*

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int diff(int a, int b)
{
	int ret = (a-b > 0)?(a - b) : (b - a);

	return ret; 
}



int walk(vector<char> robots, vector<int> buttons, int T)
{
	//int T; 

	int p1 = 1; //orange
	int p2 = 1; //

	int s1;
	int s2; 

	bool t1 = false;
	bool t2 = false; 
	
	int count = 0; 
	int i , j; 
	
	for(i = 0; i < robots.size(); i++)
	{
		switch(robots[i])
		{
		case 'O':
			
			s1 = diff(p1, buttons[i]) + 1;

			if(!t2)
			{
			j = i+1;
			while(j < robots.size() && robots[j] == 'O' )
				j++;
			
			if(j < T)
			{
				s2 = diff(p2, buttons[j]);

				if(s1 >= s2)
				{
					p2 = buttons[j];
					//count += s1;

				}
				else p2 = buttons[j] > p2? p2 + s1: p2 - s1;   
			}
			else t2 = true; 
			}

			count += s1;

			p1 = buttons[i];
			break;
		case  'B':
			
			s2 = diff(p2, buttons[i]) + 1;
			
			if(!t1)
			{
				j = i+1;
			while(j < robots.size() && robots[j] == 'B' )
				j++;
			
			if(j < T)
			{
				s1 = diff(p1, buttons[j]);

				if(s2 >= s1)
				{
					p1 = buttons[j];
					//count += s1;

				}
				else p1 = buttons[j] > p1? p1 + s2: p1 - s2;   
			}
			else t1 = true; 
			}

			count += s2;
			p2 = buttons[i];
			break;
		}
	}

	return count; 
}
int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	
	int T;
	in>> T;

	string s;
	getline(in, s);
	
	int i, j; 

	for(i = 0; i < T; i++)
	{
		int N;
		in >> N;

		char ch;
		int cur;

		int p1 = 1;
		int p2 = 1; 
		vector<char> robots;
		vector<int> buttons;

		for(j = 0; j < N; j++)
		{
			in >> ch;
			in >> cur;

			robots.push_back(ch);
			buttons.push_back(cur);
		}

		out << "Case #"  << i+1 << ": " << walk(robots, buttons, N) << endl; 

		getline(in, s); 
	}

	return 0; 
}

//*/