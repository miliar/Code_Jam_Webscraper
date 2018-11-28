#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		char cell[4][4];
		bool finish = true;
		string re("");
		for (int line = 0; line < 4; ++line)
		{
			for (int col = 0; col < 4; ++col)
			{
				cin>>cell[line][col];
				if(cell[line][col] == '.')
				{
					finish = false;
					continue;
				}
				if (col == 3)
				{
					bool find = true;
					char t = cell[line][col];
					if (cell[line][col] == 'T')
					{
						t = cell[line][0];
					}
					if(t!='.'){
						for (int thisline = 0; thisline < 4; ++thisline)
						{
							if(cell[line][thisline] != t 
								&& cell[line][thisline] != 'T')
							{
								find = false;
								break;
							}
						}

						if(find) 
						{
							re = string(1,t) + " won"; 
						}
					}
					
				}

				if (line == 3)
				{
					bool find = true;
					char t = cell[line][col];
					if (cell[line][col] == 'T')
					{
						t = cell[0][col];
					}
					if(t!='.'){
						for (int thisline = 0; thisline < 4; ++thisline)
						{
							if(cell[thisline][col] != t 
								&& cell[thisline][col] != 'T')
							{
								find = false;
								break;
							}
						}

						if(find) 
						{
							re = string(1,t) + " won"; 
						}
					}
				}

				if (line == 3 && col == 0)
				{
					bool find = true;
					char t = cell[line][col];
					if (cell[line][col] == 'T')
					{
						t = cell[0][3];
					}
					if(t!='.'){
						for (int thisline = 0; thisline < 4; ++thisline)
						{
							if(cell[3-thisline][thisline] != t 
								&& cell[3-thisline][thisline] != 'T')
							{
								find = false;
								break;
							}
						}

						if(find) 
						{
							re = string(1,t) + " won"; 
						}
					}
				}

				if (line == 3 && col == 3)
				{
					bool find = true;
					char t = cell[line][col];
					if (cell[line][col] == 'T')
					{
						t = cell[0][0];
					}
					if(t!='.'){
						for (int thisline = 0; thisline < 4; ++thisline)
						{
							if(cell[thisline][thisline] != t 
								&& cell[thisline][thisline] != 'T')
							{
								find = false;
								break;
							}
						}

						if(find) 
						{
							re = string(1,t) + " won"; 
						}
					}
				}
			}
		}

		cout<<"Case #"<<i+1<<": ";
		if (re.size() != 0)
		{
			cout<<re<<endl;
		} else if(finish){
			cout<<"Draw"<<endl;
		} else{
			cout<<"Game has not completed"<<endl;
		}
	}
	return 0;
}