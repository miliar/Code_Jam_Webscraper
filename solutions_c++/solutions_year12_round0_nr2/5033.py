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


int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("inp2");
	fout.open("out2");
	int T, N, S, P, Sd;
	vector<int> A;	
	fin >> T;
	for (int t=0; t<T;t++){
		int max = 0;
		fin>>N>>S>>P;
		Sd = S;
		A.resize(N);
		for(int i =0 ;i< N; i++){
			fin >> A[i];
			if(A[i]%3 == 0){
				if(A[i]/3 >= P){
					max++;
				}
				else if(A[i]/3!= 0 && A[i]/3 + 1 >= P){
					if(Sd > 0){
						max++;
						Sd--;
					}
				}
			}
			else if(A[i]%3 == 2){
				if(A[i]/3 + 1 >= P){
					max++;
				}
				else if(A[i]/3 + 2 >= P){
					if(Sd > 0){
						max++;
						Sd--;
					}
				}
			}
			else if(A[i]%3 == 1){
				if(A[i]/3 + 1 >= P){
					max++;
				}
			}
		}
		fout << "Case #"<<t+1<<": "<<max<<"\n";
	}
	return 0;
}
	
