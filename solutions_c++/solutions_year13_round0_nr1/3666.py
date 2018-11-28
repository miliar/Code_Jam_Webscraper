#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <map>
#include <cstdlib>
#include <vector>
#include <iterator>
#include <fstream>
#include <list>
#include <queue>
#include <random>
#include <ctime>

#define M 4
using namespace std;

string Xwin[] = {"XXXT" , "XXTX" , "XTXX" , "TXXX" , "XXXX"};
string Owin[] = {"OOOT" , "OOTO" , "OTOO" , "TOOO" , "OOOO"};

bool isMatch(string a , string b[])
{
	for(int i = 0 ; i < 5 ; i ++)
	{
		if(a == b[i])
			return true;
	}
	return false;
}

int main()
{
	ifstream in("1.in");
	ofstream out("ans.out");
	int casen , k = 0;
	bool win = false;
	in >> casen;
	while(k < casen)
	{
		k ++;
		string a[M];
		string ans = "di";
		bool win = false;
		bool empty = false;
		string winp;
		for(int i = 0 ; i < M ; i ++)
		{
			in >> a[i];
		}
		//ºá
		for(int i = 0 ; i < M ; i ++)
		{
			if(isMatch(a[i] , Xwin))
			{
				win = true;
				winp = "X";
				break;
			}
			else if(isMatch(a[i] , Owin))
			{
				win = true;
				winp = "O";
				break;
			}
		}
		if(win)
		{
			out << "Case #" << k <<": " << winp << " won" << endl;
			continue;
		}
		//Êú
		for(int i = 0 ; i < M ; i ++)
		{
			string tmp;
			for(int j = 0 ; j < M ; j ++)
			{
				tmp.push_back(a[j][i]);
			}
			if(isMatch(tmp , Xwin))
			{
				win = true;
				winp = "X";
				break;
			}
			else if(isMatch(tmp , Owin))
			{
				win = true;
				winp = "O";
				break;
			}
		}
		if(win)
		{
			out << "Case #" << k <<": " << winp << " won" << endl;
			continue;
		}

		//Ð±
		string tmpT;
		string tmpF;
		for(int i = 0 ; i < M ; i ++)
		{
			tmpT.push_back(a[i][i]);
			tmpF.push_back(a[i][M - i - 1]);
		}
		if(isMatch(tmpT , Xwin) || isMatch(tmpF , Xwin))
		{
				win = true;
				winp = "X";
				
		}
		else if(isMatch(tmpT , Owin) || isMatch(tmpF , Owin))
		{
				win = true;
				winp = "O";
		}
		if(win)
		{
			out << "Case #" << k <<": " << winp << " won" << endl;
			continue;
		}
		for(int i = 0 ; i < M ; i ++)
		{
			for(int j = 0 ; j < M ; j ++)
			{
				if(a[i][j] == '.')
				{
					empty = true;
					break;
				}
			}
			if(empty)
			{
				break;
			}
		}
		if(empty)
		{
			out << "Case #" << k <<": Game has not completed" << endl;
		}
		else
		{
			out << "Case #" << k <<": Draw" << endl;
		}
		
	}
	return 0;
}