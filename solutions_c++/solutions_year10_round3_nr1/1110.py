/*
Author : tatvamasi
Date : 22-05-2010
Usage : $> ./a.out < input.txt		(Input redirection. Takes no command line arguments.)
3rd Party Libs : 
	1.	Name :							URL :
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <functional>
#include <stdlib.h>
#include <string.h>

using namespace std;

bool intersect(int x1, int x2, int y1, int y2){
	//cout << x1 << " " << x2 << " " << y1 << " " << y2 << endl;
	if(x1 <= y1 && x2 >= y2){
		return true;
	} 
	if(x1 >= y1 && x2 <= y2){
		return true;
	}
	return false;
}

main(){
	long long T = 0; cin >> T;

	for(long long i=0; i<T; i++){
		long long answer=0;
		long long N=0; cin >> N;
		vector<pair<int, int> > lines;
		for(long long n=0; n<N; n++){
			int A=0; int B=0;
			cin >> A >> B;
			pair<int, int> line(A, B);
			lines.push_back(line);
		}
		//cout << "---" << endl	;
		
		for(int n=0; n<N; n++){
			for(int m=n+1; m<N; m++){
				if(intersect(lines[n].first, lines[n].second, lines[m].first, lines[m].second)) answer++;
			}
		}
		
		cout << "Case #" << i+1 << ": " << answer << endl;
		
	}
}
