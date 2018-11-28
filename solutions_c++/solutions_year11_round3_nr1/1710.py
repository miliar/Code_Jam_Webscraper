#include <iostream>
using namespace std;

char matrix[51][51];
int R, C;

int fill(char buffer[51][51], int i, int j)
{
	if(i>=(R-1) || j>=(C-1))
		return 1;
	if(buffer[i][j+1] != '#' || 
	   buffer[i+1][j] != '#' ||
	   buffer[i+1][j+1] != '#')
		return 1;
	
	buffer[i][j] = buffer[i+1][j+1] = '/';
	buffer[i+1][j] = buffer[i][j+1] = '\\';
	return 0;
}

void processCase(int casenum)
{
	char buffer[51][51];
	memcpy(buffer, matrix, sizeof(matrix));
	
	for(int i=0; i<R; i++)
	{
		for(int j=0; j<C; j++)
		{
			if(buffer[i][j] == '#')
			{
				int rc = fill(buffer, i, j);
				if (rc) {
					cout << "Case #" << casenum << ":" << endl;
					cout << "Impossible" << endl;
					return;
				}
			}
		}
	}
	cout << "Case #" << casenum << ":" << endl;
	for(int i=0; i<R; i++)
	{
		for(int j=0; j<C; j++)
			cout << buffer[i][j];
		cout << endl;
	}
	
}

int main (int argc, char * const argv[]) {
    int T;
	
	cin >> T;
	for(int i=1; i<=T; i++)
	{
		cin >> R >> C;
		for (int j=0; j< R;j++)
			for(int k=0;k<C; k++)
			{
				char c;
				cin >> c;
				matrix[j][k]=c;
			}
		processCase(i);
	}
    return 0;
}
