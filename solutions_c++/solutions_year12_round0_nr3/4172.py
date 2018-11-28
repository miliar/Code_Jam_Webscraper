#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>
#include <queue>
#include <set>

using namespace std;

#define show(s) cout << #s << "-->" << s << endl;
#define show1(x,y,z) cout << #x << " , " << y << " , "<< z<< "-->" << x << endl;


int rotate(int input, int num_r){
	int output;
	int lenght = (int)log10(input);
	output = (input%((int)pow(10,num_r)))*((int)pow(10, lenght-num_r+1))+(input/((int)pow(10,num_r)));
	return output;
}

int main()
{
    int n;
    scanf("%d", &n);
    int a,b;
    for (int i = 0; i < n; i++)
    {
    	scanf("%d%d", &a, &b);
    	int l = (int)log10(a);
    	int count = 0;
    	for(int j = 0 ; j < (b-a)+1 ; j++ ){
    		for(int k = 1 ;  k <= l ; k++){
    			if( a <= rotate(a+j, k) && rotate(a+j, k) <= b && rotate(a+j,k)>(a+j) ){
    				//cout << a+j << "-->" << rotate(a+j, k) << endl;
    				count++;
    				/*if (rotate(a+j, k) == rotate(a+j, k-1))
    				{
    					cout << "salam" << endl;
    				}*/
    			}
    		}
    	}
    	cout<<  "Case #" << i+1 << ": " << count << endl;
    }
    return 0;
}