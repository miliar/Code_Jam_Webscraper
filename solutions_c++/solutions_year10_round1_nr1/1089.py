// scalarProduct.cpp : Defines the entry point for the console application.
//

#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <assert.h>
#include <sstream>
#include <iomanip>
#include <iterator>

using namespace std;
class CTestCase
{
public:
	CTestCase()
	{
		m_num = 0;
	}
	void SetNum(int num)
	{
		m_num = num;
	}
	virtual void Input(istream &is)=0;
	void  PrintOutput( ostream &os)
	{
		PrintHeader(os);
		PrintResult(os);
	}
	virtual void ProcessTest()=0;
protected:
	virtual void PrintHeader( ostream &os)
	{
		os << "Case #" << m_num << ": ";
	}
	virtual void PrintResult( ostream &os)=0;
private:
	int m_num;
};


char inputbuffer[50][50];
bool findbuffer[50][50];

class CMyTest : public CTestCase
{
public:
	virtual void Input(istream &is)
	{

		for (int i=0; i<50; i++)
		{
			for (int j=0; j<50; j++)
			{
				inputbuffer[i][j] = 0;
			}
		}
		is >> N >> K;
		for (int i=0;i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				is >> inputbuffer[j][N-i-1];
				findbuffer[i][j] = false;
			}
		}
	}
	virtual void ProcessTest()
	{
		int startX, int endX;

		for (int j=0; j<N; j++)
		{
			startX = N;
			endX = 0;
			while(1)
			{
				startX = -1;
				for (int i=N-1; i>=0; i--)
				{
					if (inputbuffer[i][j] == '.')
					{
						startX = i;
						break;
					}
				}
				if (startX==-1)
				{
					break;
				}
				endX = -1;
				for (int i=startX-1; i>=0; i--)
				{
					if (inputbuffer[i][j] != '.')
					{
						endX = i;
						break;
					}
				}
				if (endX == -1)
				{
					break;
				}
				int len = startX - endX;
				for (int i=endX; i>=0; i--)
				{
					inputbuffer[i+len][j] = inputbuffer[i][j];
				}
				for (int i=0; i<len; i++)
				{
					inputbuffer[i][j] = '.';
				}
			}

		}
		bool redWin = false;
		bool blueWin = false;

		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				findbuffer[i][j] = false;
			}
		}
		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				if (inputbuffer[i][j] != '.' )
				{
					if(IsRow(i,j))
					{
						if (inputbuffer[i][j] == 'R')
						{
							redWin = true;
						}
						else
						{
							blueWin = true;
						}
					}
				}
			}
		}

		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				findbuffer[i][j] = false;
			}
		}
		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				if (inputbuffer[i][j] != '.' )
				{
					if(IsCol(i,j))
					{
						if (inputbuffer[i][j] == 'R')
						{
							redWin = true;
						}
						else
						{
							blueWin = true;
						}
					}
				}
			}
		}

		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				findbuffer[i][j] = false;
			}
		}
		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				if (inputbuffer[i][j] != '.' )
				{
					if(IsDiag(i,j))
					{
						if (inputbuffer[i][j] == 'R')
						{
							redWin = true;
						}
						else
						{
							blueWin = true;
						}
					}
				}
			}
		}

		for (int i=0; i<N; i++)
		{
			for (int j=0; j<N; j++)
			{
				if (inputbuffer[i][j] != '.' )
				{
					if(IsDiag1(i,j))
					{
						if (inputbuffer[i][j] == 'R')
						{
							redWin = true;
						}
						else
						{
							blueWin = true;
						}
					}
				}
			}
		}
		if (redWin)
		{
			if (blueWin)
			{
				m_res = "Both";
			}
			else
			{
				m_res = "Red";
			}
		}
		else
		{
			if (blueWin)
			{
				m_res = "Blue";
			}
			else
			{
				m_res = "Neither";
			}
		}
	}
protected:
	virtual void PrintResult( ostream &os)
	{
		
		os << m_res;
	}
	bool IsRow(int i, int j)
	{
		int k=1;
		int left = i-1;
		while (left>=0)
		{
			if (inputbuffer[i][j]==inputbuffer[left][j])
			{
				k++;
				findbuffer[left-1][j] = true;
			}
			else
			{
				break;
			}
			left--;
		}
		int right = i+1;
		while (right<N)
		{
			if (inputbuffer[i][j]==inputbuffer[right][j])
			{
				k++;
				findbuffer[right][j] = true;
			}			
			else
			{
				break;
			}
			right++;
		}
		if (k>=K)
		{
			return true;
		}
		return false;
	}
	bool IsCol(int i, int j)
	{
		int k=1;
		int down = j-1;
		while (down>=0)
		{
			if (inputbuffer[i][j]==inputbuffer[i][down])
			{
				k++;
				findbuffer[i][down] = true;
			}
			else
			{
				break;
			}
			down--;
		}
		int up = j+1;
		while (up<N)
		{
			if (inputbuffer[i][j]==inputbuffer[i][up])
			{
				k++;
				findbuffer[i][up] = true;
			}			
			else
			{
				break;
			}
			up++;
		}
		if (k>=K)
		{
			return true;
		}
		return false;
	}
	bool IsDiag(int i, int j)
	{
		int k=1;
		int left = i-1;
		int down = j-1;
		while (left>=0 && down>=0)
		{
			if (inputbuffer[i][j]==inputbuffer[left][down])
			{
				k++;
				findbuffer[left][down] = true;
			}
			else
			{
				break;
			}
			left--;down--;
		}
		int up =j+1;int right = i+1;
		while (up<N && right<N)
		{
			if (inputbuffer[i][j]==inputbuffer[right][up])
			{
				k++;
				findbuffer[right][up] = true;
			}			
			else
			{
				break;
			}
			up++; right++;
		}
		if (k>=K)
		{
			return true;
		}
		return false;
	}

	bool IsDiag1(int i, int j)
	{
		int k=1;
		int left = i-1;
		int down = j+1;
		while (left>=0 && down<N)
		{
			if (inputbuffer[i][j]==inputbuffer[left][down])
			{
				k++;
				findbuffer[left][down] = true;
			}
			else
			{
				break;
			}
			left--;down++;
		}
		int up =j-1;int right = i+1;
		while (up>=0 && right<N)
		{
			if (inputbuffer[i][j]==inputbuffer[right][up])
			{
				k++;
				findbuffer[right][up] = true;
			}			
			else
			{
				break;
			}
			up--; right++;
		}
		if (k>=K)
		{
			return true;
		}
		return false;
	}
private:
	int N;
	int K;
	string m_res;
};

int main(int argc, char* argv[])
{
	ifstream inFile("a.dat");
	ofstream outFile("o.dat");

	int N;
	inFile >> N;
	for (int i=0; i<N; i++)
	{
		CMyTest test;
		test.SetNum(i+1);
		test.Input(inFile);
		test.ProcessTest();
		test.PrintOutput(outFile);
		outFile << std::endl;
	}
	return 0;
}
