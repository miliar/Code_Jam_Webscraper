#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <iostream>
#include <vector>
#include <deque>
#include <iterator>
#include <algorithm>
using namespace std;

int TT[26];  // Translation Table

int main(){
	int T;
	scanf("%d\n",&T);
	int A,B;
	int count=0;
	vector<int> used;	// 登録済み数

	for(int i=1; i<=T; i++){
		scanf("%d %d\n",&A,&B);
		printf("Case #%d: ",i);
		count = 0;

		for( int m=A; m<=B; m++ ){
			deque<int> digits;	// 各位の数字
			for( int k=0; k<log10(m); k++ )
				digits.push_back((m%(int)pow(10,k+1))/(int)pow(10,k));

			//printf("m:%d\n",m);
			for( int s=1; s<log10(m); s++ ){ // sはシフト量
				int n=0;	// リサイクルによって生成される数字
				for( int k=0; k<log10(m); k++ ){		
					n += digits[(k+s)%digits.size()]*pow(10,k);
				}
				vector<int>::iterator iter = find( used.begin(),used.end() , n );
				if( n <= B && m<n && iter == used.end()){
					used.push_back(n);
				//	printf("n:%d\n",n);
					count++;
				}
			}
			used.clear();
			//printf("\n");

			//for( int i=0; i<digits.size(); i++ )
			//	printf("%d ",digits[i]);			
			//digits.clear();
			//printf("\n");
		}
		printf("%d \n",count);
	}

	return 0;
}