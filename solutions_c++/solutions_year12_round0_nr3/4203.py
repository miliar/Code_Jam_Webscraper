#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <sstream>

using namespace std;

int check_permutation(int a, int b){
	int digits[10];

	for(int i = 0; i < 10; ++i)
		digits[i] = 0;
	
	while(a != 0){
		digits[a%10]++;
		a = a/10;
	}

	while(b!= 0){
		digits[b%10]--;
		b = b/10;
	}

	for(int i =0; i < 10; ++i){
		if(digits[i] != 0)
			return 0;
	}

	return 1;
}

int rotate_check(int a, int b){

	stringstream ss_a;
	stringstream ss_b;
	ss_a << a;
	ss_b << b;
	string a_str = ss_a.str();
	string b_str = ss_b.str();
	string temp;
	string copy;

	for(int i = b_str.length()-1;  i > 0; --i){
		copy.assign(b_str.begin(), b_str.begin()+i);
		temp.assign(b_str.begin()+i, b_str.end());
		if(a_str.compare(temp + copy) == 0){
			return true;
		}
	}
	return false;
}


int find_recycled(int a, int b){
	int count = 0;

	for(int i = a; i <= b; ++i){
		for(int j = a; j <= b; ++j){
			if(i == j){
				continue;
			}
			
			if(check_permutation(i, j)){
				if(rotate_check(i, j)){
					count++;
				}
			}
		}
	}

	count /= 2;

	return count;
}


unsigned int _rotr(const unsigned int value, int shift) {
	if ((shift &= sizeof(value)*8 - 1) == 0)
		return value;
	return (value >> shift) | (value << (sizeof(value)*8 - shift));
}

int main(int argc, char** argv){
	FILE *fp = fopen("C-small-attempt0.in", "rb");
	char line[20];
	int index = 0;
	int a, b;

	if(fp != NULL){
		while(fgets(line, 20, fp) != NULL){
			if(index == 0){
				index++;
				continue;
			}
			sscanf(line, "%d %d", &a, &b);
			
			cout << "Case #" << index << ": " << find_recycled(a, b) << endl;
			index++;
		}
	}
}
