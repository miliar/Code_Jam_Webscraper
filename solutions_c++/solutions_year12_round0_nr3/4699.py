#include <sstream>
#include <cstdlib>
#include <iostream>
using namespace std;
int main()
{

	int t;
	cin >> t;
	int c = 1;
	while(c <= t)
	{
	
		string a , b ;
		int res = 0;
		cin >> a >> b;
		for(int i = atoi(a.c_str());i <= atoi(b.c_str());i++)
		{
			stringstream ss1;
			ss1 << i;
			string t = ss1.str();
			for(int j = 1;j < t.length();j++)
			{
				string a1 = t.substr(t.length()-j , j);
				string a2 = t.substr(0 , t.length()-j);
			/*	for(int k = 1;k < t.length();k++)
				{
					a1 += t[k];
					for(int x = 0;x < k;x++)
						a1 += t[x];			
				}*/	
					stringstream ss2;
					ss2 << a1 << a2;
					string str = ss2.str();
					if(str != t && str[0] != '0' && atoi(str.c_str()) >= atoi(a.c_str()) && atoi(str.c_str()) <= atoi(b.c_str()))
					{
						res++;
					//	cout << str << " ";
					}
				
			}
		}
		cout <<"Case #" << c << ": " << res/2 << endl;
		c++;
	}

}
