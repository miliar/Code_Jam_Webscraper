#include <iostream>
using namespace std;
bool test_direction_with_map(char map[][4],short dir_x,short dir_y,char pos_x,char pos_y,char player,char count)
{
	if((pos_x+dir_x)<0 || (pos_x+dir_x)>3 || (pos_y+dir_y)<0 || (pos_y+dir_y)>3)
		return false;
	if(map[pos_y+dir_y][pos_x+dir_x]!=player&&map[pos_y+dir_y][pos_x+dir_x]!='T')
		return false;
	else if(count==3)
		return true;
	else
		return test_direction_with_map(map,dir_x,dir_y,pos_x+dir_x,pos_y+dir_y,player,count+1);
}

char test_point(char map[][4],char pos_x,char pos_y)
{
	short dir[8][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
	for(char i=0;i<8;i++)
		if(test_direction_with_map(map,dir[i][1],dir[i][0],pos_x,pos_y,map[pos_y][pos_x],1))
			return map[pos_y][pos_x];
	return 0;
}

char test_map(char map[][4])
{
	char winner;
	bool count_dot=false;
	for(char i=0;i<4;i++)
		for(char j=0;j<4;j++)
		{
			if(map[i][j]!='.' && map[i][j]!='T')
			{
				winner=test_point(map,j,i);
				if(winner)
					return winner;
			}
			else if(map[i][j]=='.'&&!count_dot)
				count_dot=true;
		}
	return int(count_dot);
}

int main()
{
	short T;
	cin>>T;
	getchar();
	for(short t=1;t<=T;t++)
	{
		char map[4][4];
		for(char i=0;i<4;i++)
		{
			for(char j=0;j<4;j++)
				map[i][j]=getchar();
			getchar();
		}
		getchar();
		char winner=test_map(map);
		cout<<"Case #"<<t<<": ";
		switch(winner)
		{
			case 1: cout<<"Game has not completed"<<endl;break;
			case 0: cout<<"Draw"<<endl;break;
			default: cout<<winner<<" won"<<endl;break;
		};
	}
	return 0;
}