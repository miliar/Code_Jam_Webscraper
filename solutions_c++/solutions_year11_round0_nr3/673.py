#include <iostream>
#include <vector>
#include <map>
#include <string>

#define MIN_INIT 10000000

using namespace std;

int main(){
	int i=0 , n, candy_num,y,sum,buf,exor,min;
	cin >> n;
	while(++i<=n){
		cin >> candy_num;
		sum = 0;
		exor = 0;
		min = MIN_INIT;
		while(--candy_num>=0){
			cin >> buf;
			exor = exor^buf;
			if(buf < min){
				if(min != MIN_INIT){
					sum += min;
				}
				min = buf;
			}else{
				sum += buf;
			}
		}
		cout << "Case #" << i << ": ";
		if(exor!=0){
			cout << "NO";
		}else{
			cout << sum;
		}
		cout << endl;
	}
	return 0;
}