#include <iostream>
#include <algorithm>

using namespace std;


inline void perm(int k, int cfg[], const char *src, char *dest)
{
	for(; *src; src += k, dest += k){
		for(int i = 0; i < k; ++i)
			dest[i] = src[cfg[i]];
	}
	*dest = 0;
}

inline int compress_size(const char *str)
{
	const char *orig = str;
	int L;
	L = 0;
	while(*str){
		++str;
		++L;
		while(*str == str[-1])
			++str;
	}
	/*int tmp;
	while(*str){
		tmp = 1;
		++str;
		while(str[0] == str[-1]){
			++str;
			++tmp;
		}

		if(tmp > L)
			L = tmp;
	}*/

	cerr << orig << " : " << L << endl; 
	return L;
}

int main()
{
	int N, k;
	const int MAX_LEN = 1000;
	char src[MAX_LEN + 5], dest[MAX_LEN + 5];
	int aux[8];
	cin >> N;
	for(int cas = 1; cas <= N; ++cas){
		cin >> k;
		cin >> src;
		cerr << "String len : " << strlen(src) << endl;
		int opt;
		
		for(int i = 0; i < k; ++i)
			aux[i] = i;
		
		perm(k, aux, src, dest);
		opt = compress_size(dest);
		while(next_permutation(aux, aux + k)){
			perm(k, aux, src, dest);
			int tmp = compress_size(dest);
			if(tmp < opt)
				opt = tmp;
		}

		cout << "Case #" << cas << ": " << opt << endl;

	}
	return 0;
}
