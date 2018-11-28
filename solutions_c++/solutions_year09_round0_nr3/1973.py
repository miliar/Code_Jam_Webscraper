#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int num;
	cin >> num;
	string boo;
	getline(cin, boo);
	string base = "welcome to code jam";
	int c = 0;
	while (num-- > 0)
	{
		c++;
		string foo;
		getline(cin, foo);
		unsigned int mat[foo.size()+1][base.size()+1];
		for(int i = 0; i <= foo.size(); i++)
		{
			for(int j = 0; j <= base.size(); j++)
			{
				mat[i][j] = 0;
			}
		}
		
		mat[0][0] = 1;
		
		for(int i = 0; i < foo.size(); i++)
		{
			for(int j = 0; j < base.size(); j++)
			{
				if (foo[i] == base[j])
				{
					mat[i+1][j+1] += mat[i][j];
				}
				mat[i+1][j] += mat[i][j];
			}
		}
		
		for(int i = 0; i < foo.size(); i++)
		{
			for(int j = 0; j < base.size(); j++)
			{
				//cout << mat[i][j] << " ";
			}
//			cout << endl;
		}		
		
		
		unsigned int ct = 0;
		for(int i = 0; i <= foo.size(); i++)
		{
			ct += mat[i][base.size()];
		}
		
	//	cout << foo << " " << ct << endl;
		printf("Case #%d: %04d\n", c, ct % 10000);
	}
}