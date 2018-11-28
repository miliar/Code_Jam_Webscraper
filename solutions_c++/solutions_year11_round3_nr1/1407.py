// A2

#include <iostream>
#include <string>

using namespace std;

int main(int nargs, char** args)
{
	int T, R, C;
	string row;

	char* pic;
	bool done = false;

	cin >> T;

	for(int t = 0; t < T; ++t)
	{
	    done = false;
		cin >> R >> C;
		pic = (char*)calloc(R*C+1,1);

		for(int r = 0; r < R; ++r)
		{
			cin >> row;
			memcpy(pic + r*C,row.c_str(),C);
		}

		for(int r = 0; r < R; ++r)
		{
			for(int c = 0; c < C; ++c)
			{
				if(pic[r*C+c] == '#') {
					if(r+1 >= R || c+1 >= C ||
						pic[(r+1)*C+c] != '#' ||
						pic[r*C+c+1] != '#' ||
						pic[(r+1)*C+c+1] != '#' ) {
						cout << "Case #" << t+1 << ":\nImpossible" << endl;
						/*for(int r1 = 0; r1 < R; ++r1)
						{
							for(int c1 = 0; c1 < C; ++c1)
							{
								cout << pic[r1*C+c1];
							}
							cout << "\n";
						}*/
						done = true;
						break;
					}

					if(!done) {
						// mark this square \/
						pic[r*C+c] = '/';
						pic[(r+1)*C+c] = '\\';
						pic[r*C+c+1] = '\\';
						pic[(r+1)*C+c+1] = '/';
						
						/*for(int r1 = 0; r1 < R; ++r1)
						{
							for(int c1 = 0; c1 < C; ++c1)
							{
								cout << pic[r1*C+c1];
							}
							cout << "\n";
						}*/


					}
				}
				if(done)
					break;
			}
			if(done)
				break;
		}

		if(!done) {
			cout << "Case #" << t+1 << ":\n";
			for(int r = 0; r < R; ++r)
			{
				for(int c = 0; c < C; ++c)
				{
					cout << pic[r*C+c];
				}
				cout << "\n";
			}

		}

		free(pic);
	}

	return 0;
}