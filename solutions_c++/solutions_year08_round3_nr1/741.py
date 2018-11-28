#include <iostream>
using namespace std;

int compare_ints( const void* a, const void* b ) {
	int* arg1 = (int*) a;
	int* arg2 = (int*) b;
	if( *arg1 < *arg2 ) return 1;
	else if( *arg1 == *arg2 ) return 0;
	else return -1;
}
int main()
{
	int n;
	int p,k,l;
	int *f;
	int i,j,m;
	int sum;
	cin>>n;
	for(i=0;i<n;i++)
	{
		sum = 0;
		cin>>p;
		cin>>k;
		cin>>l;
		f = new int[l];
		for (j=0;j<l;j++)
			cin>>f[j];
		qsort( f, l, sizeof(int), compare_ints);
		for (j=0;j<l;j++)
		{
			m = j/k+1;
			sum += f[j]*m;
		}
		cout<<"Case #"<<i+1<<": "<<sum<<endl;

	}
	

}