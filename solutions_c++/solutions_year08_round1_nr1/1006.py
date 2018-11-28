#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <sstream>
#include <utility>

#define PI acos(-1)
#define pb push_back
#define sz size()
#define all(v) (v).begin(),(v).end()
#define VER(x) cout << #x" = " << x << "\n"
#define INTMAX  2147483647

using namespace std;

int main (void){

    //freopen("A-small.in","r",stdin);
    //freopen("A-small.out","w",stdout);

	int N;
	
	cin>>N;
	
	for(int X=0; X<N; X++)
	{	
		int T;
		
		cin>>T;
		
		vector <int> A(T,0),B(T,0);
		
		 
		for(int i=0; i<T; i++)
			cin>>A[i];
		 
		for(int i=0; i<T; i++)
			cin>>B[i];
		
		//int res=INTMAX;
		
		sort(all(A));
		sort(all(B));
		reverse(all(B));
		
		
		int res=0;
		
		for(int i=0; i<T; i++)
		{
			res+=A[i]*B[i];
		}	
		
		
		
		cout<<"Case #"<<X+1<<": "<<res<<endl;
		//Case #X: Y
	}

    //system("pause");
    return 1;
}

