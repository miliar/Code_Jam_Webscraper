#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <sstream>
#include <iomanip>

using namespace std;
#define st first
#define fin second.first
#define c second.second
#define INF 2000000000

typedef long long ll;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;


int main(){
	int L,D,N;
	cin >> L >> D >> N;
	vector<string> word(D);
	for(int i=0;i<D;i++) cin >> word[i];

	for(int n=0;n<N;n++){
		cout << "Case #" << n+1 << ": ";
		string s;
		cin >> s;
		int sol=0;
		for(int i=0;i<word.size();i++){
			bool val=1;
			for(int j=0,k=0;j<s.size();k++){
				if(s[j]!='(' && word[i][k]!=s[j]){ val=0; break; }
				else if(s[j]!='(') j++;
				else {
					int p;
					bool e=0;
					for(p=j+1;s[p]!=')';p++) if(s[p]==word[i][k]) e=1;
					if(e) j = p+1;
					else { val=0; break; }
				}
			}
			if(val) sol++;
		}
		cout << sol << endl;

	}
}
