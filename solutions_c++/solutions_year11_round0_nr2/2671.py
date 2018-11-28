#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int tNum=0; tNum<T; ++tNum)
	{
		int C, D, N;
		cin >> C;
		string cs[C];
		for(int i=0; i<C; ++i)
			cin >> cs[i];
		cin >> D;
		string ds[D];
		for(int i=0; i<D; ++i)
			cin >> ds[i];
		cin >> N;
		string text;
		cin >> text;
		char ans[1000];
		int r=0;
		for(int i=0; i<N; ++i)
		{
			ans[r++]=text[i];
			while(r>1){
				char c1=ans[r-2], c2=ans[r-1];
				bool ok=false;
				for(int j=0; j<C; ++j)
					if((cs[j][0]==c1 && cs[j][1]==c2)||(cs[j][0]==c2 && cs[j][1]==c1)){
						ok=true;
						ans[r-2]=cs[j][2];
						--r;
						break;
					}
				if(!ok) break;
			}
			for(int j=0; j<r-1; ++j)
			{
				char c1=ans[j], c2=ans[r-1];
				bool find=false;
				for(int d=0; d<D; ++d)
					if((ds[d][0]==c1 && ds[d][1]==c2) || (ds[d][0]==c2 && ds[d][1]==c1)){
						find=true;
						break;
					}
				if(find){
					r=0;
					break;
				}
			}
		}
		printf("Case #%d: [",tNum+1);
		for(int i=0; i<r; ++i)
		{
			printf("%c",ans[i]);
			if(i<r-1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
