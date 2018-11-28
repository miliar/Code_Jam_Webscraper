#include <iostream>
#include <string.h>
#include <queue>
#include <fstream>
using namespace std;

class Robot
{
public:
	int Position;
	queue<int> Aim;
	queue<int> Order;
	bool waited ;
	Robot()
	{
		Position=1;
		waited = false;

	}
};


int main()
{
	ifstream Input("Input0.txt");
		ofstream Output("Output.txt");
int BOrder;
	int T;
	Input>>T;
	for(int j=1;j<=T;j++)
	{
		Robot O;
		Robot B;
		int N;
		Input>>N;

		for(int i=0;i<N;i++)
		{
			char RobotType;
			Input>>RobotType;
			if (RobotType == 'O')
			{
				int g;
				Input>>g;
				O.Aim.push(g);
				O.Order.push(i);

			}
			if (RobotType == 'B')
			{
				int g;
				Input>>g;
				B.Aim.push(g);
				B.Order.push(i);

			}
		}
		int q=0;
		while (!(B.Aim.empty() && O.Aim.empty())) 
		{

			if(!B.Aim.empty())
			{
			BOrder=B.Order.front();

				if(B.Aim.front()== B.Position)
				{
					if(!O.Aim.empty())
					{
						if(B.Order.front()< O.Order.front()/*&& B.waited == true*/)
						{
							B.Order.pop();
							B.Aim.pop();
							B.waited= false;
						}
						else
						{
							B.waited = true;
						}
					}
					else /*if (B.waited == true)*/
						{
							B.Order.pop();
							B.Aim.pop();
							B.waited = false;
						}
					//else 
					//		B.waited = true;

				}
				else
				{
					if(B.Position > B.Aim.front())
						B.Position--;
					if(B.Position < B.Aim.front())
						B.Position++;
				}
			}
			else 
			{
				BOrder=99999;
			}
			if(!O.Aim.empty())
			{
			

				if(O.Aim.front()== O.Position)
				{
					{
						if(O.Order.front()< BOrder/*&& O.waited == true*/)
						{
							O.Order.pop();
							O.Aim.pop();
							O.waited= false;
						}
						else if(B.Aim.empty())
						{
							BOrder = 9999999;
							O.waited = true;
						}
					}
						
				}
				else
				{
					if(O.Position > O.Aim.front())
						O.Position--;
					if(O.Position < O.Aim.front())
						O.Position++;
				}
			}
			q++;

		}
		Output<<"Case #"<<j<<": "<<q<<endl;

	}

}

