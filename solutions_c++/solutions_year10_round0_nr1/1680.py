#include <vector>
#include <list>
#include <map>
#include <set>
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

#define sort(A) sort(A.begin(),A.end()) 
#define rei(i,A,B) for(int i=A;i<B;i++) 
#define red(i,A,B) for(int i=A;i>=B;i--)
#define ree(i,A,B) for(int i=A;i<=B;i++) 
#define pb(A,B) A.push_back(B)

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	rei(t,0,T){
		int N,K;
		cin>>N>>K;
		string ret="ON";
		rei(i,1,N+1){
			if( K/((int)pow(2.0,(i-1)*1.0))% 2==0)				
				ret="OFF";
		}
		cout<<"Case #"<<t+1<<": "<<ret<<endl;
	}
	return 0;
}



















