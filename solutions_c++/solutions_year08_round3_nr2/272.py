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

char dig[100];
int a[100];


int count;


void dfs( int index,int len,bool lastOP,int currSum,int currNum ){
	currNum = currNum%210;
	currSum = currSum%210;
	if( index == len ){
		currNum = currNum*10+a[index-1];
		if( lastOP == true ){
			currSum += currNum;
		}
		else{
			currSum -= currNum;
		}
		if( currSum < 0 )
			currSum = -currSum;
		if( currSum%2 == 0 ||
			currSum%3 == 0 ||
			currSum%5 == 0 ||
			currSum%7 == 0 ){
			count++;
		}
		return;
	}

	//什么都不加
	dfs( index+1,len,lastOP,currSum,currNum*10+a[index-1] );
	int number;
	number = currNum*10+a[index-1];
	if( lastOP == true )
		currSum += number;
	else{
		currSum -= number;
	}
	//+
	dfs( index+1,len,true,currSum,0 );
	//-
	dfs( index+1,len,false,currSum,0 );
}


int main(int argc, char * argv[])
{
//	freopen( "input","r",stdin );
	int n;
	std::cin>>n;
	for( int i = 0; i < n; i++ ){
		std::cin>>dig;
		int len = strlen( dig );
		for( int k = 0; k < len; k++ ){
			a[k] = dig[k]-'0';
		}
		count = 0;
		dfs( 1,len,true,0,0 );
		std::cout<<"Case #"<<i+1<<": "<<count<<std::endl;
	}
    return 0;
}
