#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

struct button{
	char type;
	int num;
	int time;
	button(char type, int num)
	{
		this->type = type;
		this->num = num;
	};
};

void main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int cases =0;
	in>>cases;

	for(int i=0; i<cases; i++)
	{
		int N =0;
		in>>N;
		button** buttons = new button*[N];
		button** oButtons = new button*[N];
		int oCount = 0;
		button** bButtons = new button*[N];
		int bCount = 0;
		for(int j=0; j<N; j++)
		{
			int num;
			char type;
			in>>type>>num;
			if(type == 'O')
			{
				oButtons[oCount] = new button('O', num);
				buttons[j] = oButtons[oCount++];
			}
			else
			{
				bButtons[bCount] = new button('B', num);
				buttons[j] = bButtons[bCount++];
			}
		}
		int oIt(0),bIt(0);
		for(int j=0; j<N; j++)
		{
			if(buttons[j]->type == 'O')
			{
				if(oIt == 0)
				{
					int tmp = buttons[j]->num;
					if(bIt == 0) // 1st button in the test
					{
						oButtons[oIt]->time = tmp;
						oIt++;
					}
					else
					{
						if(bButtons[bIt-1]->time < tmp)
						{
							oButtons[oIt]->time = tmp;
							oIt++;
						}
						else
						{
							oButtons[oIt]->time = bButtons[bIt-1]->time+1;
							oIt++;
						}
					}
				}
				else
				{
					int tmp = abs(oButtons[oIt]->num - oButtons[oIt-1]->num) + oButtons[oIt-1]->time + 1;
					if(bIt == 0)
					{
						oButtons[oIt]->time = tmp;
						oIt++;
					}
					else
					{
						if(bButtons[bIt-1]->time < tmp)
						{
							oButtons[oIt]->time = tmp;
							oIt++;
						}
						else
						{
							oButtons[oIt]->time = bButtons[bIt-1]->time+1;
							oIt++;
						}
					}
					
				}
			}
			else
			{
				if(bIt == 0)
				{
					int tmp = buttons[j]->num;
					if(oIt == 0) // 1st button in the test
					{
						bButtons[bIt]->time = tmp;
						bIt++;
					}
					else
					{
						if(oButtons[oIt-1]->time < tmp)
						{
							bButtons[bIt]->time = tmp;
							bIt++;
						}
						else
						{
							bButtons[bIt]->time = oButtons[oIt-1]->time+1;
							bIt++;
						}
					}
				}
				else
				{
					int tmp = abs(bButtons[bIt]->num - bButtons[bIt-1]->num) + bButtons[bIt-1]->time + 1;
					if(oIt == 0)
					{
						bButtons[bIt]->time = tmp;
						bIt++;
					}
					else
					{
						if(oButtons[oIt-1]->time < tmp)
						{
							bButtons[bIt]->time = tmp;
							bIt++;
						}
						else
						{
							bButtons[bIt]->time = oButtons[oIt-1]->time+1;
							bIt++;
						}
					}
					
				}
			}
		}
		out<<"Case\t#"<<i+1<<":\t"<<buttons[N-1]->time<<endl;
	}
	in.close();
	out.close();
}