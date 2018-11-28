#include<iostream>
#include<cstdlib>
#define N 1005

using namespace std;

int arr[N];
int arr1[N];
int count;

int cmp(const void *a,const void *b)
{
	return *(int*)a-*(int*)b;
}

int main()
{
	int tcase;
	int n;
	int walk = 0;
	int i;
	FILE *in,*out;
	in = freopen("D-large.in","r",stdin);
	out = freopen("d-large.txt","w",stdout);
	cin >>tcase;
	while(tcase--){
		cin >>n;
		count = 0;
		for(i = 0;i < n;i++){
		   cin >>arr[i];
		   arr1[i] = arr[i];
		}
		qsort(arr1,n,sizeof(arr1[0]),cmp);
		for(i = 0;i < n;i++){
			if(arr[i] != arr1[i])
				count++;
		}
		printf("Case #%d: %d.000000\n",++walk,count);
	}
	fclose(in);
	fclose(out);
	return 0;
}