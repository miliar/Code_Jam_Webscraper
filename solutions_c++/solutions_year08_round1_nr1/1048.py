#include <iostream>


using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}


int descompare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}


int main(void)
{
	int t,i,n,j;
	long acc;
	int vetor_a[800];
	int vetor_b[800];

	cin >> t;

	for(i=0;i<t;i++)
	{
		cin >> n;
		for(j=0;j<n;j++)
			cin >> vetor_a[j];
		for(j=0;j<n;j++)
			cin >> vetor_b[j];

		qsort (vetor_a, n, sizeof(int), compare);
		qsort (vetor_b, n, sizeof(int), descompare);

		acc=0;
		for(j=0;j<n;j++)
			acc+= vetor_a[j]*vetor_b[j];

		cout << "Case #" << i+1 << ": " << acc << endl;
	}
	


return 0;

}
