#include <iostream>
#include <limits>
using namespace std;

//char * small_in = "A-small-practice.in";
//char * small_out = "A-small-practice.out";
char * small_att_in =  "C-small-attempt1.in";
char * small_att_out = "C-small-attempt1.out";
//char * large_in = "A-large.in";
//char * large_out = "A-large.out";

const int MAX_CANDIES = 1000;

int candy_set[MAX_CANDIES];
int subset_set[MAX_CANDIES];
int max_variant[MAX_CANDIES];
long int count_permutations = 0;


int PatrickSumm(int a, int b)
{
		int n_a = ~a;
		int n_b = ~b;
		int ans =  (n_a & b)|( n_b & a); // a*b_ + a_*b
		return ans;
}

int summ( const int * candy_set, const int * subset, int N )
{
	int sum1 = 0;

	for ( int i = 0; i < N; i++ )
	{
		sum1 += candy_set[i]*subset[i];
	}
	int sum2 = 0;

	for ( int i = 0; i < N; i++ )
	{
		sum2 += ( 1 - subset[i])*candy_set[i];
	}
	if ( sum1 > sum2 ) return sum1;
	else return sum2;
}

bool summ_eq( const int * candy_set, const int * subset, int N )
{
	int sum1 = 0;
	for ( int i = 0; i < N; i++ )
	{
		sum1 = PatrickSumm(sum1, candy_set[i]*subset[i]);
	}
	int sum2 = 0;
	for ( int i = 0; i < N; i++ )
	{
		sum2 = PatrickSumm( sum2, ( 1 - subset[i]) * candy_set[i]);
	}
	return ( sum1 == sum2 );
}

int perm ( int * subset, const int N, const int r, const int p, const int vMax)
{
	int myMax = vMax;

	if ( p == 0 )
	{
		////memcpy(set_permutations[count_permutations], subset_set, N);
		////count_permutations++;
		//for ( int i = 0; i < N; i++ )
		//{
		//	cout << subset[i] << " ";
		//}
		//cout << endl;
		if ( summ_eq( candy_set, subset, N ) )
		{
			int try_perm = summ( candy_set, subset, N );
			if ( try_perm > myMax )
			{
				myMax = try_perm;
			}
		}
		return myMax;
	}
	for ( int j = r; j < N - p + 1; j++ )
	{
		subset[j] = 1;
		myMax = perm( subset, N, j+1, p-1, myMax );
		subset[j] = 0;
	}
	return myMax;
}


int main()
{
	freopen(small_att_in, "rt", stdin);
	freopen(small_att_out, "w", stdout);

	int T;
	cin >> T;

	for ( int i = 0; i < T; i++ )
	{
		int N;
		cin >> N;

		if ( i + 1 == 34 )
		{
			int asd = 0;
			asd += 1;
		}


		for ( int j = 0; j < N; j++ )
		{
			cin >> candy_set[j];
		}
		
		int maxPerm = -1;

		for ( int i = 1; i < N; i++ )
		{
			maxPerm = perm ( subset_set, N, 0, i, maxPerm);
		}

		cout << "Case #" << i+1<<": ";
		if (maxPerm == -1) cout << "NO";
		else cout << maxPerm;
		cout << endl;
	}

	//int N = 5;

	//		for ( int i = 1; i < N; i++ )
	//	{
	//		perm ( subset_set, N, 0, i, -1);
	//	}

	//while (1)
	//{
	//	int a;
	//	int b;
	//	cin >> a;
	//	cin >> b;
	//	cout << a << " + " << b << " = " << PatrickSumm(a, b) << endl;
	//}

	return 0;
}