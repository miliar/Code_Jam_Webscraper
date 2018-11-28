#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <deque>
#include <cstring>
#include <ctime>
#include <complex>

using namespace std;

#define MSG(a) cout << #a << " = " << a << endl;
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define PB push_back

vector<int> dest[10000];
vector<int> src[10000];
bool matchedD[10000];
bool matchedS[10000];

int main()
{
// 	ifstream fin("C-sample.in");
// 	ofstream fout("C-sample.out");
// 	ifstream fin("C-small-attempt1.in");
// 	ofstream fout("C-small-attempt1.out");
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	int T;
	fin >> T;
	for(int trz = 0; trz < T; trz++)
	{
		fout << "Case #" << trz+1 << ": ";
		int N,M;
		fin >> N >> M;
		
		char G[100][100];
		FOR(p,0,N)
		FOR(q,0,M)
			fin >> G[p][q];
			
		int NODES = N*M;	
		FOR(i,0,NODES)
			src[i].clear(), dest[i].clear();		
			
		memset(matchedD,0,sizeof matchedD);
		memset(matchedS,0,sizeof matchedS);
		
		FOR(i,0,N)
		FOR(j,0,M)
		{
			int ind = i*M+j;
			if(G[i][j] == '|')
			{
				int d1 = ((i+1)%N)*M+j;
				int d2 = ((i+N-1)%N)*M+j;
				dest[ind].PB(d1), dest[ind].PB(d2);
				src[d1].PB(ind), src[d2].PB(ind);
			}
			else if(G[i][j] == '-')
			{
				int d1 = i*M+(j+1)%M;
				int d2 = i*M+(j+M-1)%M;
				dest[ind].PB(d1), dest[ind].PB(d2);
				src[d1].PB(ind), src[d2].PB(ind);
			}
			else if(G[i][j] == '/')
			{
				int d1 = ((i+1)%N)*M+(j+M-1)%M;
				int d2 = ((i+N-1)%N)*M+(j+1)%M;
				dest[ind].PB(d1), dest[ind].PB(d2);
				src[d1].PB(ind), src[d2].PB(ind);
			}
			else if(G[i][j] == '\\')
			{
				int d1 = ((i+N-1)%N)*M+(j+M-1)%M;
				int d2 = ((i+1)%N)*M+(j+1)%M;
				dest[ind].PB(d1), dest[ind].PB(d2);
				src[d1].PB(ind), src[d2].PB(ind);
			}
		}
		
		int BAD = 0;
		
		FOR(p,0,NODES)
		if(src[p].size() == 0)
		{
			BAD = 1;
			break;
		}
		if(BAD)
		{
			fout << 0 << endl;
			cout << 0 << endl;
			continue;
		}			
		
		while(1)
		{
			int changed = 0;
			FOR(p,0,NODES)
			if(matchedS[p] == 0 && src[p].size() == 1)
			{
				int corrD = src[p][0];
				matchedS[p] = 1;
				matchedD[corrD] = 1;
				src[p].clear();
				
				if(dest[corrD].size() != 2) MSG("ERROR");
				
				int k1 = dest[corrD][0];
				int k2 = dest[corrD][1];
				if(k1 == p) k1 = k2;
				
				dest[corrD].clear();
				
				FOR(x,0,src[k1].size())
				if(src[k1][x] == corrD)
				{
					src[k1].erase(src[k1].begin() + x);
					break;
				}
				changed = 1;
			}
			if(changed == 0) break;
			
			FOR(p,0,NODES)
			if(src[p].size() == 0 && matchedS[p] == 0)
			{
				BAD = 1;
				break;
			}
			if(BAD) break;
		}
		
		if(BAD)
		{
			fout << 0 << endl;
			cout << 0 << endl;
			continue;
		}
		
		FOR(p,0,NODES)
		if(matchedS[p] == 0 && src[p].size() != 2)
		{
			MSG("ERROR");
			return 0;
		}
				
		FOR(p,0,NODES)
		if(matchedD[p] == 0)
		{
			cout << p << ": ";
			FOR(k,0,dest[p].size())
				cout << dest[p][k] << " ";
			cout << endl;
		}
		
		int cnter = 0;
		
		FOR(p,0,NODES)
		if(matchedD[p] == 0)
		{
			cnter++;
			
			int currD = p;
			int currS = dest[p][0];
			
			while(matchedD[currD] == 0)
			{
				matchedD[currD] = 1;
				matchedS[currS] = 1;
				FOR(x,0,src[currS].size())
				if(src[currS][x] != currD)
				{
					currD = src[currS][x];
					break;
				}
				FOR(x,0,dest[currD].size())
				if(dest[currD][x] != currS)
				{
					currS = dest[currD][x];
					break;
				}
			}
		}
		
		long long ans = 1;
		FOR(p,0,cnter)
			ans *= 2, ans %= 1000003;
		fout << ans << endl;
		cout << ans << endl;
			








	}
	return 0;
}






