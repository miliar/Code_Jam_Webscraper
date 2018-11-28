using namespace std;

#include <iostream>
#include <queue>

struct Button {
	unsigned char who;
	unsigned int  but;
};

//#define TEST
//#define SMALL
#define LARGE
int main(void) {
#ifdef TEST
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

#ifdef SMALL
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	int T;
	int N;
	unsigned char R;
	int P;

	queue<int> orange;
	queue<int> blue;
	queue<Button>		path;

	

	int posO;
	int posB;
	
	int y;

	cin >> T;

	for(int i=0; i<T; i++){
		cin >> N;

		for(int j=0; j<N; j++)
		{
			cin >> R;
			cin >> P;

			if (R == 'O')
			{
				orange.push(P);
			}
			else
			{
				blue.push(P);
			}
			Button b;
			b.who = R;
			b.but = P;
			path.push(b);
		}

		posO = 1;
		posB = 1;

		y = 0;

		while(!path.empty())
		{
			bool found = false;
			Button b = path.front();

			if(posO != orange.front())
			{
				if(orange.front() > posO)
				{
					posO++;
				}
				else
				{
					posO--;
				}
			}
			else
			{
				if(b.who == 'O')
				{
					found = true;
					orange.pop();
				}
			}

			if(posB != blue.front())
			{
				if(blue.front() > posB)
				{
					posB++;
				}
				else
				{
					posB--;
				}
			}
			else
			{
				if(b.who == 'B')
				{
					found = true;
					blue.pop();
				}
			}

			if(found)
			{
				path.pop();
			}

			y++;
		}
		
		cout << "Case #" << (i+1) << ": " << y << endl;
		
	}
	return 0;
}
