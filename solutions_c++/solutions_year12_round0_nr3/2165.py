#include <iostream>
#include <fstream>
#include <math.h>
#include <cstdlib>
#include <set>

using namespace std;

int T;

int solve_each(int nr, int A, int B){
	int n = 1, tmp = nr, sz;
	char buffer[32];
	
	while(tmp >= 10) tmp /= 10, n++;
	
	itoa (nr, buffer, 10);
	sz = strlen(buffer);
	
	//int result = 0;
	set<int> result;
	for(int i = 0; i < sz; ++i){
		int part1 = 0, part2 = 0;
		for(int j = 0; j <= i; ++j)
			part1 *= 10, part1 += buffer[j] - '0';
		for(int j = i+1; j < sz; ++j)
			part2 *= 10, part2 += buffer[j] - '0';
		for(int j = 0; j <= i; ++j)
			part2 *= 10;
		int tmp_result = (part1 + part2);
		int nr_tmp = tmp_result;
		int nr_cifre = 1;
		while(nr_tmp >= 10) nr_tmp /= 10, nr_cifre++;
		if(tmp_result <= B && tmp_result >= A && nr < tmp_result && sz == nr_cifre)
			result.insert(tmp_result);
	}
	
	return result.size();;
}

int solve(int A, int B){
	int t = 0;
	for(int i = A; i <= B; ++i)
		t += solve_each(i, A, B);
	return t;
}

int main(){
	ifstream in("C-large.in");
	ofstream out("C-large.out");
	in >> T;
	for(int i = 1; i <= T; ++i){
		int A, B;
		in >> A >> B;
		int ret = solve(A, B);
		out << "Case #" << i << ": " << ret << endl;
	}
	return 0;
}
