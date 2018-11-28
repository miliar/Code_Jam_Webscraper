// acm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

enum situation{WAIT,MOVE,END};
struct Robot
{
	int current_pace;
	int current_target;
	situation s;
};

struct Pace
{
	int pace;
	char r;
};
char target;

int GetTarget(vector<Pace>& q, char c)
{
	if(q.empty())
	{
		return -1;
	}
	int res = -1;
	//bool flag = false;
	for(vector<Pace>::iterator i=q.begin(); i != q.end(); i++)
	{
		if(Pace((*i)).r == c)
		{
			res = Pace((*i)).pace;
	/*		if(i == q.begin())
			{
				flag = true;*/

			//}
			break;
		}
	}

	target = Pace(*q.begin()).r;
	//if(flag)
	//{
	//	q.erase(q.begin());
	//}

	return res;
}

int GetAnswer(vector<Pace>& q)
{
	if(q.empty())
	{
		return 0;
	}

	int res=0;
	Robot O,B;
	O.current_pace = 1;
	B.current_pace = 1;
	O.s = WAIT;
	B.s = WAIT;
	bool bPressed = false;

	B.current_target = GetTarget(q,'B');
	if(B.current_target == -1)
	{
		B.s = END;
	}
	O.current_target = GetTarget(q,'O');
	if(O.current_target == -1)
		O.s = END;
	while(B.s != END || O.s != END)
	{
		res++;
		bPressed = false;
		//if(B.s == WAIT)
		//{
		//	B.current_target = GetTarget(q,'B');
		//	if(B.current_target == -1)
		//	{
		//		B.s = END;
		//	}
		//}
		//if(O.s == WAIT)
		//{
		//	O.current_target = GetTarget(q,'O');
		//	if(O.current_target == -1)
		//		O.s = END;
		//}

		if(B.s != END)
		{
			B.s = MOVE;
			if(B.current_pace < B.current_target)
			{
				B.current_pace++;
			}
			else if(B.current_pace > B.current_target)
			{
				B.current_pace--;
			}
			else
			{
				if(target == 'B' && !bPressed)
				{
					q.erase(q.begin());
					bPressed = true;
					B.current_target = GetTarget(q,'B');
					if(B.current_target == -1)
					{
						B.s = END;
					}
					//B.s = WAIT;
				}
			}
		}

		if(O.s != END)
		{
			O.s = MOVE;
			if(O.current_pace < O.current_target)
			{
				O.current_pace++;
			}
			else if(O.current_pace > O.current_target)
			{
				O.current_pace--;
			}
			else
			{
				if(target == 'O'&& !bPressed)
				{
					q.erase(q.begin());
					bPressed = true;
					O.current_target = GetTarget(q,'O');
					if(O.current_target == -1)
						O.s = END;
					//O.s = WAIT;
				}
			}
		}

	}


	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T=0;

	vector< vector<Pace> > q;

	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("out.out");

	in>>T;
	int* N = new int[T];
	for(int i=0; i < T; i++)
	{
		in>>N[i];
		vector<Pace> temp;
		for(int j=0; j < N[i]; j++)
		{
			Pace p;
			in>>p.r;
			in>>p.pace;
			temp.push_back(p);
		}
		q.push_back(temp);
	}

	for(int i=0; i < T; i++)
	{
		int res = GetAnswer(q[i]);
		out<<"Case #"<<i+1<<": "<<res<<endl;
	}

	in.close();
	out.close();

	getchar();
	getchar();
	getchar();
	return 0;
}

