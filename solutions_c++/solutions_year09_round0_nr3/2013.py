#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
//#include <cstdio>
//#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>


using namespace std;

typedef long long int64;

string str;
int icount[11];
int index[11][500];
long mx[19][501];
enum letters{w, e, l, c, o, m, t, d, j, a, space};

void indexing();
void dynamicPlot();


map<int, char> maps;



void main(){
	//freopen("D:\\Visual Studio 2008\\Projects\\googlejam2008\\Welcome to Code Jam\\input.txt", "rt", stdin);
	//freopen("D:\\Visual Studio 2008\\Projects\\googlejam2008\\Welcome to Code Jam\\output.txt", "wt", stdout);

	int N;
	long count;
	string strN, strCount;
	ifstream infile("D:\\Visual Studio 2008\\Projects\\googlejam2008\\Welcome to Code Jam\\input.txt");
	//ofstream ofile ("D:\\Visual Studio 2008\\Projects\\googlejam2008\\Welcome to Code Jam\\output.txt");


	getline(infile, strN);


	istringstream is(strN);
	is >> N;

	
	maps[0] = 'w'; 
	maps[1] = 'e'; 
	maps[2] = 'l'; 
	maps[3] = 'c'; 
	maps[4] = 'o'; 
	maps[5] = 'm'; 
	maps[6] = 'e'; 
	maps[7] = ' '; 
	maps[8] = 't'; 
	maps[9] = 'o'; 
	maps[10] = ' '; 
	maps[11] = 'c'; 
	maps[12] = 'o'; 
	maps[13] = 'd'; 
	maps[14] = 'e'; 
	maps[15] = ' '; 
	maps[16] = 'j'; 
	maps[17] = 'a'; 
	maps[18] = 'm'; 


	for(int i = 0; i < N; i ++)
	{
		getline(infile, str);

		//indexing();
		dynamicPlot();


/*		for(int j = 0; j < str.length(); j ++)
		{
			if(str[j] == 'w')
				count = count + mx[0][j];
		}*/

		ostringstream os;

		os <<  mx[0][0];
		strCount = os.str();
		string tmp;
		if(strCount.length() < 4)
		{
			for(int k = strCount.length() ; k < 4; k ++)
				tmp = tmp + "0";
			strCount = tmp + strCount;
		}
		else
		{
			strCount = strCount.substr(strCount.length() - 4, 4);
		}

		cout <<"Case #" << i + 1 << ": " << strCount << endl;

	}

	getchar();
	
}


void dynamicPlot()
{
	/*
	if(str[str.length() - 1] == 'm')
		mx[18][str.length - 1] = 1;
	else 
		mx[18][str.length - 1] = 0;
		*/

	mx[18][str.length()] = 0;
	for(int i = str.length() - 1; i >= 0; i --){
		if(str[i] == 'm')
			mx[18][i] = mx[18][i + 1] + 1;
		else
			mx[18][i] = mx[18][i + 1];
		//cout << mx[18][i] << endl;
	}


	for(int j = 17; j >= 0; j --)
	{
		mx[j][str.length()] = 0;
		for(int i = str.length() - 1; i >= 0; i --)
		{
			if(str[i] == maps[j])
			{
				mx[j][i] = mx[j + 1][i] + mx
					[j][i + 1];
			}
			else
				mx[j][i] = mx[j][i + 1];
		}
	}

}

void indexing()
{
	int k[11];
	for(int i = 0; i < 11; i ++)
	{
		k[i] = 0;
	}

	for(int i = 0; i < str.length(); i ++)
	{
		switch(str[i])
		{
		case 'w':
			index[w][k[w]] = i;
			k[w] ++;
			break;
		case 'e':
			index[e][k[e]] = i;
			k[e] ++;
			break;
		case 'l':
			index[l][k[l]] = i;
			k[l] ++;
			break;
					case 'c':
			index[c][k[c]] = i;
			k[c] ++;
			break;
					case 'o':
			index[o][k[o]] = i;
			k[o] ++;
			break;
					case 'm':
			index[m][k[m]] = i;
			k[m] ++;
			break;
					case 't':
			index[t][k[t]] = i;
			k[t] ++;
			break;
					case 'd':
			index[d][k[d]] = i;
			k[d] ++;
			break;
					case 'j':
			index[j][k[j]] = i;
			k[j] ++;
			break;
					case 'a':
			index[a][k[a]] = i;
			k[a] ++;
			break;
					case ' ':
			index[space][k[space]] = i;
			k[space] ++;
			break;	
		}

	}
}