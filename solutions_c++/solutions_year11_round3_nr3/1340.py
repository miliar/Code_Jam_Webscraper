//#include <iostream>
//#include <fstream>
//#include <map>
//#include <set>
//#include <string>
//using namespace std;
//
//void main(void)
//{
//	
//	ifstream fin("A-large.in");
//	ofstream fout("output.txt");
//	int T, tempT;
//	//cout << "HH";
//	fin >> T;
//	tempT = T;
//	while(T--)
//	{
//		int R, C, numBlue = 0, i, j;
//		char mat[50][50];
//		fin >> R >> C;
//
//		for(i = 0; i < R; ++i)
//		{
//			for(j = 0; j < C; ++j)
//			{
//				fin >> mat[i][j];
//				if( mat[i][j] == '#' )
//					++numBlue;
//			}
//		}
//		//cout << "HH";
//		if(numBlue % 4 != 0 )
//		{
//			fout <<"Case #"<<tempT - T<<":"<<endl<<"Impossible"<<endl;
//			continue;
//		}
//		for(i = 0; i < R; ++i)
//		{
//			for(j = 0; j < C;)
//			{
//				if(mat[i][j] == '#')
//				{//cout <<"AA";
//					if(j == C - 1 || mat[i][j+1] != '#' || i == R - 1 || mat[i+1][j] != '#' || mat[i+1][j+1] != '#')
//						goto IM;
//					mat[i][j] = '/';
//					mat[i][j+1] = '\\';
//					mat[i+1][j] = '\\';
//					mat[i+1][j+1] = '/';
//					j += 2;
//					continue;
//				}
//				++j;
//			}
//		}
//
//		fout <<"Case #"<<tempT - T<<":"<<endl;
//		for(i = 0; i < R; ++i)
//		{
//			for(j = 0; j < C; ++j)
//			{
//				fout << mat[i][j];
//			}
//			fout << endl;
//		}
//		continue;
//IM:	fout <<"Case #"<<tempT - T<<":"<<endl<<"Impossible"<<endl;
//			continue;
//	}//end while(T--)
//}
	//int T, C, D, N, tempT;
	//fin >> T;
	//tempT = T;
	//while(T--)
	//{
	//	map<string,char> mapC;
	//	map<string,char>::iterator mapIt;
	//	char chC[4]={}, chKey[3]={};
	//	fin >> C;
	//	while(C--)
	//	{
	//		fin >> chC;
	//		chKey[0] = chC[0];
	//		chKey[1] = chC[1];
	//		mapC[chKey] = chC[2];
	//		chKey[1] = chC[0];
	//		chKey[0] = chC[1];
	//		mapC[chKey] = chC[2];
	//	}
	//	
	//	set<string> setD;
	//	set<string>::iterator setIt;
	//	char chD[3]={};
	//	fin >> D;
	//	while(D--)
	//	{
	//		fin >> chD;
	//		chKey[0] = chD[0];
	//		chKey[1] = chD[1];
	//		setD.insert(chKey);
	//		chKey[0] = chD[1];
	//		chKey[1] = chD[0];
	//		setD.insert(chKey);
	//	}

	//	char chN[101], chResult[101]={};
	//	fin >> N >> chN;
	//	int index = 0;
	//	for(int i = 0; i < N; ++i)
	//	{
	//		chResult[index] = chN[i];
	//		if(index == 0) 
	//		{
	//			++index;
	//			continue;
	//		}
	//		//check whether could be conbined
	//		chKey[0] = chResult[index - 1];
	//		chKey[1] = chResult[index];
	//		if( (mapIt = mapC.find(chKey)) != mapC.end() )
	//		{
	//			chResult[index - 1] = mapIt->second;
	//			continue;
	//		}
	//		//check whether could be clear
	//		for(int j = 0; j < index; ++j)
	//		{
	//			chKey[0] = chResult[j];
	//			if( (setIt = setD.find(chKey)) != setD.end() )
	//			{
	//				index = 0;
	//				break;
	//			}
	//		}
	//		if(0 != index)//have not been clear
	//			++index;
	//	}
	//	fout <<"Case #" << tempT - T <<": [";
	//	for(int i = 0; i < index; ++i)//chResult[index] = '\0';
	//	{
	//		fout << chResult[i];
	//		if(i != index - 1)
	//			fout <<", ";
	//	}
	//	fout << "]" << endl;
	//}//end while(T--)

#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

int main()
{
	ifstream fin("C-small-attempt1.in");
	ofstream fout("output.txt");
	int T, tempT;
	fin>>T;
	tempT = T;

	while(T--)
	{
		int N, sound[10000];
		long long L, H, i, j;
		bool flag = true;
		fin >> N >> L >> H;

		for(i = 0; i < N; ++i)
			fin >> sound[i];
		for(i = L; i <= H; ++i)
		{
			flag = true;
			for( j = 0; j < N; ++j)
				if( i % sound[j] != 0 && sound[j] % i != 0 )
				{
					flag = false;
					break;
				}
			if(flag == true)
			{
				fout << "Case #" <<tempT - T << ": " << i << endl;
				break;
			}
		}
		if(flag == false)
			fout << "Case #" <<tempT - T << ": NO"  << endl;
	}
}
