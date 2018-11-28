#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <cmath>
#include <cstring>

using namespace std;

long long powll(int a, int b)
{
	if(b==0)
		return 1;
	
	long long res=a;
	for(int i=1;i<b;i++)
		res *= a;
	return res;
}

void input()
{	
	int T,i,j;
	cin >> T;
	
	char buf[100];
	cin.getline(buf, 100);
	for(int C=1; C<=T; C++)
	{
		cin.getline(buf, 100);
		buf[strlen(buf)]='\0';
		string str = buf;
		
		map<char,bool> check;
		for(i=0; i<str.size(); i++)
			check[str[i]] = true;
		
		int c=check.size();
		if(c==1)
			c++;
		
		map<char, int> table;		

		for(i='0'; i<='9'; i++)
			table[i] = -1;
		for(i='a'; i<='z'; i++)
			table[i] = -1;
		
		
		long long res=0;
		int num=0;
		int res_table[61];

		table[str[0]]=1;
		res_table[0]=1;

		int a=str.size();
		res += powll(c, str.size()-1) * res_table[0];
		
		for(i=1; i<str.size(); i++)
		{
			if(table[str[i]] == -1)
			{
				if(num==1)
					num++;
				table[str[i]] = num;
				res_table[i] = num;
				num++;
				
				
			}
			else
			{
				res_table[i] = table[str[i]];
			}
			int b=str.size()-(i+1);
			res += powll(c, str.size()-(i+1)) * res_table[i];
		}

		cout << "Case #" << C << ": " << res << endl;
	}
}

int main()
{
	input();
	return 0;
}