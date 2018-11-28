#include <iostream>
#include <stdio.h>

#define ct (int) 1e3

using namespace std;

int t, c, d, n, h; 
char map[ct][ct], list[ct]; 
bool del[ct][ct];

char Ins (char val)
{
	list[h++] = val;

	return val;
}

char Del ()
{       	
	return list[--h];
}

bool Check ()
{
	if (h == 1 || h == 0)
		return false;

   	if (map[ list[h - 1] ][ list[h - 2] ] >= 'A' && map[ list[h - 1] - 'A'][ list[h - 2] - 'A'] <= 'Z')
   	{
   		cerr << " Element " << Ins( map[Del()][Del()] ) << " appended ";

   		return true;
   	}

	for (int i = 0; i < h - 1; i++)
		if (del[ list[i] ][ list[h - 1] ])
		{
			cerr << " List has been deleted ";
			 
			h = 0;

			return true;
		}

	return false;
}
                                                             
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	freopen("log.txt", "w", stderr);

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cerr << endl << endl << endl;

		for (int j = 'A'; j <= 'Z'; j++)
			for (int k = 'A'; k <= 'Z'; k++)
				map[j][k] = '*', map[k][j] = '*';
		
		for (int j = 'A'; j <= 'Z'; j++)
			for (int k = 'A'; k <= 'Z'; k++)
				del[j][k] = false;
				 
		h = 0;

		cin >> c;
		for (int j = 0; j < c; j++)
		{
			char x, y, val;

			cin >> x >> y >> val;
			
			map[x][y] = val;
			map[y][x] = val;

			cerr << x << "+" << y << " -> " << val << endl;
		}            
		cerr << endl;

		cin >> d;
		for (int j = 0; j < d; j++)
		{
			char x, y;

			cin >> x >> y;


			del[x][y] = true;
			del[y][x] = true;

			cerr << x << "><" << y << endl;
		}
		cerr << endl;

		cin >> n;

		for (int j = 0; j < n; j++)
		{
			char val;

			cin >> val;
			cerr << val;
			
			Ins(val);

			while ( Check() );

			cerr << "	";
			for (int j = 0; j < h; j++)
				cerr << list[j] << ' ';	
			cerr << endl;
		}

		cout << "Case #" << i + 1 << ": [";
		
		if (h != 0)
		{
			for (int j = 0; j < h - 1; j++)
				cout << list[j] << ", ";
			cout << list[h - 1] << ']' << endl; 
		}
		else
			cout << "]" << endl;

		cerr << endl << endl << endl;
	}

	return 0;
}
