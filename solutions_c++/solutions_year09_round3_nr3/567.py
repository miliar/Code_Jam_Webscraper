#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
#include <math.h>
using namespace std;



int findmin(int first, int last, vector <int> toreal){
	int* results = new int[toreal.size()];
	if(first == last)
		return 0;
	for (int j = 0; j < toreal.size(); j++){
		if ((toreal[j] >= first)&&(toreal[j] <= last)){
			results[j] = findmin(first, toreal[j] - 1, toreal) + findmin(toreal[j] + 1, last,toreal);
			results[j] += last - first;
			
			
		}
		else
			results[j] = -1;
		
	}
	bool someone = false;
	int min;
	for (int j = 0; j < toreal.size(); j++)
		if (results[j] != -1){
			min = results[j];
			someone = true;
			break;
		}
	if (!someone)
		return 0;
	for (int j = 0; j < toreal.size(); j++)
		if ((results[j] < min)&&(results[j] != -1))
			min = results[j];
	return min;
		
}

int main(){
	int n, p, q;	
	cin >> n;	
	for(int i = 0; i < n; i++){
		cin >> p;
		cin >> q;
		
		
		vector <int> torel;
		int pr;
		
		for (int j = 0; j < q; j++){
			cin >> pr;
			torel.push_back(pr - 1);
		}
		
		sort(torel.begin(), torel.end());
		
		int res = findmin(0, p - 1, torel);

		cout << "Case #" << i + 1 << ": " << res << endl;
	
		
	}
}