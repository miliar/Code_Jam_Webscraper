#include <iostream>
using namespace std;

char board[10][10];
int dir[][2] = {{1,0}, {0,1}, {1,1}, {1, -1}};

int valide(int r, int c){
	return r >= 0 && c >= 0 && r < 4 && c < 4;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, num_x, num_t, num_o, num_e;
	cin>>T;
	for(int tt = 0; tt < T; ++tt){
		for(int i = 0; i < 4; ++i)
			cin>>board[i];
		num_e = 0;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				if(board[i][j] == '.')
					++num_e;
			}
		}
		int win = 0; //1->x, 2->o
		for(int i = 0; i < 4 && !win; ++i){
			for(int j = 0; j < 4 && !win; ++j){
				if(i && j)continue;
				
				for(int d = 0; d < 4; ++d){
					num_t = num_o = num_x = 0;
					int r = i, c = j;
					while(valide(r, c)){
						if(board[r][c] == 'X')
							num_x++;
						else if(board[r][c] == 'O')
							num_o++;
						else if(board[r][c] == 'T')
							num_t++;
						r += dir[d][0];
						c += dir[d][1];
					}
					if(num_o == 4 || (num_o == 3 && num_t == 1))
						win = 2;
					if(num_x == 4 || (num_x == 3 && num_t == 1))
						win = 1;
				}
			}
		}
		cout<<"Case #"<<tt + 1<<": ";
		if(win == 1)
			cout<<"X won"<<endl;
		else if(win == 2)
			cout<<"O won"<<endl;
		else if(num_e != 0)
			cout<<"Game has not completed"<<endl;
		else 
			cout<<"Draw"<<endl;
	}
	return 0;
//	cout<<"hello world"<<endl;
//	system("pause");
} 
