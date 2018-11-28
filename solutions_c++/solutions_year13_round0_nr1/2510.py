#include <fstream>
using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	int T;
	int board[4][4];
	int num=0;
	int state=0;
	fin>>T;
	for(int t=1;t<=T;t++)
	{
		char ch;
		num=0;
		while(num!=16)
		{
			fin>>ch;
			if(ch=='X'||ch=='.'||ch=='O'||ch=='T')
			{
				board[num/4][num%4]=ch;
				num++;
			}
		}
		//检查4行。
		char first;
		state=0;
		for(int i=0;i<4;i++)
		{
			first=board[i][0];
			if(first=='T')
			{
				first=board[i][1];
				if(first=='.') continue;
				else if(board[i][2]==first&&board[i][3]==first)
				{
					state=(first=='X')?1:2;
					break;
				}
			}
			else if(first=='.') continue;
			else
			{
				if((first==board[i][1]||'T'==board[i][1])&&(first==board[i][2]||'T'==board[i][2])&&(first==board[i][3]||'T'==board[i][3]))
				{
					state=(first=='X')?1:2;
					break;
				}
			}
		}
		//找四列。
		if(state==0)
		{
			for(int j=0;j<4;j++)
			{
				first=board[0][j];
				if(first=='T')
				{
					first=board[1][j];
					if(first=='.') continue;
					else if(board[2][j]==first&&board[3][j]==first)
					{
						state=(first=='X')?1:2;
						break;
					}
				}
				else if(first=='.') continue;
				else
				{
					if((first==board[1][j]||board[1][j]=='T')&&(first==board[2][j]||board[2][j]=='T')&&(first==board[3][j]||board[3][j]=='T'))
					{
						state=(first=='X')?1:2;
						break;
					}
				}
			}
		}
		//找两斜杠。
		if(state==0)
		{
			first=board[0][0];
			if(first=='T')
			{
				first=board[1][1];
				if(board[2][2]==first&&board[3][3]==first)
				{
					state=(first=='X')?1:2;
				}
			}
			else if(first=='.');
			else
			{
				if((first==board[1][1]||board[1][1]=='T')&&(first==board[2][2]||board[2][2]=='T')&&(first==board[3][3]||board[3][3]=='T'))
				{
					state=(first=='X')?1:2;
				}
			}
		}
		if(state==0)
		{
			first=board[0][3];
			if(first=='T')
			{
				first=board[1][2];
				if(first=='.');
				else if(board[2][1]==first&&board[3][0]==first)
				{
					state=(first=='X')?1:2;
				}
			}
			else if(first=='.');
			else
			{
				if((first==board[1][2]||board[1][2]=='T')&&(first==board[2][1]||board[2][1]=='T')&&(first==board[3][0]||board[3][0]=='T'))
				{
					state=(first=='X')?1:2;
				}
			}
		}
		//看满了没。
		if(state==0)
		{
			for(int i=0;i<3;i++)
			{
				for(int j=0;j<3;j++)
				{
					if(board[i][j]=='.')
					{
						state=4;
						break;
					}
				}
				if(state==4) break;
			}
			if(state==0) state=3;
		}
		switch(state)
		{
		case 1:fout<<"Case #"<<t<<": X won"<<endl;break;
		case 2:fout<<"Case #"<<t<<": O won"<<endl;break;
		case 3:fout<<"Case #"<<t<<": Draw"<<endl;break;
		case 4:fout<<"Case #"<<t<<": Game has not completed"<<endl;break;
		default:fout<<"ERROR"<<endl;break;
		}
	}
	fin.close();
	fout.close();
	return 0;
}

