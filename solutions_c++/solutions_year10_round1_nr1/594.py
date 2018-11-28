#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

string arr[100];
int n, k;

bool ver (int x, int y, char c)
{
	int s = 0;
	while(x < n && arr[x++][y] == c && s < k) s++;
	return s == k;
}

bool hor (int x, int y, char c)
{
	int s = 0;
	while(y < n && arr[x][y++] == c && s < k) s++;
	return s == k;
}

bool diag_right (int x, int y, char c)
{
	int s = 0;
	while(y < n && x < n && arr[x++][y++] == c && s < k) s++;
	return s == k;
}

bool diag_left (int x, int y, char c)
{
	int s = 0;
	while(y < n && x < n && arr[x++][y--] == c && s < k) s++;
	return s == k;
}

int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t;
	cin >> t;
	for(int cnt = 0; cnt < t; cnt++)
	{
		cin >> n >> k;
		for(int i = 0; i < n; i++)
		{
			arr[i] = "";
			for(int j = 0; j < n; j++)
			{
				char c;
				cin >> c;
				if(c != '.') arr[i] += c;
			}
			while(arr[i].length() < n)
				arr[i] = '.' + arr[i];
		}
		
		bool red = false, blue = false;
		for(int i = 0; i <= n - k && (!red || !blue); i++)
			for(int j = 0; j < n && (!red || !blue); j++)
			{
				if(ver(i, j, 'R')) red = true;
				if(ver(i, j, 'B')) blue = true;
			}
			
		for(int i = 0; i < n && (!red || !blue); i++)
			for(int j = 0; j <= n - k && (!red || !blue); j++)
			{
				if(hor(i, j, 'R')) red = true;
				if(hor(i, j, 'B')) blue = true;
			}
			
		for(int i = 0; i <= n - k && (!red || !blue); i++)
			for(int j = 0; j <= n - k && (!red || !blue); j++)
			{
				if(diag_right(i, j, 'R')) red = true;
				if(diag_right(i, j, 'B')) blue = true;
			}
			
		for(int i = 0; i <= n - k && (!red || !blue); i++)
			for(int j = k - 1; j < n && (!red || !blue); j++)
			{
				if(diag_left(i, j, 'R')) red = true;
				if(diag_left(i, j, 'B')) blue = true;
			}
		
		cout << "Case #" << cnt + 1 << ": ";
		if(red && blue) cout << "Both";
		else if(blue) cout << "Blue";
		else if(red) cout << "Red";
		else cout << "Neither";
		cout << endl;
	}
}
