#include <iostream>
#include <fstream>

using namespace std;

const int maxl = 200;
const int maxn = 105;

char eng[maxn][maxl];
int best[maxn];
char query[maxl];

ifstream fin("a.in");
ofstream fout("a.out");

#define cin fin
#define cout fout

int main()
{
	int n, num = 0, s, q, min, i, j;
	cin >> n;
	while (num ++ < n)
	{
		cin >> s;
		for (i = 0;i < s;i ++) {
			while(cin.getline(eng[i], maxl), eng[i][0] == '\0');
		}
		cin >> q;
		memset(best, 0, sizeof(best));
		while (q -- > 0) {
			while (cin.getline(query, maxl), query[0] =='\0');
			int i;
			for (i = 0;i < s;i ++)
				if (strcmp(eng[i], query) == 0 )
					break;
			for (j = 0;j < s;j ++) {
				if (i != j) 
					if (best[j] > best[i] + 1)
						best[j] = best[i] + 1;
				//	cout << best[j] << " ";
				//} else 
				//	cout << q + 1 << " " ;

			}
			
			best[i] = 2000;				
		}

		min = best[0];
		for (i = 1;i < s;i ++)
			if (min > best[i])
				min = best[i];
		cout << "Case #" << num << ": "	<< min << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}