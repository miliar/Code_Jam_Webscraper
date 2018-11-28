#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include <cmath>
#include <cassert>
#include "iostream"
#include "sstream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()

const int INF = 1000000000;

typedef pair<vi, bool> s_s;

int n, m, c;



int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);


	int test_count;
	cin >> test_count;


	for (int test = 0; test < test_count ; test++)
	{
		fprintf(stderr, "%d\n", test);

	
		string term;
		cin >> term;
		int k;
		cin >> k;
		cin >> n;
		vvi words;
		for (int i = 0; i < n ; i++)
		{
			string s;
			cin >> s;
			vi w(26);
			for (int j = 0; j < s.length() ; j++)
			{
				w[s[j] - 'a']++;
			}

			words.push_back(w);
		}

		vi ans(k);

		
		for (int c = 1; c <= k; ++c)
		{

			int mmax = 1;
			for (int i = 0; i < c ; i++)
			{
				mmax *= n;
			}
vi bb(c);
		for (int ma = 0; ma < mmax; ++ma)
		{

			

			for (int ma_ = ma, b = 0; b < c ; b++ )
			{

				int i = ma_ % n;

				bb[b] = i;

				ma_ /= n;
			}

			int res = 0;
			int cur_val = 1;
			
			for (int i = 0; i < term.length() ; i++)
			{
				if (term[i] == '+')
				{
					res += cur_val;
					cur_val = 1;
				} else
				{
					int by = term[i] - 'a';
					int sum_ = 0;

					for (int b = 0; b < c; ++b)

						sum_ += words[bb[b]][by];

						
					

					cur_val *= sum_;
				}
			}

			res += cur_val;

			ans[c - 1] = (ans[c - 1] + res) % 10009;
		}

		}
	//	printf("Case #%d: %d\n", test + 1, best == INF ? -1 : best);


		
		printf("Case #%d: ", test + 1);
		for (int i = 0; i < k ; i++)
		{
			printf("%d ", ans[i]);
		}
		puts("");
		/*if (res == INF)
		printf("THE CAKE IS A LIE\n");
		else
		printf("%d\n", res);
		*/



	}

}
