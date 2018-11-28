#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <string>
#include <cmath>
#include <iostream>
#include <stack>
#include <queue>
#include <ctime>
#include <utility>
#include <bitset>
#include <memory.h>
#include <list>
#include <deque>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int z = 0; z < T; z++)
	{
		vector<string> first;
		vector<string> second;
		int C;
		scanf("%d",&C);
		for(int i = 0; i < C; i++){
			string temp;
			cin >> temp;
			first.push_back(temp);
		}
		int D;
		scanf("%d",&D);
		for(int i = 0; i < D; i++){
			string temp;
			cin >> temp;
			second.push_back(temp);
		}

		string res;
		string cur;
		int size;
		cin >> size >> cur;
		for(int i = 0; i < cur.size(); i++){
			res.push_back(cur[i]);
			bool flag = false;
			if(res.size()==1)
				continue;
			else{
				for(int j = 0; j < C; j++)
					if((res[res.size()-1]==first[j][0] && res[res.size()-2]==first[j][1])||
						(res[res.size()-2]==first[j][0] && res[res.size()-1]==first[j][1]))
					{
						res.erase(res.begin() + res.size()-1);
						res.erase(res.begin() + res.size()-1);
						res.push_back(first[j][2]);
						flag = true;
						break;
					}
				if(!flag){
					flag = false;
					for(int k = 0; k < res.size()-1; k++){
						for(int j = 0; j < D; j++)
							if((res[res.size()-1]==second[j][0] && res[k]==second[j][1])||
								(res[k]==second[j][0] && res[res.size()-1]==second[j][1]))
							{
								res.clear();
								flag = true;
								break;
							}
						if(flag)
							break;
					}
				}
			}
		}
		printf("Case #%d: [",z+1);
		for(int i = 0; i < max((int)res.size()-1,0); i++)
			printf("%c, ",res[i]);
		if(res.size()!=0)
			printf("%c]\n",res[res.size()-1]);
		else
			printf("]\n");
	}
	return 0;
}