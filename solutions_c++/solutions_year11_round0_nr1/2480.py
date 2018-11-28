#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

#define MAX 200
#define BUTTON 0
#define POS 1
#define orange 0
#define blue 1

int aim[2][MAX+1];
queue<char> moves;

int move_robot(int pos, int aim)
{
	if(aim > pos) return pos+1;
	else return pos-1;
}

int main()
{
	int T, N, k, l, b;
	int tempo, pressed, pos_b, pos_o;
	char r, next_move;
	bool flag;
	
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		cin >> N;
		k=0; l=0;
		for(int i=0; i<N; i++)
		{
			cin >> r;
			cin >> b;
			if(r == 'O') 
				aim[orange][k++] = b;	
			else
				aim[blue][l++] = b;
			moves.push(r);
		}
		pos_o = pos_b=1;
		pressed = k = l = 0;
		flag = true;
		
		next_move = moves.front();
		for(tempo=0; pressed < N; tempo++)
		{
			//~ printf("Next Robot: %c\n", next_move); 
			if(aim[orange][k] == pos_o)
			{
				if(next_move == 'O')
				{
					moves.pop();
					next_move = moves.front();
					pressed++; k++;
					//~ printf("pressed: %d; k: %d\n", pressed, k);
					flag = false;
				}
			}
			else pos_o = move_robot(pos_o, aim[orange][k]);
			
			if(aim[blue][l] == pos_b) 
			{
				if(next_move == 'B' && flag)
				{
					moves.pop();
					next_move = moves.front();
					pressed++; l++;
					//~ printf("pressed: %d; l: %d", pressed, l);
				}
			}
			else pos_b = move_robot(pos_b, aim[blue][l]);
			
			flag = true;
		}	
		cout << "Case #" << t << ": " << tempo << endl;
	}
	return 0;
}
			
