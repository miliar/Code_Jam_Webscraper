#include <cstdio>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

using namespace std;

vector<string> google;

int N;



char buf[10000];
int mas[104][1005];

void gen()
{
	string s;
	for (int i=0; i<100; i++)
		s.push_back('0');
	printf("%d\n", 20);
	for (int t=0; t<20; t++)
	{
		printf("%d\n", 100);
		for (int i=0; i<100; i++)
		{
			printf("%s\n", s.c_str());
		}
		printf("%d\n", 1000);
		for (int i=0; i<1000; i++)
			printf("%s\n", s.c_str());
	}
}


int main()
{
	freopen("a.txt", "w", stdout);
	freopen("test.txt", "r", stdin);
	//gen();
	//return 0;
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		cerr<<t<<endl;
		google.clear();
		for (int i=0; i<104; i++)
		{
			mas[i][0] = 0;
			for (int j=1; j<1005; j++)
			{
				mas[i][j] = 1000000000;
			}
		}
		scanf("%d", &N);
		cin.getline(buf,102);
		for (int i=0; i<N; i++)
		{
			cin.getline(buf,102);
			string s(buf);
			google.push_back(s);
		}
		int Q;
		scanf("%d", &Q);
		cin.getline(buf,102);
		for (int q=1; q<=Q; q++)
		{
			cin.getline(buf,102);
			string s(buf);
			int index = -1;
			for (int i=0; i<N; i++)
			{
				if (s == google[i])
				{
					index = i;
					break;
				}
			}
			for (int i=0; i<N; i++)
			{
				int curmin = 1000000000;
				if (i == index)
				{
					mas[i][q] = 1000000000;
				}
				else
				{
					for (int j=0; j<N; j++)
					{
						if (i == j)
						{
							curmin = min(curmin,mas[i][q-1]);
							continue;
						}
						curmin = min(curmin, mas[j][q-1]+1);
					}
					mas[i][q] = curmin;
				}
			}
		}
		int res = 1000000000;
		for (int i=0; i<N; i++)
		{
			res = min(res,mas[i][Q]);
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}