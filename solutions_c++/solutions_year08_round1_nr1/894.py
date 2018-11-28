#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
    int i,j,n,k,m,a[801],b[801],l;
    int sum;
    int min;
    cin>>m;
    for(i=0;i<m;i++)
    {
        cin>>n;
        k = 1;
        min = 2000000000;
        for (j = 2;j <= n;j ++) {
        	k *= j;
        }
        for(j = 0;j < n;j ++) {
        	scanf("%d",a + j);
        }
        for(j = 0;j < n;j ++) {
        	scanf("%d",b + j);
        }
        for(j = 0;j < k;j ++) {
        	next_permutation(a,a+n);
        	sum = 0;
        	for (l = 0;l < n;l ++) {
        		sum += a[l] * b[l];
        	}
        	//cout << sum << endl;
        	if (sum < min) min = sum;
        }
 		cout << "Case #" << i + 1 << ": " << min << endl;
    }    
    //system("pause");
}