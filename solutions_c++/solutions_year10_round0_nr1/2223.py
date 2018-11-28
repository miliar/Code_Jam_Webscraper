#include <iostream>

using namespace std;

int main()
{
	int n, k, t;
	int i, result;

//	FILE *fin = freopen("a.txt", "r", stdin);
	//FILE *fout = fopen("a.out", "w");

	const char crst[2][5] = {"ON", "OFF" };
	unsigned int arr[31] = {0, 1, 3, };
	unsigned int tbl[31] = {0, 2, 4, };

	scanf("%d", &t);

	for( i = 2; i <=30; ++i )
	{
		arr[i] = arr[i-1]*2 +1;
		tbl[i] = tbl[i-1]*2;
	}


	for( i = 1; i <=t; ++i )
	{

		scanf("%d %d", &n, &k);

		if( k == 0 || k < arr[n] )
			result = 1;
		else if( ( k - arr[n] ) % tbl[n] != 0 )
			result = 1;
		else
			result = 0;

//		fprintf(fout, "Case #%d: %s\n", i, crst[result]); 
		printf( "Case #%d: %s\n", i, crst[result]); 
	}
//	fclose(fout);
	
	return 0;
}