#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <stdlib.h>
//#include <ctime>
//#include <fstream>
using namespace std;

#define INF 1000000000
#define PI acos(-1.0)
#define MP make_pair
#define EPS 1e-9

int gcd(int a,int b){
	if (b==0) return a;
	else return gcd(b,a%b);
}

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin>>t;
	for (int tt=1; tt<=t; tt++){
		long long n;
		int pd,pg;
		cin>>n>>pd>>pg;

		cout<<"Case #"<<tt<<": ";

		int a=pd,b=100,c=gcd(pd,100);
		a/=c;
		b/=c;
		if (b>n){
			cout<<"Broken"<<endl;
			continue;
		}

		if (pg==100 && pd==100) cout<<"Possible"<<endl;
		else if (pg==100 && pd!=100) cout<<"Broken"<<endl;
		else if (pg==0 && pd!=0) cout<<"Broken"<<endl;
		else cout<<"Possible"<<endl;

	}


} 