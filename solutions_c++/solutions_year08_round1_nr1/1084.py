#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <queue>
#include <vector>

int a[900];
int b[900];


bool less( int da1,int da2 ){
	return da1 < da2;
}

bool bigger( int da1,int da2 ){
	return da1 > da2;
}

int main(int argc, char * argv[])
{
//	freopen( "input","r",stdin );
	int n;
	int ca;
	std::cin>>ca;
	for( int i = 0; i < ca; i++ ){
		std::cin>>n;
		for( int h = 0; h < n; h++ ){
			std::cin>>a[h];
		}
		for( int h = 0; h < n; h++ ){
			std::cin>>b[h];
		}
		std::sort( a,a+n,less );
		std::sort( b,b+n,bigger );
		int res,h;
		for( h = 0, res = 0; h < n; h++ ){
			res += a[h]*b[h];
		}
		std::cout<<"Case #"<<i+1<<": "<<res<<std::endl;
	}
    return 0;
}
