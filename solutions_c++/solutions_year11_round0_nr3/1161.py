#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int ci[1008];
bool splitting[1008];
int n;
int half;
bool getSplitting(int i,int sum){
	if(sum>half){
		return false;
	}
	int result1=0,result2=0;
	if(i<0){
		if(sum<=0)return false;
		for(int j=0;j<n;j++){
			if(splitting[j]){
				result1^=ci[j];
			}else{
				result2^=ci[j];
			}
		}
		if(result1==result2){
			return true;
		}
		return false;
	}
	if(getSplitting(i-1,sum)) return true;;
	splitting[i]=true;
	if(getSplitting(i-1,sum+ci[i])) return true;
	return false;
}

int main(){
	int t;
	int sum;
	int i,j,k;
	int result;
	ifstream cin("C-small-attempt1.in");
	ofstream cout("C-small-attempt1.out");
	cin >> t;
	for(i=1;i<=t;i++){
		result=0;
		sum=0;
		cin >> n;
		for(j=0;j<n;j++){
			cin >> ci[j];
			splitting[j]=false;
			sum+=ci[j];
		}
		sort(ci,ci+n);
		half=sum/2;
		cout << "Case #" << i <<": ";
		if(getSplitting(n,0)){
			for(j=0;j<n;j++){
				if(!splitting[j]){
					result+=ci[j];
				}
			}
			cout << result << endl;
		}else{
			cout << "NO" << endl;
		}
		
	}
}