#include <iostream>
using namespace std;


int main(int argc, char *argv[])
{
    int n, xorsum, sum, min, times, number, index = 0;
    cin >> n;
    while(index++ < n){
	xorsum = sum = 0;
	min = 1000000;
	cin >> times;
	while(times-- > 0){
	    cin >> number;
	    xorsum ^= number;
	    sum += number;
	    if(min > number){
		min = number;
	    }
	}
	if(xorsum != 0){
	    cout << "Case #" << index << ": NO" << endl;
	}else{
	    cout << "Case #" << index << ": " << sum - min << endl;
	}
    }
    return 0;
}
