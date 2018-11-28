#include <iostream>
#include <cstdio>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <cstring>
using namespace std;
const int INFI = 1000000000;

int T;
int n,m;

//FILE *in, *out;


map<string,int> mp;

ifstream in("A-small.in");
ofstream out("A-small.out");
#define cout out
#define cin in


int main()
{
	//in = fopen("A-small.in","r");
    //in = fopen("A-large.in","r");
	//out = fopen("A-small.out","w");
	//out = fopen("A-large.out","w");
	//scanf("%d",&T);
	cin >> T;
	for(int cnt = 1;cnt <= T;cnt ++)
	{
		cout << "Case #"<<cnt<<": "; 
		mp.clear();
		mp["/"] = 1;
		//scanf("%d%d",&n,&m);
		cin >> n >> m;
		for(int i = 0;i < n;i ++)
		{
			string temp;
			cin >> temp;
			mp[temp] = 1;
		}
		int ans = 0;
		for(int i = 0;i < m;i ++)
		{
			string temp;
			cin >> temp;
			if(temp == "/")
				continue;
			int pos = 1;
			int cur;
			while((cur = temp.find("/",pos)) != string::npos)
			{
				string sub = temp.substr(0,cur);
				if(mp.count(sub) == 0)
				{
					ans ++;
					mp[sub] = 1;
				}
				pos = cur + 1;
			}
			if(mp.count(temp) == 0)
			{
				ans ++;
				mp[temp] = 1;
			}
		}
		cout << ans << endl;



	}

	
	return 0;
}