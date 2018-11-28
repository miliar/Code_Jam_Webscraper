// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

void solve()
{
	string hex = "0123456789ABCDEF";
	int hextbl[256] = {0};
	for (int i=0;i<hex.length();i++)
		hextbl[hex[i]] = i;
	int T;
	cin >> T;
	char *brd = new char[512*512];
	char *used = new char[512*512];
	for (int t=0;t<T;t++)
	{
		int M, N;
		cin >> M >> N;
		memset(brd, 0, 512*512);
		memset(used, 0, 512*512);
		for (int row=0;row<M;row++)
		{
			char ch;
			int k = 0;
			for (int col=0;col<N/4;col++)
			{
				cin >> ch;
				int v = hextbl[ch];
				for (int j=0;j<4;j++)
				{
					if (v&(1<<(3-j)))
					{
						brd[(row<<9)+k] = 1;
					}
					else
					{
						brd[(row<<9)+k] = 0;
					}
					k++;
				}
			}
		}
		map<int, int> mCnt;
		int MSZ = min(M,N);
		for (int sz=MSZ;sz>=1;sz--)
		{
			for (int y=0;y<=M-sz;y++)
				for (int x=0;x<=N-sz;x++)
					if (used[x+(y<<9)]==0)
					{
						char prevtobe;
						for (int yy=0;yy<sz;yy++)
						{
							char tobe = brd[x+((y+yy)<<9)];
							if (yy>0 && tobe==prevtobe) goto nope;
							prevtobe = tobe;
							for (int xx=0;xx<sz;xx++)
							{
								if (used[xx+x+((y+yy)<<9)]) goto nope;
								if (brd[xx+x+((y+yy)<<9)]!=tobe) goto nope;
								tobe = 1-tobe;
							}
						}
						mCnt[sz]++;
						for (int yy=0;yy<sz;yy++)
						{
							for (int xx=0;xx<sz;xx++)
							{
								used[xx+x+((y+yy)<<9)] = 1;
							}
						}
nope:;
					}
		}
		cout << "Case #" << (t+1) << ": " << mCnt.size() << endl;
		vector<int> asz, acnt;
		for (map<int,int>::iterator itr=mCnt.begin();itr!=mCnt.end();++itr)
		{
			asz.push_back(itr->first);
			acnt.push_back(itr->second);
		}
		for (int i=0;i<asz.size();i++)
		{
			cout << asz[asz.size()-1-i] << " " << acnt[acnt.size()-1-i] << endl;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

