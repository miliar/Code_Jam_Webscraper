#include <iostream>
#define MAX_MOVES 100

using namespace std;

typedef struct tag_robot
{
	char color;
	int buttons[MAX_MOVES], buttonsI;
	int currButton, totalButtons;
	int move(char currBotColor)
	{
		if (buttonsI >= totalButtons)
			return 0;
		int pushed = 0;
		if (currButton > buttons[buttonsI])
		{
			currButton--;
			//cout << color << " moveu para botao " << currButton << endl;
		}
		else if (currButton < buttons[buttonsI])
		{
			currButton++;
			//cout << color << " moveu para botao " << currButton << endl;
		}else if (currBotColor == color)
		{
			//cout << color << " pressionou " << currButton << endl;
			currButton = buttons[buttonsI++];
			pushed = 1;
		}
		return pushed;
	}
} robot;

typedef struct tag_moves
{
	char moves[MAX_MOVES];
	int totalMoves, currMove;
} moves;

int main()
{
	int ncases, ccase = 0;
	cin >> ncases;
	while (ccase++ < ncases)
	{
		moves m;
		m.currMove = 0;
		cin >> m.totalMoves;
		
		robot atlas, pbody;
		atlas.color = 'B'; pbody.color = 'O';
		atlas.currButton = pbody.currButton = 1;
		atlas.totalButtons = atlas.buttonsI = pbody.totalButtons = pbody.buttonsI = 0;
		
		for (int i=0; i<m.totalMoves; i++)
		{
			char robot; int button;
			cin >> robot >> button;
			m.moves[i] = robot;
			if (robot == 'O')
			{
				pbody.buttons[pbody.totalButtons++] = button;
			}else
			{
				atlas.buttons[atlas.totalButtons++] = button;
			}
		}
		
		int time = 0;
		while (m.currMove < m.totalMoves)
		{
			time++;
			//cout << "tempo: " << time << endl;
			char currBotColor = m.moves[m.currMove];
			int atlasMove = atlas.move(currBotColor);
			int pbodyMove = pbody.move(currBotColor);
			if (atlasMove || pbodyMove)
				m.currMove++;
		}
		cout << "Case #" << ccase << ": " << time << endl;
	}
}
