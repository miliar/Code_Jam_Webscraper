/*
Author : OmarEl-Mohandes
PROG   : B.cpp
LANG   : C++
*/
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <complex>
#include <valarray>
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define REP(i,k,m) for(int i=k;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)
int main()
{
	freopen("B.in" , "rt" , stdin);
    freopen("B.out" , "wt" , stdout);
	int t;
	cin >> t;
	for(int i = 0 ; i < t ; i ++)
	{
		int c , d , n ;
		string tem , word;
		map<pair<char , char> , bool>opp;
		map<pair<char , char> , char >com;
		cin >> c;
		for(int k = 0 ; k < c ; k ++){
			cin >> tem;
			com[mp(tem[0] , tem[1])] = tem[2];
			com[mp(tem[1] , tem[0])] = tem[2];
		}
		cin >> d;
		for(int k = 0 ; k < d ; k ++){
			cin >> tem;
			opp[mp(tem[0] , tem[1])] = 1;
			opp[mp(tem[1] , tem[0])] = 1;
		}
		cin >>d;
		cin >> word;
		tem = "";
		//FAQFDFQ
		for(int k = 0 ; k < word.size() ; k ++){
			tem += word[k];
			if(tem.size() >= 2){
				pair<char , char> tt = mp(tem[tem.size()-1] , tem[tem.size()-2]);
				if(com.find(tt) != com.end()){
					tem = tem.substr(0 , tem.size()-2) + com[tt];
				}
				else
				{
					for(int j = tem.size()-2 ; j >= 0 ; j --)
						if(opp.find(mp(tem[tem.size()-1] , tem[j])) != opp.end())
						{
							tem = "";
							break;
						}
				}
			}
		}
		printf("Case #%d: [" , i+1);
		for(int k = 0 ; k < tem.size() ; k ++){
			if(k)
				printf(", ");
			printf("%c" , tem[k]);
		}
		printf("]\n");
	}
	return 0;
}
