#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	ifstream infile("sampleA.in");
	streambuf* inStream_buf(cin.rdbuf());
	cin.rdbuf(infile.rdbuf());
	ofstream outfile("sampleA.out");
	streambuf* outStream_buf(cout.rdbuf());
	cout.rdbuf(outfile.rdbuf());
	int i,row,column,n,resultO,resultX,finish;
	char map;
	cin >> n;
	for (i = 0;i < n;++i)
	{
		resultO = 0;
		resultX = 0;
		finish = 1;
		for (row = 0;row < 4;++row)
		{
			for (column = 0;column < 4;++column)
			{
				cin >> map;
				if (map == '.') finish = 0;
				if ((map == 'O')||(map == 'T')) resultO += (1 << (row * 4 + column));
				if ((map == 'X')||(map == 'T')) resultX += (1 << (row * 4 + column));
			}
		}
		resultO = ((resultO & 0x000F) == 0x000F) || ((resultO & 0x00F0) == 0x00F0) || ((resultO & 0x0F00) == 0x0F00) || ((resultO & 0xF000) == 0xF000) || ((resultO & 0x1111) == 0x1111) || ((resultO & 0x2222) == 0x2222) || ((resultO & 0x4444) == 0x4444) || ((resultO & 0x8888) == 0x8888) || ((resultO & 0x8421) == 0x8421) || ((resultO & 0x1248) == 0x1248);
		resultX = ((resultX & 0x000F) == 0x000F) || ((resultX & 0x00F0) == 0x00F0) || ((resultX & 0x0F00) == 0x0F00) || ((resultX & 0xF000) == 0xF000) || ((resultX & 0x1111) == 0x1111) || ((resultX & 0x2222) == 0x2222) || ((resultX & 0x4444) == 0x4444) || ((resultX & 0x8888) == 0x8888) || ((resultX & 0x8421) == 0x8421) || ((resultX & 0x1248) == 0x1248);
		if ((resultO == 1) && (resultX == 0)) cout << "Case #" << i+1 << ": O won" << endl;
		if ((resultO == 0) && (resultX == 1)) cout << "Case #" << i+1 << ": X won" << endl;
		if ((resultO == 0) && (resultX == 0)) 
		{
			if (finish) cout << "Case #" << i+1 << ": Draw" << endl;
			else cout << "Case #" << i+1 << ": Game has not completed" << endl;
		}
	}
	cin.rdbuf(inStream_buf);
	cout.rdbuf(outStream_buf);
	return 0;
}
