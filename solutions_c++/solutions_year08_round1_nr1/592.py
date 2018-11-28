#include <iostream>
using namespace std;
#define MAX 1000

void shellsort(long long int v[], long long int n)
{
   long long int gap, i, j, temp;
   for (gap = n/2; gap > 0; gap /= 2)
      for (i = gap; i < n; i++)
         for (j=i-gap; j>=0 && v[j]>v[j+gap]; j-=gap) 
         {
            temp = v[j];
            v[j] = v[j+gap];
            v[j+gap] = temp;
         }
   return;
}

int main()
{
	int i, j, k, casos, n;
	long long int suma, x[MAX], y[MAX];
	cin >> casos;
	for(i = 1; i <= casos; i++){
		cin >> n;
		for(j = 0; j < n; j++)
			cin >> x[j];
		shellsort(x, n);
		for(j = 0; j < n; j++)
			cin >> y[j];
		shellsort(y, n);
		suma = 0;
		for(j = 0, k = n-1; j < n; j++, k--)
			suma+=(x[j]*y[k]);
		cout << "Case #"<<i<<": "<<suma<<endl;
	}
	return 0;	
}
