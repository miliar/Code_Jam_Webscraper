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


string knowed[101];
string needcreate[101];

class CMyTest : public CTestCase
{
public:
	CMyTest()
	{
		m_res = 0;
	}
	virtual void Input(istream &is)
	{

		is >> N >> M;
		for (int i=0; i<N; i++)
		{
			is >> knowed[i];
		}
		for (int i=0; i<M; i++)
		{
			is >> needcreate[i];
		}
	}
	virtual void ProcessTest()
	{
		m_res  = 0;

		for (int i=0; i<N; i++)
		{
			Parse(knowed[i]);
		}
		for (int j=0; j<M; j++)
		{
			CreatDir(needcreate[j]);
		}
	}
protected:
	bool Have(string path)
	{
		for (int i=0; i<m_buffer.size(); i++)
		{
			if (m_buffer[i] == path)
			{
				return true;
			}
		}
		return false;
	}
	void Parse(string path)
	{
		string::size_type startDir,endDir;
		startDir = path.find_last_of('/');
		string lastDir = path;
		while(startDir != string::npos)
		{

			string curpath = path.substr(startDir);
			if (!Have(lastDir))
			{
				m_buffer.push_back(lastDir);
			}
			lastDir = path.substr(0, startDir);
			startDir = lastDir.find_last_of('/');
		}
	}
	void CreatDir(string path)
	{
		string::size_type startDir;
		if (Have(path))
		{
			return;
		}
		m_res++;
		m_buffer.push_back(path);

		startDir = path.find_last_of('/');
		if (startDir != string::npos && startDir != 0)
		{

			string lastDir = path.substr(0, startDir);
			if (!Have(lastDir))
			{
				CreatDir(lastDir);

			}

		}
		else
		{
			return;
		}
	}
	virtual void PrintResult( ostream &os)
	{
		os << m_res;
	}

private:
	int N;
	int M;
	int m_res;
	vector<string> m_buffer;
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
