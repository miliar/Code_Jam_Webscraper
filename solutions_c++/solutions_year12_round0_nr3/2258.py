#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <fstream>
#include <cmath>
#include <sstream>
using namespace std;

ofstream fout("D:\\jam.out");
	


int recycle(int A, int B)
{
	int T = 10;
	while(A/T > 0)
		T *= 10;

	bool b4 = false;// 4 or 6 digit nos
	bool b6 = false;
	if(T == 10000) b4 = true;
	else if(T == 1000000) b6 = true;
	
	vector<int> vt;
	int cnt = 0;
	bool bSuspect = false;
	int lastSuspect = -1;

	if(b4)
		lastSuspect = 1212;
	else if(b6)
		lastSuspect = 101101;

	for(int i=A; i<=B; ++i)
	{
		if(b4)
		{
			if( ((lastSuspect-i) % 101) == 0)//true if a no. can be broken into two equal halves
			{
				lastSuspect = i;
				bSuspect = true;
			}
			else 
				bSuspect = false;
		}else if(b6){
			if( ((lastSuspect-i) % 1001) == 0)
			{
				lastSuspect = i;
				bSuspect = true;
			}
			else if(i%100 == ((i/100)%100) && i%100 == i/10000) ////true if a no. can be broken into two equal halves or nos. of type 121212, 131313, 141414
				bSuspect = true;
			else
				bSuspect = false;
		}

		int f = 10;
		while(f < T)
		{
			int n = i/f + (i % f) * (T / f);
			if(n > i && n <= B) //all nos smaller than i have already been checked.
			{
				if(bSuspect)
				{
					if(find(vt.begin(), vt.end(), n) == vt.end())
					{
						vt.push_back(n);
						++cnt; //(i,n) is a valid pair.
					}
					/*else{
						fout << "DAMN " << i << " " << n << "\n";
					}*/
				}else{
					++cnt;;
				}
			}
			f *= 10;
		}

		if(bSuspect)
			vt.clear();
	}
	return cnt;
}


void find3()
{
	ifstream fin("D:\\jam.in");

	int T;
	
	//string s;
	//getline(fin, s);
	//T = atoi(s.c_str());
	fin >> T;

	int ncase = 1;

	//T = 50;

	while(T-- > 0)
	{
		//getline(fin, s);
		int A, B;
		fin >> A >> B;
		/*A = 100000;
		B = 999999;*/
		fout << "Case #"<< ncase++ << ": " << recycle(A, B) << endl;
	}
}

int main()
{
	//3 1 5 15 13 11
 //3 0 8 23 22 21
 //2 1 1 8 0
 //6 2 8 29 20 8 18 18 21

	find3();