//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;
char str[51][51];
int n;

int checkxy(char c, int x, int y, int xx, int yy, int k) {
	if (k==0) return 1;
	if (x+xx ==n ) return 0;
	if (y+yy == n) return 0;
	if (str[x+xx][y+yy] == c) checkxy(c, x+xx,y+yy,xx,yy,k-1);
	else return 0;
}

int check(char c,  int k) {

		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				if (str[i][j] == c)
				{
					int flag;
					flag = checkxy(c, i,j,1, 0, k-1);
					if (flag) return 1;
					flag = checkxy(c, i,j,0, 1, k-1);
					if (flag) return 1;
					flag = checkxy(c, i,j,1, 1, k-1);
					if (flag) return 1;
					flag = checkxy(c, i,j,1, -1, k-1);
					if (flag) return 1;
				}

	return 0;
}
int main()
{
	int l,k, a[51],flagr,flagl;

	char c;
	ifstream in("A.in");
	ofstream out("A.out");
	in >> l;
	string line;
	for (int p=0;p<l;p++)
	{
		in >> n >> k;
		for (int y=0;y<n;y++) {
			a[y] = n-1;
			for (int x=0;x<n;x++)
				str[x][y] = 'E';
		}

		getline(in, line);
		for (int i=0;i<n;i++) {
			getline(in, line);
		
			istringstream iss(line);
			line = ' ';
			while (iss >> c)
				line = c + line;
			istringstream iss2(line);

			while (iss2 >> c)
				if (c != '.') { str[i][a[i]] = c;a[i]--; }

		}
		flagr = check('R',  k);
		flagl = check('B',  k);
		out << "Case #" << p+1 << ": "  ;
		if ((flagr)&&(flagl)) out << "Both";
		else if ((!flagr)&&(!flagl)) out << "Neither";
		else if ((flagr)&&(!flagl)) out << "Red";
		else if ((!flagr)&&(flagl)) out << "Blue";
		out << endl;
	}



	return 0;
}
//---------------------------------------------------------------------------
