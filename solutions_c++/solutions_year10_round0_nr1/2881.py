#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<map>
//#include<conio.h>

using namespace std;


#define MAX(A,B) (((A)>(B))?(A):(B))
#define MIN(A,B) (((A)<(B))?(A):(B))
//#define SZ 10000

//#define MAXINT ~((~0)<<31)




int main()
{
	freopen("A-large.in","r+",stdin);
	freopen("A.out","w+",stdout);
	
	int T,N,K,cse=1;

	cin >> T;
	while(T--)
	{
		cin >> N >> K;

		if(!((K+1)%(1 << N)))
			cout << "Case #" << cse++ << ": " << "ON" << endl;
		else cout << "Case #" << cse++ << ": " << "OFF" << endl;
	}
	


	
	return 0;
}

