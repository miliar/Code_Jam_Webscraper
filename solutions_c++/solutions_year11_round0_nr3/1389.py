#include<iostream>
#include<cstdlib>
#define N 1005
using namespace std;

int cmp(const void *a,const void *b)
{
	return *(int *)a-*(int *)b;
}

int main()
{
	int tcase;
	int n;
	int sum;
	int walk = 0;
	int i;
	int arr[N];
	FILE *in,*out;
	in = freopen("C-large.in","r",stdin);
	out = freopen("C-large.txt","w",stdout);
	cin >>tcase;
	while(tcase--){
		cin >>n;
		for(i = 0;i < n;i++){
		    cin >>arr[i];
		}
		qsort(arr,n,sizeof(arr[0]),cmp);
		sum = arr[1];
		for(i = 2;i < n;i++){
			sum += arr[i];
			arr[i] ^= arr[i-1];
		}
		if(arr[0] != arr[n-1])
			cout << "Case #" << ++walk <<": "<<"NO" <<endl;
		else
			cout << "Case #" << ++walk <<": "<<sum <<endl;
	}
	fclose(in);
	fclose(out);
	return 0;
}