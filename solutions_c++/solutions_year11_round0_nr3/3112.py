#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))

//int next_combination(int c[], int N, int R) // N is no. of items, R is no. of choices
//{
//    int i = 0;
//    while ( i <R-1 && c[i+1]==c[i]+1) // for each bump
//        c[i] = i++;                 // fall back
//    return N - ++c[i];              // push forward and verify
//}

//template<class RandIt, class Compare>
//bool next_combination(RandIt first, RandIt mid, RandIt last, Compare comp)
//{
//    std::sort(mid, last, std::tr1::bind(comp, std::tr1::placeholders::_2
//                                        , std::tr1::placeholders::_1));
//    return std::next_permutation(first, last, comp);
//}

template <typename Iterator>
   inline bool next_combination(const Iterator first, Iterator k, const Iterator last)
   {
      if ((first == last) || (first == k) || (last == k))
         return false;
      Iterator itr1 = first;
      Iterator itr2 = last;
      ++itr1;
      if (last == itr1)
         return false;
      itr1 = last;
      --itr1;
      itr1 = k;
      --itr2;
      while (first != itr1)
      {
         if (*--itr1 < *itr2)
         {
            Iterator j = k;
            while (!(*itr1 < *j)) ++j;
            std::iter_swap(itr1,j);
            ++itr1;
            ++j;
            itr2 = k;
            std::rotate(itr1,j,last);
            while (last != j)
            {
               ++j;
               ++itr2;
            }
            std::rotate(k,itr2,last);
            return true;
         }
      }
      std::rotate(first,k,last);
      return false;
   }


int main()
{
	//freopen("myinput.txt", "r", stdin);
	freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small.out", "w", stdout);

	//freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);

	int T;
	scanf_s("%d", &T);
	
	rep(i, T)
	{
		int N;
		scanf_s("%d", &N);
		
		int * C = new int[N];
		//ll sum = 0;
		rep(j, N)
		{
			scanf_s("%d", &(C[j]));
			//sum += C[j];
		}

		//vector<int> Cv(C,C+N);
		//sort(C, C+N, greater<int>()); 
		

		ll largest_split = 0;
		for(int j = N - 1; j >= N/2; --j)
		{
			// display all possible combinations
			do
			{
				ll split1 = 0;
				ll split2 = 0;
				
				int binsp1 = 0;
				int binsp2 = 0;

				for (int k=0; k<j; ++k)
				{
					split1 += C[k];
					binsp1 ^= C[k];
					//printf("%d ", C[k]);
				}
				for (int k=j; k<N; ++k)
				{
					split2 += C[k];
					binsp2 ^= C[k];
				}
				if (binsp1 == binsp2)
				{
					ll sp_max = (split1 > split2)? split1 : split2;
					if (sp_max > largest_split) largest_split = sp_max;
				}
				//printf("\n");
			}
			//while (next_permutation(C, C + N));
			while (next_combination(C, C + j, C + N));
		}
		//printf("\n");
		if (largest_split == 0)
			printf("Case #%d: NO\n", i+1); 
		else
			printf("Case #%d: %lld\n", i+1, largest_split); // 
		
		delete [] C;
	}
	
	return 0;
}
