#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		int n, s, p;
		cin >> n >> s >> p;
		int *arr = new int [n];
		for (int i=0;i<n;i++)
			cin >> arr[i];
		sort(arr, arr+n);
		int count = 0;
		for (int i=n-1;i>=0;i--){
			if (arr[i]%3==2 && arr[i]/3+1>=p)
				count++;
			else if (arr[i]%3==1 && arr[i]/3+1>=p)
				count++;
			else if (arr[i]%3==0 && arr[i]/3>=p)
				count++;
			else if (arr[i]%3==0  && arr[i]>=3 && arr[i]/3+1>=p && s>0){
				count++;
				s--;
			}
			else if (arr[i]%3==2 && arr[i]>=4 && arr[i]/3+2>=p && s>0){
				count++;
				s--;
			}
		}
		delete arr;
		cout << count << endl;
	}
	return 0;
}
