#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))


int main()
{
	//freopen("myinput.txt", "r", stdin);
	//freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d\n", &T);
	vector <char> outS;
	rep(i, T)
	{
		outS.clear();
		char L[1000];
		gets(L); 
		
		char * pch;
		//printf("Length of string %d\n", strlen(L));
		pch = strtok (L, " ");
		
		int C = atoi(pch);
		//cout << C << " ";
		
		string * CO;
		if (C > 0) CO = new string[C];
		rep(j, C)
		{
			pch = strtok (NULL, " ");
			CO[j].assign(pch);
			//printf("%s ", CO[j].c_str());
		}
		//cout << endl;
		
		pch = strtok (NULL, " ");
		int D = atoi(pch);
		//cout << D << " ";
		
		string * DO;
		if (D > 0) DO = new string[D];
		rep(j, D)
		{
			pch = strtok (NULL, " ");
			DO[j].assign(pch);
			//printf("%s ", DO[j].c_str());
		}
		//cout << endl;
		
		pch = strtok (NULL, " ");
		int N = atoi(pch);
		//cout << N << " ";
		
		string NS;
		pch = strtok (NULL, " ");
		NS.assign(pch);
		//printf("%s\n", NS.c_str());
		//pch = strtok (NULL, " ");
		
		
		outS.push_back(NS[0]);
		for(int j = 1; j < N; ++j)
		{
			outS.push_back(NS[j]);

			//check for combine
			int lenO = SZ(outS);
			bool success = false;
			if (lenO > 1)
			{
				string tmp1 = "";
				tmp1.push_back(outS[lenO-1]);
				tmp1.push_back(outS[lenO-2]);
				
				string tmp2 = "";// + outS[lenO-2] + outS[lenO-1];
				tmp2.push_back(outS[lenO-2]);
				tmp2.push_back(outS[lenO-1]);

				for (int k = 0; k < C; ++k)
				{
					if (CO[k].find(tmp1) == 0 || CO[k].find(tmp2) == 0)
					{
						success = true;

						outS.erase(outS.end() - 1);
						outS.erase(outS.end() - 1);
						outS.push_back( (char) CO[k][2]);
						k = C; // exit condition
					}
				}
			}
			
			//check for destroy
			if (!success && lenO > 1)
			{
				for (int k = 0; k < D; ++k)
				{
					char ctmp1 = (char) DO[k][0];
					char ctmp2 = (char) DO[k][1];
					bool found1 = false;
					bool found2 = false;
					for (int m = 0; m < SZ(outS); ++m)
					{
						if (outS[m] == ctmp1)
							found1 = true;
						if (outS[m] == ctmp2)
							found2 = true;
					}
					if (found1 && found2)
					{
						outS.clear();
						k = D;
					}
				}

				
			}

			
		}
		//cout << ans << endl;
		//printf("Case #%d: %lld\n", i+1, c_time); // 
		int lsz = SZ(outS);
		if (lsz == 0) printf("Case #%d: []\n", i+1); // 
		else
		{
			printf("Case #%d: [", i + 1);
			rep(m, lsz)
			{
				if (m != 0) printf(", ");
				printf("%c", outS[m]);
			}
			printf("]\n");
		}

		//delete [] NS;
		if (C > 0) delete [] CO;
		if (D > 0) delete [] DO;
		
	}
	
	return 0;
}
