#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v;

void printBin(int i){
	if(i==0){
	    return;
	}else{
        printBin(i>>1);
		cout << i%2;
	}
}

int pAdd(int a, int b){
	return a+b-2*(a&b);
}

int add(int n, int arr[]){
	int i=0;
	while(n!=0){
		if(n%2==1){
			arr[i] = (arr[i]+1)%2;
		}
		n >>= 1;
		i++;
	}
}

bool check(int a[], int b[]){
	for(int i=0; i<20; i++){
		if(a[i]!=b[i])
		    return false;
	}
	return true;
}

void print(int arr[]){
	for(int i=0; i<20; i++){
		cout << arr[19-i];
	}
	cout << endl;
}

bool compare(int a, int b){
	return a<b;
}

int search(int m,int a[], int b[]){
	return 0;
}

int main(){
	int n, m, temp;
	cin >> n;

	for(int i=0; i<n; i++){
	    cin >> m;
	    v.clear();
	    for(int j=0; j<m; j++){
			cin >> temp;
			v.push_back(temp);
		}
		sort(v.begin(),v.end(),compare);

        int a[20]={};
		int b[20]={};
		add(v[0],a);
		add(v[0],b);
		for(int k=0; k<m; k++){
			add(v[k],b);
		}
		if(check(a,b)){
			int sum = 0;
			for(int j=1; j<m; j++){
				sum += v[j];
   			}
			cout << "Case #" << i+1 << ": " << sum << endl;
		}else{
			cout << "Case #" << i+1 << ": " << "NO" << endl;
		}
	}
	system("pause");
}
