/*
TASK: A
LANG: C++
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;
#define sz(x) ((int)(x).size())
#define MAXSIZE 40


int main(){
	freopen("B-large.in","rt",stdin);
	freopen("BsmallBIG.out","wt",stdout);
	char listChar[110];
	char tempChar[4];
	map<string, char> cMap;
	set<string> oSet;
	vector<char> inputList;
	vector<char> lastList;
	set<char> base ; //Q, W, E, R, A, S, D, F
	base.insert('Q');base.insert('W');base.insert('E');base.insert('R');base.insert('A');base.insert('S');base.insert('D');base.insert('F');

	int N;
	int cNum = 0, oNum = 0, lNum = 0;
	map<string, char>::iterator itMap;
	set<string>::iterator itSet;
	scanf("%d",&N);
	for (int ii = 1; ii <= N; ii++) {		
		scanf("%d",&cNum); 
		for(int iT = 0; iT < cNum; iT++){
			char c;
			scanf("%s", tempChar);
			c = tempChar[2];
			tempChar[2] = '\0';
			string subTemp(tempChar);
			cMap[subTemp] =  c;
			reverse(subTemp.begin(), subTemp.end());
			cMap[subTemp] =  c;
		}				
		scanf("%d",&oNum);
		for(int iT = 0; iT < oNum; iT++){
			scanf("%s", tempChar);
			tempChar[2] = '\0';
			string subTemp(tempChar);
			oSet.insert(subTemp);
			reverse(subTemp.begin(), subTemp.end());
			oSet.insert(subTemp);
		}
		scanf("%d", &lNum);
		scanf("%s", listChar);

		for(int iT = 0; iT < lNum; iT++){
			inputList.push_back(listChar[iT]);
		}   
		reverse(inputList.begin(),inputList.end());
		
		while(inputList.size() > 0){
			lastList.push_back(inputList.back());
			inputList.pop_back();
			if (lastList.size() > 1 && base.find(lastList[lastList.size()-1]) != base.end()) { // base				
				tempChar[0] = lastList[lastList.size()-1];
				tempChar[1] = lastList[lastList.size()-2];
				tempChar[2] = '\0';
				string subTemp(tempChar);
				itMap = cMap.find(subTemp);	
				if (itMap != cMap.end() ){
					lastList.pop_back();
					lastList.pop_back();
					lastList.push_back(cMap[subTemp]);
				} else {// find oposite
					if(lastList.size() > 0)
					for(int iTB = lastList.size() - 2; iTB >= 0; iTB--) {
						tempChar[0] = lastList[iTB];
						tempChar[1] = lastList[lastList.size()-1];
						tempChar[2] = '\0';
						string subTemp(tempChar);
						if (oSet.find(tempChar) != oSet.end()) {// clear
							//lastList.erase(lastList.begin() + iTB , lastList.end());
							lastList.clear();
							break;
						}			
					}
				} 
			}
		}
		printf("Case #%d: [",ii);
		for(int TT = 0; lastList.size() > 0 && TT < lastList.size() -1 ; TT++){
			char cTemp = lastList[TT];
			printf("%c, ", cTemp);
		}
		if(lastList.size() > 0)
			printf("%c",lastList[lastList.size()-1]);
		printf("]\n");
		inputList.clear();
		lastList.clear();
		cMap.clear();
		oSet.clear();
	}
	return 0;
}
