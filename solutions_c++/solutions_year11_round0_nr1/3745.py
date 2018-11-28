#include<iostream>
using namespace std;

int main()
{
	int N;
	cin>>N;
	int count = 1;
	while(N--)
	{
		int n;
		cin>>n;
		int currentTime = 0;
		int lastOrange = 0;
		int lastBlue = 0;
		int orangePos = 1,bluePos = 1;
		bool lastMove = 0;
		for(int i=0;i<n;i++)
		{
			char robo;
			int move;
			int pos;
			cin>>robo>>move;
			pos = move;
			switch(robo)
			{
				case 'O' :
					move = orangePos - move;
					if(move < 0)
						move = -1 * move;
					move++;
					if(lastMove == 0)
						currentTime += move;
					else
						currentTime = (currentTime+1) > (lastOrange+move) ? currentTime + 1 : lastOrange + move;
						 
					lastMove = 0;
					lastOrange = currentTime;
					orangePos = pos;
					break;
				case 'B' :
					move = bluePos - move;
					if(move < 0)
						move = -1 * move;
					move++;
					if(lastMove == 1)
						currentTime += move;
					else
						currentTime = (currentTime+1) > (lastBlue+move) ? currentTime + 1 : lastBlue + move;
						 
					lastMove = 1;
					lastBlue = currentTime; 
					bluePos = pos;
					break;
			}
		}
		cout<<"Case #"<<count++<<": "<<currentTime<<endl;
	}
}
