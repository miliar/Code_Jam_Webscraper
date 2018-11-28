#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <ctime>
//#include <fstream>
using namespace std;

#define INF 1000000000
#define PI acos(-1.0)



int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	cin>>tt;
	for (int t=1; t<=tt; t++){
		int n;
		cin>>n;
		int sum=0,mm=INF;
		int xor=0;
		for (int i=0; i<n; i++){
			int x;
			cin>>x;
			sum+=x;
			xor^=x;
			mm=min(mm,x);
		}

		cout<<"Case #"<<t<<": ";

		if (xor!=0){
			cout<<"NO"<<endl;
		}
		else cout<<sum-mm<<endl;
	}
	

}