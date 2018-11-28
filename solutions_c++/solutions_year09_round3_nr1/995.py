#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

typedef struct _hash {
	char k;
	int v;
}Hash;

int init_hash(Hash *tbl, int len) {
	int i=0;
	for(i=0; i<len; i++) {
		tbl[i].k=' ';
		tbl[i].v=-1;
	}
	return 0;
}
int search_hash(char k, Hash *tbl, int len) {
	int i=0;
	for(i=0; i<len; i++) {
		if( tbl[i].k == k ) {
			return tbl[i].v;
		}
	}
	return -1;
}

int assign_hash(char k, int v, Hash *tbl, int len) {
	int i=0;
	for(i=0; i<len; i++) {
		if( tbl[i].k == ' ' ) {
			tbl[i].k = k;
			tbl[i].v = v;
			return v;
		}
	}
	return -1;
}

int main() {
	int dis[10] = {1,0,2,3,4,5,6,7,8,9};

	Hash hash[128];
	char input[128];
	//j指示，指派器的下标
	int i, j=0;
	int n;


	int result = 0;
	int presult = 0;
	int base = 1;
	int sk;
	
	ofstream fout("result.txt");
	cin >> n;
	int m=0;
	for(m=0; m<n; m++) {

	cin >> input;

	i=j=0;
	result=0;
	presult=0;
	base=1;
	sk=0;
	init_hash(hash, 128);

	for(i=0; i<strlen(input); i++) {
		sk = search_hash(input[i], hash, 128);
		//不存在此值
		if( sk == -1 ) {
			if( j<10 ) {
				sk = assign_hash(input[i], dis[j++], hash, 128);
			}
			else {
				sk = assign_hash(input[i], 9, hash, 128);
			}
		}
		presult *= 10;
		presult += sk;
	}
	
	if( j==0 ) {
		cout << "error, use unary\n";
	}
	else if( j==1 ) {
		base = 2;
	}
	else {
		base = j;
	}

	int tmp = 0;
	int tt = 1;
	while( presult != 0 ) {
		tmp = presult % 10;
		result += tmp * tt;
		tt *= base;
		presult /= 10;
	}
	fout << "Case #" << m+1 << ": " << result << endl;
}
	fout.close();
	return 0;
}