#include <deque>
#include <utility>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

deque<char> out;

const char* print_queue() {
	char * buffer = new char [3*out.size()+100];
	buffer[0] = buffer[1] = 0;
	for(int i = 0; i < out.size(); i++){
		if(!i && out.size() == 1) sprintf(buffer, "[%c]", out[i]);
		else if(!i) sprintf(buffer, "[%c,", out[i]);
		else if (i+1 == out.size()) sprintf(buffer+strlen(buffer), " %c]", out[i]);
		else sprintf(buffer+strlen(buffer), " %c,", out[i]);
	}
	if(!out.size()) sprintf(buffer, "[]");

	return const_cast<const char*>(buffer);
}

int main() {
	freopen("input", "r", stdin);
	int cases; scanf("%d\n", &cases);
	for(int i = 0; i < cases; i++) {
		deque<char*> goods; deque<char*> bads;
		int goodsc; scanf("%d ", &goodsc);
		char* arr;
		for(int i = 0; i < goodsc; i++) {
			arr = new char[3];
			scanf("%c%c%c", &arr[0], &arr[1], &arr[2]);
			goods.push_back(arr);
		}
		int badsc; scanf("%d ", &badsc);
		for(int i = 0; i < badsc; i++){
			arr = new char[2];
			scanf("%c%c", &arr[0], &arr[1]);
			bads.push_back(arr);
		}
		int go; scanf("%d ", &go);
		for(int i = 0; i < go; i++){
			char current; scanf("%c", &current);
			out.push_back(current);
			// check to combine
			for(int j = 0; j < goods.size() && out.size() > 1; j++){
				if(goods[j][0] == current) {
					if(goods[j][1] == out[out.size() - 2]) {
						out.pop_back(); out.pop_back(); out.push_back(goods[j][2]);
					}
				}
				else if(goods[j][1] == current) {
					if(goods[j][0] == out[out.size() - 2]) {
						out.pop_back(); out.pop_back(); out.push_back(goods[j][2]);
					}
				}
			}
			// check for clear
			for(int j = 0; j < bads.size() && out.size() > 1; j++) {
				if(bads[j][0] == out[out.size() - 1]) {
					if(find(out.begin(), out.end(), bads[j][1]) != out.end()) {
						out.clear();
					}
				}
				else if (bads[j][1] == out[out.size() - 1]) {
					if(find(out.begin(), out.end(), bads[j][0]) != out.end()) {
						out.clear();
					}
				}
			}
		}
		goods.clear(); bads.clear();
	    printf("Case #%d: %s\n", i+1, print_queue());
		out.clear();
	}
	return 0;
}
