#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int make_money(int r, int k , int n, vector<int>& vec)
{
		int vecIndex = -1;
		int money = 0;
		for(int i = 0; i < r; i++)
		{
				int current_holder = 0;
				while(true)
				{
						int next = vecIndex + 1;
						if(next %= n);
						if(vec[next] + current_holder <= k)
						{
								current_holder += vec[next];
								vecIndex = next;
						}
						else
						{
								break;
						}
				}
				money += current_holder;
		}
		return money;
}


int main(int argc, char**argv)
{
		ifstream in(argv[1]);
		ofstream out(argv[2]);
		if(!in)
		{
				cerr<<"can not open input file\n"<<endl;
				return 1;
		}
		int t,r, k, n;
		in>>t;
		int i = 1;
		char result[100];
		char enter = '\n';
		int temp;
		while(t-- > 0)
		{
				in>>r>>k>>n;
				vector<int> group_num;
				for(int j = 0; j < n ; j++)
				{
						in>>temp;
						group_num.push_back(temp);
				}
				int money = make_money(r, k, n, group_num);
				sprintf(result, "Case #%d: %d", i, money);
				out.write(result, strlen(result));
				i++;
				if(t != 0 )
						out.write(&enter, 1);
		}
		return 0;
}
