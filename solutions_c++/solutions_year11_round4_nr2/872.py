// round1-b.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include<vector>
#include<algorithm>
#include  <iomanip> 

using namespace std;

int T;
int R;
int C;
int D;

_int64 arr[600][600];

bool check( int ii, int jj, double len){
	double  sum_x = 0;
	double sum_y = 0;
	double sum = 0;
	for( int i = ii; i <= ii+len; i++ ){
		for( int j=jj; j<=jj+len; j++){
			sum_x += arr[i][j]*(i-ii);
			sum_y += arr[i][j]*(j-jj);
			sum += arr[i][j];
		}
	}

	sum_x += arr[ii+(int)len][jj]*(0-len) + arr[ii+(int)len][jj+(int)len]*(0-len);
	sum_y += (0-len)*(arr[ii][jj+(int)len]+arr[ii+(int)len][jj+(int)len]);
	sum -= (arr[ii][jj]+arr[ii][jj+(int)len]+arr[ii+(int)len][jj]+arr[ii+(int)len][jj+(int)len]);

	if( sum*len/2 == sum_x && sum_y == sum_x)
		return true;
	else
		return false;
}

int findmax( int i,int j, int max){
	//step 1:limit
	int limit = R-i;
	if( limit > C-j) limit = C-j;
	//step 2: min
	int min = 2;
	if(min < max) min = max;
	//step 3: check
	int r = 0;
	for(int k = limit-1; k >= min; k--){
		if( check(i,j,k) == true){
			r = k;
			break;
		}
	}
	return r;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\\B-small-attempt0 (3).in");
	ofstream out("D:\\B-small.out");
	
	//cout <<fixed <<setprecision(10) ;
	//out <<fixed <<setprecision(10) ;

	in >> T;
	int cur = 0;
	while(cur++ < T){
		int max = 0;
		in >> R;
		in >> C;
		in >> D;
		int i,j;

		//cout << R <<C<< D<<endl;

		for(i=0;i<R;i++){
			for(j=0;j<C;j++){
				char c;
				in >> c;
				arr[i][j] = c-'0';
			}
		}

		for(i=0;i<R;i++){
			for(j=0;j<C;j++){
				if( C - j < max )
					break;
				int temp = findmax(i,j,max);
				if(temp > max) max = temp;
			}
			if( R-i < max )
				break;
		}
		max ++;

		if(max >=3 )
			out <<"Case #"<<cur<<": "<<max<<endl;
		else
			out <<"Case #"<<cur<<": IMPOSSIBLE"<<endl;
	}

	in.close();
	out.close();
	return 0;
}


