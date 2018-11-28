#include <iostream>

#define BIT_SET(a,b) ((a) |= (1<<(b)))
#define NUM_SET(a,b) (((a) & (b)) == (b))

using namespace std;

void getBin(int num)
{
	while(num!=0)
	{
		cout << num % 2;
		num = num / 2;
	}
}

int main()
{
	int T = 0;
	cin >> T;
	for(int t=0;t<T;t++)
	{
		cout << "Case #" << (t+1) << ": ";

		int p1 = 0, p2 = 0, dr = 0;
		for(int i=0;i<16;i++)
		{
			char c;
			cin >> c;
			if (c == 'T')
			{
				BIT_SET(p1,i);
				BIT_SET(p2,i);
				BIT_SET(dr,i);
			}
			else if (c == 'X')
			{
				BIT_SET(p1,i);
				BIT_SET(dr,i);
			}
			else if (c == 'O')
			{
				BIT_SET(p2,i);
				BIT_SET(dr,i);
			}
		}

		//cout << p1 << " :: "; getBin(p1); cout << endl;
		//cout << p2 << " :: "; getBin(p2); cout << endl;
		//cout << dr << " :: "; getBin(dr); cout << endl;

		     if(NUM_SET(p1,0x000F))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0x00F0))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0x0F00))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0xF000))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0x1111))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0x2222))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0x4444))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0x8888))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0x8421))
			cout << "X won" << endl;
		else if(NUM_SET(p1,0x1248))
			cout << "X won" << endl;
		else if(NUM_SET(p2,0x000F))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0x00F0))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0x0F00))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0xF000))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0x1111))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0x2222))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0x4444))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0x8888))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0x8421))
			cout << "O won" << endl;
		else if(NUM_SET(p2,0x1248))
			cout << "O won" << endl;
		else if(NUM_SET(dr,0xFFFF))
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}
}
