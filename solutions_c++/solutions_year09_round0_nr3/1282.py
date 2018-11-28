#include <cstdio>
#include <vector>
#include <map>

int main(){
	char buf[512] = "welcome to code jam";
	std::map<char, std::vector<int> > mat;
	int len = 0;
	for(; buf[len]; len++) mat[buf[len]].push_back(len);
	len++;
	const int N = atoi(gets(buf));
	for(int n = 1; n <= N; n++){
		gets(buf);
		std::vector<int> arr(len, 0);
		arr[0] = 1;
		for(int i = 0; buf[i]; i++){
			const std::map<char, std::vector<int> >::const_iterator f = mat.find(buf[i]);
			if(f == mat.end()) continue;
			for(std::vector<int>::const_iterator it = f->second.begin(), end = f->second.end(); it != end; it++){
				int x = *it;
				arr[x + 1] = (arr[x + 1] + arr[x]) % 10000;
			}
		}
		printf("Case #%d: %04d\n", n, arr.back());
	}
	return 0;
}
