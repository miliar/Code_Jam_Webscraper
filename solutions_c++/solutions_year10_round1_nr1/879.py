#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

int N, K;
char init[51][51];
char rot[51][51];

void blah(int offset, int level)	{
	
	if (level == 1)	{
		rot[offset][offset] = init[offset][offset];
		return;
	}
	// top right
	for (int i = 0; i < level; i++)	{
		rot[offset + i][offset + level - 1] = init[offset][offset + i];
	}
	
	// right down
	for (int i = 0; i < level; i++)	{
		rot[offset + level - 1][offset + level - 1 - i] = init[offset + i][offset + level - 1];
	}
	
	// bottom left
	for (int i = 0; i < level; i++)	{
		rot[offset + level - 1 - i][offset] = init[offset + level - 1][offset + level - i - 1];
	}
	
	// left up
	for (int i = 0; i < level; i++)	{
		rot[offset][offset + i] = init[offset + level - i - 1][offset];
	}
	
}

void rot90(int offset, int level)	{
	
	if (level == 1)	{
		rot[offset][offset] = init[offset][offset];
		return;
	}
	
	// top left right
	for (int i = 0; i < level/2; i++)	{
		rot[offset][i + level/2] = init[offset][i];
	}
	
	// top right right
	for (int i = level/2; i < level; i++)	{
		rot[offset + i - level/2][offset + level - 1] = init[offset][i];
	}
	
	// top right down
	for (int i = 0; i < level/2; i++)	{
		rot[offset + i + level/2][offset + level - 1] = init[offset + i][offset + level - 1];
	}
	
	// bottom right down
	for (int i = level/2; i < level; i++)	{
		rot[offset + level - 1][level - i + level/2 - 1] = init[offset + i][offset + level - 1];
	}
	
	// bottom right left
	for (int i = 0; i < level/2; i++)	{
		rot[offset + level - 1][level/2 - i] = init[offset + level - 1][offset + level - i - 1];
	}
	
	// bottom left left
	for (int i = level/2; i < level; i++)	{
		rot[offset + level - 1 - i + level/2][offset] = init[offset + level - 1][level - i - 1];
	}
	
	// bottom left up
	for (int i = 0; i < level/2; i++)	{
		rot[offset + level/2 - i][offset] = init[offset + level - 1 - i][offset];
	}
	
	// top left up
	for (int i = 0; i < level/2; i++)	{
		rot[offset][i] = init[offset + level/2 - i][offset];
	}
	
}

void printGridRot()	{
	cout <<"rot " << endl;
	for (int i = 0; i < N; i++)	{
		for (int j = 0; j < N; j++)	{
			cout << rot[i][j] << " " ;
		}
		cout << endl;
	}
}

void rotate()	{

	int temp = 0;
	int tempN = N;
	
	while (tempN > 0)	{
//  		cout << " shit " << temp << " " << tempN << endl;
		blah(temp, tempN);
// 		cout << temp << " " << tempN << endl;
//  		printGridRot();
		tempN = tempN - 2;
		temp++;
	}

}

void printGridInit()	{

	cout << " init" << endl;
	for (int i = 0; i < N; i++)	{
		for (int j = 0; j < N; j++)	{
			cout << init[i][j] << " " ;
		}
		cout << endl;
	}
}

void gravity()	{
	
	vector<int> height (N, 0);
	
	for (int i = N-1; i >= 0; i--)	{
		
// 		printGridRot();
		
		for (int j = 0; j < N; j++)	{
			if (rot[i][j] != '.')	{
				char temp = rot[i][j];
				rot[i][j] = '.';
				rot[N - height[j] - 1][j] = temp;
				height[j]++;
			}
		}
	}
}

bool bounds(int row, int col)	{
	return row < N && row >= 0 && col < N && col >= 0;
}

bool find(int row, int col)	{

	char temp = rot[row][col];
	bool blah;
	// down
	if (bounds(row + K - 1, col))	{
		blah = true;
		for (int i = 0; i < K; i++)	{
			if (rot[row + i][col] == temp)
				continue;
			else	{
				blah = false;
				break;
			}
		}
		
		if (blah)
			return blah;
	}
	
	// up
	if (bounds(row - K + 1, col))	{
		blah = true;
		for (int i = 0; i < K; i++)	{
			if (rot[row - i][col] == temp)
				continue;
			else	{
				blah = false;
				break;
			}
		}
		
		if (blah)
			return blah;
	}
	
	// right
	if (bounds(row, col + K - 1))	{
		blah = true;
		for (int i = 0; i < K; i++)	{
			if (rot[row][col + i] == temp)
				continue;
			else	{
				blah = false;
				break;
			}
		}
		
		if (blah)
			return blah;
	}
	
	// left
	if (bounds(row, col - K + 1))	{
		blah = true;
		for (int i = 0; i < K; i++)	{
			if (rot[row][col - i] == temp)
				continue;
			else	{
				blah = false;
				break;
			}
		}
		
		if (blah)
			return blah;
	}
	
	// upleft
	if (bounds(row + K  - 1, col - K + 1))	{
		blah = true;
		for (int i = 0; i < K; i++)	{
			if (rot[row + i][col - i] == temp)
				continue;
			else	{
				blah = false;
				break;
			}
		}
		
		if (blah)
			return blah;
	}
	
	// upright
	if (bounds(row + K  - 1, col+ K  - 1))	{
		blah = true;
		for (int i = 0; i < K; i++)	{
			if (rot[row + i][col+ i] == temp)
				continue;
			else	{
				blah = false;
				break;
			}
		}
		
		if (blah)
			return blah;
	}
	
	// downright
	if (bounds(row - K + 1, col+ K  - 1))	{
		blah = true;
		for (int i = 0; i < K; i++)	{
			if (rot[row - i][col+ i] == temp)
				continue;
			else	{
				blah = false;
				break;
			}
		}
		
		if (blah)
			return blah;
	}
	
	// downleft
	if (bounds(row - K + 1, col- K + 1))	{
		blah = true;
		for (int i = 0; i < K; i++)	{
			if (rot[row - i][col- i] == temp)
				continue;
			else	{
				blah = false;
				break;
			}
		}
		
		if (blah)
			return blah;
	}
	
	return false;
}

void solve(int testnum)	{
	
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			rot[i][j] = '.';
	
// 	printGridInit();
 	rotate();
	gravity();
// 	printGridRot();
	
	bool redwin = false;
	bool bluewin = false;
	for (int i = 0; i < N; i++)	{
		for (int j = 0; j < N; j++)	{
			
			if(rot[i][j] == '.')
				continue;
			
			if (rot[i][j] == 'R' && redwin)
				continue;
			
			if (rot[i][j] == 'B' && bluewin)
				continue;
			
			if (find(i,j))	{
				
				if (rot[i][j] == 'R')	{
					redwin = true;
				} else if (rot[i][j] = 'B')	{
					bluewin = true;
				}
			}
		}
	}
	
	if (redwin && bluewin)	{
		cout << "Case #" << testnum << ": Both" << endl;
		return;
	}
	
	if (redwin)	{
		cout << "Case #" << testnum << ": Red" << endl;
		return;
	}
	
	if (bluewin)	{
		cout << "Case #" << testnum << ": Blue" << endl;
		return;
	}
	
	cout << "Case #" << testnum << ": Neither" << endl;	
}

int main()	{
	
	int testnum;
	
	cin >> testnum;
	
	for (int i = 0; i < testnum; i++)	{
	
		cin >> N >> K;
		
		for (int j = 0; j < N; j++)	{
			cin >> init[j];
		}
		
		solve(i + 1);
	}
}