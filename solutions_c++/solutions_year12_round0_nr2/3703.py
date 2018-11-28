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

#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
//#include <iostream>

using namespace std;

int main(){
	
	ifstream cin;
	ofstream cout;
	cin.open("B-large.in");
	cout.open("output.txt");	
	int t;
	cin>> t;
	for(int i=0;i<t;i++){
		int n,s,p;
		cin>>n>>s>>p;
		int count=0;
		for(int j=0;j<n ;j++){
			int a;
			cin>>a;
			if(a>=(3*p-2))
				count++;

			else if (a>=(3*p-4)&& s>0 && p>1 ){
				s--;
				count++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;


	}

	return 0;
}


	