#include <cstdio>
#include<iostream>  
#include<fstream>

#define TAG_X 0x10
#define TAG_O 0x20
#define TAG_XO (TAG_X | TAG_O)
#define TAG_P (0x80 | TAG_XO)
#define TAG_T 0x01


enum Result
{
	RET_X, RET_O, RET_DRAW, RET_LESS
};

int parse(char buf[4][4])
{
	bool hasPoint = false;
	for(int i=0; i<4; ++i)
	{
		int tagH = 0;
		int cntH = 0;
		int tagV = 0;
		int cntV = 0;
		for(int j=0; j<4; ++j)
		{
			tagH |= buf[i][j];
			cntH += (buf[i][j] & TAG_T);
			tagV |= buf[j][i];
			cntV += (buf[j][i] & TAG_T);
		}
		if(TAG_P == (tagH & TAG_P) || TAG_P == (tagV & TAG_P))
		{
			hasPoint = true;
		}
		tagH &= TAG_XO;
		if(cntH < 2)
		{
			if(TAG_X == tagH)
			{
				return RET_X;
			}
			else if(TAG_O == tagH)
			{
				return RET_O;
			}
		}
		tagV &= TAG_XO;
		if(cntV < 2)
		{
			if(TAG_X == tagV)
			{
				return RET_X;
			}
			else if(TAG_O == tagV)
			{
				return RET_O;
			}
		}
	}
	int tagL = 0;
	int cntL = 0;
	int tagR = 0;
	int cntR = 0;
	for(int i=0; i<4; ++i)
	{		
		tagL |= buf[i][i];
		cntL += (buf[i][i] & TAG_T);
		tagR |= buf[i][3-i];
		cntR += (buf[i][3-i] & TAG_T);
	}
	tagL &= TAG_XO;
	if(cntL < 2)
	{
		if(TAG_X == tagL)
		{
			return RET_X;
		}
		else if(TAG_O == tagL)
		{
			return RET_O;
		}
	}
	tagR &= TAG_XO;
	if(cntR < 2)
	{
		if(TAG_X == tagR)
		{
			return RET_X;
		}
		else if(TAG_O == tagR)
		{
			return RET_O;
		}
	}
	return hasPoint ? RET_LESS : RET_DRAW;
}

int main(int argc, char *argv[])
{
	char table[256];
	memset(table, TAG_P, sizeof(table));
	table['X'] = TAG_X;
	table['O'] = TAG_O;
	table['T'] = TAG_T;

	std::ofstream os;
	os.open("A-large.out");

	std::ifstream is;
	is.open("A-large.in");
	if(!is)
	{
		std::cout << "Open file failed" << std::endl;
		return 1;
	}
	int N;
	is >> N;
	char buff[32];
	is.getline(buff, sizeof(buff));
	char data[4][4];
	for(int i=0; i<N; ++i)
	{
		memset(data, TAG_P, sizeof(data));
		for(int j=0; j<4; ++j)
		{
			is.getline(buff, sizeof(buff));
			for(int k=0; k<4; ++k)
			{
				data[j][k] = table[buff[k]];
			}
		}
		int ret = parse(data);
		os << "Case #" << i+1 << ": ";
		switch(ret)
		{
		case RET_X:
			os << "X won" << std::endl;
			break;
		case RET_O:
			os << "O won" << std::endl;
			break;
		case RET_LESS:
			os << "Game has not completed" << std::endl;
			break;
		case RET_DRAW:
			os << "Draw" << std::endl;
			break;
		default:
			os << "Error" << std::endl;
			break;
		}
		is.getline(buff, sizeof(buff));
	}
}
