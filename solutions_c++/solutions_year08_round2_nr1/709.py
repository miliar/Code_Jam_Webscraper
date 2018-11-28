#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <functional>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cstdio>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

struct Data
{
	bool operator < (const Data& data)
	{
		return true;
	}
};

static int c[51][51];

static inline int get_c(int i, int j)
{
	if(i > j || i < 0 || j < 0)return 0;
	if(i == 0) return 1;
	if(c[i][j] != -1)return c[i][j];
	int &val = c[i][j];
	val = get_c(i-1, j-1) + get_c(i, j-1);
	return val;
}


static inline void o_case(int i)
{
	fout << "Case #"<<i <<": ";
}


static void process_case(int num)
{
	////input here
    long long n, A, B, C, D, x0, y0, M;
	fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;	
	int m[3][3];
	memset(m, 0, sizeof(m));
		
	int xt = x0 ,yt = y0;


	m[x0%3][y0%3]++;
	for(int i = 1; i < n ; i++)
	{
		xt = (A * xt + B) % M;
		yt = (C * yt + D) % M;
		m[xt%3][yt%3]++;
	}

	/////process
	int count = 0;
	for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++)
		for(int k = 0; k < 3; k++) for(int l = 0; l < 3; l++)
			for(int s = 0; s < 3; s++) for(int t = 0; t < 3; t++)
				if((i + k + s)%3 == 0 && (j + l + t) %3 == 0)
				{
					//fout << i << j << k << l << s << t<<endl;
					//fout <<"val " << m[i][j]<<" " << m[k][l]<<" " << m[s][t]<<endl;
					int x = m[i][j] * m[k][l] * m[s][t];
					if(i == k && i == s&& j ==l && j == t){
						if(m[i][j] >= 3)
							count +=  m[i][j] * (m[i][j]-1)*(m[i][j]-2);
					}
					else 
						count += x;
				}

	//////////////
	o_case(num);
	///output here
	fout<<count/6 <<endl;
	
}

int main()
{
	int case_num;

	fin >> case_num;

	for(int i = 1; i <= case_num; i++)
	{
		process_case(i);
	}
}







