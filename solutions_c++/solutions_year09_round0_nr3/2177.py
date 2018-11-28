#include <string>
#include <fstream>
using namespace std;

const int rows = 19;
const int length = 510;
char input[length];
char *pattern = "welcome to code jam";
long long result[22][510];

int count(int rows, int cols,const char* str )
{
	for( int i = 1; i < rows; i++ )
	{
		result[i][0] = 0;
	}
	for(int j = 0; j< cols;j++)
	{
		result[0][j] = 1;
	}
	for( int i = 1; i < rows; i++ )
	{
		for(int j = 1; j< cols;j++)
		{
			if(str[j-1] == pattern[i-1])
			{
				result[i][j] = (result[i-1][j-1] + result[i][j-1])%10000;
			}else
				result[i][j] = result[i][j-1];
		}
	}
	return result[rows-1][cols-1];
}

int output(const char* str)
{
	int len = strlen(str);
	return count(rows+1, len+1, str );
}

void getChar(long long input,int *resChar)
{
	int temp;
	for(int i = 3; i >= 0; i--)
	{
		temp = input % 10;
		if(temp < 0)
			temp *= -1;
		resChar[i] = temp;
		input /= 10;
	}
}

void main()
{
	ifstream inf("F:\\C-large.in");
	ofstream ouf("F:\\C-large.out");

	string str;
	long long res;
	if(inf)
	{
		getline(inf,str);
		int N = atoi(str.c_str());
		int i = 1;
		int resC[4];
		while(i <= N && getline(inf,str))
		{
			const char* cstr = str.c_str();
			res = output(cstr);
			getChar(res,resC);
			ouf<<"Case #"<<i<<": "<<resC[0]<<resC[1]<<resC[2]<<resC[3]<<endl;
			i ++;
		}
	}
}