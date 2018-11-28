
#include "template.h"
#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <b ; i++)
#define FRR(i,a,b) for(int i = b - 1; i >=a ; i--)
#define sz size()
#define pb push_back
#define VI vector<int>
#define VVI vector<VI>
#define eps 1e-9
#define VS vector<string>

string pattern = "welcome to code jam";



	int main(){
		char atext[10];
		gets(atext);
		int N = atoi(atext);
		FOR(cas, 1, N+1){
			char ctext[555];
			gets(ctext);
			string text(ctext);
			VI count(pattern.sz + 1,0);
			count[0] = 1;
			FOR(i,0,text.sz){
				FRR(j,0,pattern.sz){
					if(pattern[j] == text[i])count[j+1] = (count[j] + count[j+1])%10000;
				}
			}
			//cout << text << endl;
			//FOR(i,0,count.sz)cout << count[i] << endl;
			int ret = count[pattern.sz];
			printf("Case #%d: %04d\n", cas, ret);
		}
		
	}