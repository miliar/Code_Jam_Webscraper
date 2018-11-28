#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iterator>
#include<cstring>
#include<string>
#include<cassert>
#define for_a(i,n,a)  for(int i =a;i<n;i++)
#define for_n(i,n)  for(int i =0;i<n;i++)


using namespace std;


#define SZ(x) (int)(x).size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))

int nodigits(int n){
	int count = 0;
	while(n != 0){
		count++;
		n /= 10;
	}
	return count;
}

int rotateL(int x, int pow){	
	int usb = x/pow;
	int y = (x%pow)*10 + usb;	
	return y;
}


int main(){
	ifstream fin;
	fin.open("inp3");
	ofstream fout;
	fout.open("out3");
	int T;
	fin >> T;
	int S;
	int L;
	int dig,dig1,itemp,count;		
	for(int t = 0;t<T;t++){
		fin >> S >> L;
		count = 0;
		for(int i = S; i< L; i++){
			for(int j=i+1;j<L+1;j++){
				//cout << i << " "<<j<<"\n";
				dig = nodigits(i);
				//cout<<i<<" "<<dig<<endl;
				dig1 = nodigits(j);
				if(dig == dig1){
					itemp = i;
					int pow = 1;
					for(int m=0;m<dig-1;m++){
						pow*=10;
					}
					for(int k =0;k<dig-1;k++){
												
						if(j == rotateL(itemp,pow)){
							 count++;
					//		 cout <<"i "<<i<<" j "<<j<<endl;
							 break;							 
						}
						itemp = rotateL(itemp,pow);
					}
				}
			}
		}
		fout <<"Case #"<<t+1<<": "<<count<<"\n";
	}
	return 0;
}
						
				
		
