// g_1.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <tchar.h>

#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <iostream>
#include <assert.h>
#include <algorithm>
#include <sstream>
#include <string>


/*
MSVS 2008

The program must be run with:
first argument = text file with input data
second argument = file name to write output data
*/
int _tmain(int argc, _TCHAR* argv[])
{
	////////////////////////////////////
	const TCHAR * cfin = NULL;
	const TCHAR * cfout = NULL;

	if(argc < 3)
	{
		cfin = _T("test.txt");
		cfout = _T("test2.out");
	}
	else
	{
		cfin = argv[1];
		cfout = argv[2];
	}

	std::fstream f;
	f.open(cfin);

	std::fstream f2;
	f2.open(cfout, std::fstream::out);

	int tasks;
	f >> tasks;

	int opptbl[64];
	int i2i[256];
	memset(i2i, 0, 256 * sizeof(int));
	i2i['Q'] = 0;
	i2i['W'] = 1;
	i2i['E'] = 2;
	i2i['R'] = 3;
	i2i['A'] = 4;
	i2i['S'] = 5;
	i2i['D'] = 6;
	i2i['F'] = 7;

	for(int t = 0; t < tasks; t++)
	{
		memset(opptbl, 0, 64 * sizeof(int));

		typedef std::pair<char, char> CMB;
		std::map<CMB, char> combines;

		int cn;
		f >> cn;

		if(cn > 0)
		{
			for(int i = 0; i < cn; i++)
			{
				std::string s;
				f >> s;
				combines[CMB(s[0], s[1])] = s[2];
				combines[CMB(s[1], s[0])] = s[2];
			}
		}
		
		int co;
		f >> co;

		if(co > 0)
		{
			for(int i = 0; i < co; i++)
			{
				std::string s;
				f >> s;
				opptbl[i2i[s[0]] * 8 + i2i[s[1]]] = 1;
				opptbl[i2i[s[1]] * 8 + i2i[s[0]]] = 1;
			}
		}

		int sl;
		f >> sl;
		std::string invoke;
		f >> invoke;

		char * out = new char[sl+1];
		int outlen = 0;
		for(int i = 0; i < sl; i++)
		{
			char c = invoke[i];
			if(0 == outlen)
			{
				out[0] = c;
				outlen ++;
			}
			else
			{
				bool ok = false;

				std::map<CMB, char>::const_iterator ci = combines.find(CMB(c, out[outlen - 1]));
				if(ci != combines.end())
				{
					out[outlen - 1] = ci->second;
					ok = true;
				}
				else
				{
					int * opprow = opptbl + i2i[c] * 8;
					bool found = false;
					for(int h = 0; h < outlen; h++)
					{
						switch(out[h])
						{
						case 'Q':
							found = opprow[0];
							break;
						case 'W':
							found = opprow[1];
							break;
						case 'E':
							found = opprow[2];
							break;
						case 'R':
							found = opprow[3];
							break;
						case 'A':
							found = opprow[4];
							break;
						case 'S':
							found = opprow[5];
							break;
						case 'D':
							found = opprow[6];
							break;
						case 'F':
							found = opprow[7];
							break;
						default:
							break;
						}

						if(found)
						{
							ok = true;
							outlen = 0;
							break;
						}
					}
				}

				if(!ok)
				{
					out[outlen] = c;
					outlen ++;
				}
			}
		}

		f2 << "Case #" << (t+1) << ": [";
		for(int r = 0; r < outlen; r++)
		{
			if(r > 0)
				f2 << ", ";
			f2 << out[r];
		}
		f2 << "]" << std::endl;
		delete[] out;
	}

	return 0;
}

