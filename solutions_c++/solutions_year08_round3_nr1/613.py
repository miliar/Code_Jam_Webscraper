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

bool cmp( int a1,int a2 ){
	return a1>a2;
}

int a[1009];

int main(int argc, char * argv[])
{
//	freopen( "input","r",stdin );
	int n;
	std::cin>>n;
	for( int i = 0; i < n; i++ ){
		int p,k,l;
		std::cin>>p>>k>>l;
		for( int g = 0; g < l; g++ ){
			std::cin>>a[g];
		}
		std::sort( a,a+l,cmp );
		int keyTime,keyIndex,res;
		for( keyIndex = 0 , keyTime = 0 , res = 0; keyIndex < l; keyIndex++ ){
			if( keyIndex%k == 0 )
				keyTime ++;
			res += a[keyIndex]*keyTime;
		}
		std::cout<<"Case #"<<i+1<<": "<<res<<std::endl;
	}
    return 0;
}
