#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int nCases, iCases;
	cin >> nCases;
	
	for (iCases=1; iCases<=nCases; iCases++){
		int n, l, h;
		scanf("%d %d %d", &n, &l, &h);
		
		int arr[n];
		
		int i, j, f=-1;
		for (i=0; i<n; i++)
			scanf("%d", arr+i);
			
		for (i=l; i<=h; i++){
			for (j=0; j<n; j++){
				if (arr[j]%i!=0 and i%arr[j]!=0)
					break;
			}
			
			if (j==n){
				f=i;
				break;
			}
		}
		
		printf("Case #%d: ", iCases);
		if (f==-1)
			printf("NO\n");
		else
			printf("%d\n", f);
	}
	
	return 0;
}
