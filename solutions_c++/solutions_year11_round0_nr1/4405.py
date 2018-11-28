#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

// 1st dimension - Button to be pressed
// 2nd dimension - Its place in the sequence
int TimeRequired(int orange[][2],int no, int blue[][2], int nb)
{
	// oIndex - Current index being examined for orange bot
	// oSpacesMoved - How much is to be subtracted from current index. Indicates
	//          how much the bot has moved
	int oIndex,bIndex,oSpacesMoved,bSpacesMoved,seq;
	bool oIncrease,bIncrease;
	oIncrease = bIncrease = true;
	oIndex = bIndex = 0;
	oSpacesMoved = bSpacesMoved = 1;
	seq = 1;
	int time;

	for(time=0;oIndex<no&&bIndex<nb;time++)
	{
		if(orange[oIndex][0]-oSpacesMoved != 0 && blue[bIndex][0]-bSpacesMoved != 0)
		{
			if(oIncrease)
				++oSpacesMoved;
			else
				--oSpacesMoved;

			if(bIncrease)
				++bSpacesMoved;
			else
				--bSpacesMoved;
		}

		else if(orange[oIndex][0]-oSpacesMoved == 0 && blue[bIndex][0]-bSpacesMoved != 0)
		{
			if(orange[oIndex][1]==seq)
			{
				// press the button here, else stay right there if this is
				// not orange's turn
				oIndex++;
				seq++;

				// decide whether to move forward or backwards for next
				// if this was last for orange, never mind
				if(oIndex < no)
				{
					if(orange[oIndex][0] < oSpacesMoved)
						oIncrease = false;
					else
						oIncrease = true;
				}
			}
			// move blue bot ahead or back
			if(bIncrease)
				++bSpacesMoved;
			else
				--bSpacesMoved;
		}

		else if(orange[oIndex][0]-oSpacesMoved != 0 && blue[bIndex][0]-bSpacesMoved == 0)
		{
			if(blue[bIndex][1]==seq)
			{
				bIndex++;
				seq++;

				if(bIndex < nb)
				{
					if(blue[bIndex][0] < bSpacesMoved)
						bIncrease = false;
					else
						bIncrease = true;
				}
			}
			if(oIncrease)
				++oSpacesMoved;
			else
				--oSpacesMoved;
		}
		else // both are at 0 difference
		{
			if(orange[oIndex][1]==seq)
			{
				oIndex++;
				if(oIndex < no)
				{
					if(orange[oIndex][0] < oSpacesMoved)
						oIncrease = false;
					else
						oIncrease = true;
				}
			}
			else
			{
				bIndex++;
				if(bIndex < nb)
				{
					if(blue[bIndex][0] < bSpacesMoved)
						bIncrease = false;
					else
						bIncrease = true;
				}
			}
			seq++;
		}
	}

	if(oIndex == no) // orange bot is up, move blue all the way
	{
		int addtime = 0;
		while(bIndex < nb)
		{
			// move ahead
			addtime += abs(blue[bIndex][0] - bSpacesMoved);
			bSpacesMoved = blue[bIndex][0];
			++addtime; // for button press;
			++bIndex;
		}
		time+=addtime;
	}

	else
	{
		int addtime = 0;
		while(oIndex < no)
		{
			// move ahead
			addtime += abs(orange[oIndex][0] - oSpacesMoved);
			oSpacesMoved = orange[oIndex][0];
			++addtime; // for button press;
			++oIndex;
		}
		time += addtime;
	}

	return time;
}

void TestTimeRequired()
{
	int orange[][2] = {0,0};
	int blue[][2] = {{2,1},{1,2}};
	int time = TimeRequired(orange,0,blue,2);
}

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		int orange[100][2],blue[100][2];
		int no,nb;
		no = nb = 0;
		int size;
		cin >> size;
		int seq = 1;
		for(int j=0;j<size;j++)
		{
			char code;
			int val;
			cin >> code >> val;
			if(code == 'O')
			{
				orange[no][0] = val;
				orange[no][1] = seq++;
				++no;				
			}
			else
			{
				blue[nb][0] = val;
				blue[nb][1] = seq++;
				++nb;
			}			
		}
		cout << "Case #"<<i+1<<": " << TimeRequired(orange,no,blue,nb) << endl;
	}
	return 0;
}