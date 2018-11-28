#include "iostream"
#include <string>
#include <fstream>
#include <cmath>


using namespace std;


bool is_reflective(int m, int n)
{
	int len = ceil(log(m*1.0)/log(10.0));
	int l2 = ceil(log(n*1.0)/log(10.0));
	int nt = n;
	if(m == n || (len != l2)) return false;
	for(int i = 1; i < len; i++)
	{
		int tenth = pow(10.0, i);
		nt = (n % tenth) * pow(10.0, len - i) + (n / tenth);
		if(nt == m) return true;
	}
	return false;
}

void repNum()
{
	int T;
	cin >> T;
	int A, B;
	//ofstream out;
	//out.open("E://refl.out");
	
	for(int i = 0; i < T; i++)
	{
		cin >> A >> B;
		int n, m;
		int count = 0;
		for(n = A; n < B; n++)
		{
			for(m = n + 1; m <= B; m++)
			{
				if(is_reflective(m, n))
					count++;
			}
		}
		cout <<"Case #" << i + 1 << ": " << count << endl;
		//out <<"Case #" << i + 1 << ": " << count << endl;
	}
	out.close();
}

int main()
{

	repNum();
	return 0;
}


	string* G = new string[T];
	cout << "";
	
	int len;

	getline(cin, G[0]);
	for(int i = 0; i < T; i++)
	{
		getline(cin, G[i]);
	}

	for(int i = 0; i < T; i++)
	{
		len = strlen(G[i].c_str());
		for(int j = 0; j < len; j++)
		{
			if(G[i][j] != ' ')
			G[i][j] =  MAP[G[i][j] - 'a'] + 'a';
		}
		cout <<"Case #" << i + 1 << ": " << G[i] << endl;
	}
	//delete G;
	return 0;
}

