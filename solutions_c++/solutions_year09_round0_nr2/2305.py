#include <iostream>
#include <map>
#include <set>
#include <string>
#include <fstream>
#include <list>
#include <stack>
#include <vector>
using namespace std;

#define SIZE 10000

int numOfMaps = 0;
int height = 0;
int width = 0;
vector <char> alpha;
int count = 0;


int findLowest(vector <vector <int> > &matrix, int i, int j, vector<int> &pVec)
{
	int N = -1;
	int W = -1;
	int E = -1;
	int S = -1;
	int curr = -1;
	vector <int> iVec;
	if (i-1 >=0)
	{
		N = matrix[i-1][j];
	}
	iVec.push_back(N);
	if (j-1 >= 0)
	{
		W = matrix[i][j-1];
	}
	iVec.push_back(W);
	if (j+1 < width)
	{
		E = matrix[i][j+1];
	}
	iVec.push_back(E);
	if (i+1 < height)
	{
		S = matrix[i+1][j];
	}
	iVec.push_back(S);
	int lowest = 10000;
	int lowVal = -1;
	for (int i = 0; i < 4; i++)
	{
		if (iVec[i] >=0 && iVec[i] < lowest)
		{
			lowest = iVec[i];
			lowVal = i;
		}
	}
	if (matrix[i][j] <= lowest)
	{
		pVec.push_back(i);
		pVec.push_back(j);
		return matrix[i][j];
	}
	
	switch(lowVal)
	{
	case 0:
		pVec.push_back(i-1);
		pVec.push_back(j);
		break;
	case 1:
		pVec.push_back(i);
		pVec.push_back(j-1);
		break;
	case 2:
		pVec.push_back(i);
		pVec.push_back(j+1);
		break;
	case 3:
		pVec.push_back(i+1);
		pVec.push_back(j);
		break;
	}

	return iVec[lowVal];	
}

char calculate(vector <vector <int> > &matrix, int i, int j, vector<vector<char> >& cVec)
{
	int val = -1;
	int lh = -1;
	int lw = -1;
	int low = 10000;
	static char c = 0;
	if (cVec[i][j] != 0)
	{
		return cVec[i][j];
	}

	vector <int> iVec;

	/*for (int h  = i-1; h < i+2 && h < height; h++)
	{
		for (int w = j-1; w < j+2 && w < width; w++)
		{
			if (h >= 0 && w >= 0)
			{
				if (h != i && w != j)
				{
					continue;
				}
				val = matrix[h][w];
				iVec.push_back(val);
				if (val < low)
				{
					low = val;
					lh = h;
					lw = w;
				}
			}
		}
	}*/

	val = findLowest(matrix, i, j, iVec);
	lh = iVec[0];
	lw = iVec[1];
	if (lh == i && lw == j)
	{
		if (cVec[i][j] == 0)
		{
			c = alpha[count];
			cVec[i][j] = c;
			count++;
		}
		else
		{
			c = cVec[i][j];
		}
		return c;
	}

	char s = calculate(matrix, lh, lw, cVec);
	cVec[i][j] = s;
	return s;
}



int main(int argc, char **argv)
{
	for (char c = 'a'; c <= 'z'; c++)
		alpha.push_back(c);

	ifstream ifstr("Input.txt");
	ofstream ofstr("Output.txt");
	char buffer[SIZE];
	memset(buffer, 0, SIZE);
	ifstr.getline(buffer, SIZE, '\n');
	numOfMaps = atoi(buffer);

	for (int i = 0; i < numOfMaps; i++)
	{
		memset(buffer, 0, SIZE);
		ifstr.getline(buffer, SIZE, '\n');
		string temp(buffer);
		height = atoi(temp.substr(0, temp.find_first_of(" ")).c_str());
		temp.erase(0, temp.find_first_of(" ")+1);
		width = atoi(temp.c_str());
		vector <vector<int> > matrix;
		for (int j = 0; j < height; j++)
		{
			memset(buffer, 0, SIZE);
			ifstr.getline(buffer, SIZE, '\n');
			string temp1(buffer);
			vector<int> iVec;
			for (int k = 0; k < width; k++)
			{
				int val = atoi(temp1.substr(0, temp1.find_first_of(" ")).c_str());
				iVec.push_back(val);
				temp1.erase(0, temp1.find_first_of(" ")+1);
			}
			matrix.push_back(iVec);
		}
		
		vector <vector<char> > cVec;
		for (int p = 0; p < height; p++)
		{
			vector <char> cVec1;
			for (int q = 0; q < width; q++)
			{
				cVec1.push_back(0);
			}
			cVec.push_back(cVec1);
		}
		for (int h = 0; h < height; h++)
		{
			for (int w = 0; w < width; w++)
			{
				if (cVec[h][w] != 0)
					continue;
				calculate(matrix, h, w, cVec);
			}
		}

		
		ofstr << "Case #" << i+1 << ":" << endl;
		for (int h = 0; h < height; h++)
		{
			for (int w = 0; w < width; w++)
			{
				cout << cVec[h][w];
				cout << " ";
				ofstr << cVec[h][w];
				ofstr << " ";
			}
			cout << endl;
			ofstr << endl;
		}
		
		cout << endl;
		//ofstr << endl;
		count = 0;
	}
}



