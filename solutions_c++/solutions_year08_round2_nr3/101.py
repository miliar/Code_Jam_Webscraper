#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

const double EPS = 1e-10;
const double PI = 3.14159265358979323846264338328;

#define PB push_back
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define INF INT_MAX
#define MSG(a) cout << #a << " = " << a << endl;
#define SORT(a) sort(a.begin(),a.end())


int main()
{
   ofstream fout;
   fout.open("outputCsmall.txt");
   ifstream fin("C-small-attempt0.in");
    
   int T;
   fin >> T;
   
   FOR(k,1,T+1)
   {
		int K;
		fin >> K;
		
		int array[5005];
		FOR(t,0,5005)
			array[t] = -1;
		
		int pos = 1;
		int curr = 0;
		while(curr < K)
		{
//			fout << curr << endl;

			int cnt = 0;
			while(cnt < curr)
			{
				if(array[pos] == -1) cnt++;
				
				pos++;
				
				if(pos == K+1) pos = 1;
			}
			
			while(array[pos] != -1)
			{
				pos++;
				if(pos == K+1) pos = 1;
			}
			array[pos] = curr+1;
			cnt = 0;
			curr++;
			pos++;
			if(pos == K+1) pos = 1;
//			FOR(t,1,K+1)
//			fout << array[t] << " ";
//		fout << endl;
		}
		
		fout << "Case #" << k << ":";
		
		int tests;
		fin >> tests;
		FOR(t,0,tests)
		{
			int tmp;
			fin >> tmp;
			fout << " " << array[tmp];
		}
		fout << endl;
		

      
   }
   
   return 0; 
    
    
    
    
    
    
}

