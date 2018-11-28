#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <bitset>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cctype>
#include <climits>
#include <cassert>

using namespace std;

int main()
{
//	freopen("B-large.in","r",stdin);
	//freopen("02large.txt","w",stdout);
	int T;
	cin >> T;
	char str[32];
	for (int i = 0 ;i < T ;i++){
		cin >> str;
		char *p = str;
		vector<char> v;
		while (*p != 0){
			v.push_back(*p);
			p++;
		}
		bool res = next_permutation(v.begin(),v.end());
		cout << "Case #" << i+1 << ": ";
		if (res){
			for(int j = 0 ;j < v.size() ;j++){
				cout << v[j];
			}
			cout << endl;
		}else{
			v.push_back('0');
			sort(v.begin(),v.end());
			int ll = 0;
			for (ll = 0 ;ll < v.size() ;ll++){
				if (v[ll] != '0')
					break;
			}
			cout << v[ll];
			for (int j = 0 ;j < v.size() ;j++){
				if (j != ll){
					cout << v[j] ;
				}
			}
			cout << endl;
		}
	}
	return 0;
}
