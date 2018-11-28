#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

struct node_t{
	std::map<char, node_t*> data;
	~node_t(){
		for(std::map<char, node_t*>::const_iterator it = data.begin(); it != data.end(); it++){
			delete it->second;
		}
	}
};

int main(){
	node_t list;
	int L = 0, D = 0, N = 0;
	scanf("%d %d %d", &L, &D, &N);
	char buf[1024];
	for(int i = 0; i < D; i++){
		scanf("%s", buf);
		node_t* ptr = &list;
		for(int j = 0; j < L; j++){
			std::map<char, node_t*>::const_iterator f = ptr->data.find(buf[j]);
			if(f != ptr->data.end()){
				ptr = f->second;
			}else{
				ptr = ptr->data[buf[j]] = new node_t;
			}
		}
	}
	for(int i = 1; i <= N; i++){
		std::vector<node_t*> stack, neu;
		stack.push_back(&list);
		scanf("%s", buf);
		int start = -1;
		for(int j = 0; stack.size() && buf[j]; j++){
			switch(buf[j]){
			case '(':
				start = j;
				break;
			case ')':
				neu.clear();
				for(int k = start + 1; k < j; k++){
					for(std::vector<node_t*>::const_iterator it = stack.begin(); it != stack.end(); it++){
						std::map<char, node_t*>& p = (*it)->data;
						std::map<char, node_t*>::const_iterator f = p.find(buf[k]);
						if(f != p.end()) neu.push_back(f->second);
					}
				}
				neu.swap(stack);
				start = -1;
				break;
			default:
				if(start >= 0) break;
				neu.clear();
				for(std::vector<node_t*>::const_iterator it = stack.begin(); it != stack.end(); it++){
					std::map<char, node_t*>& p = (*it)->data;
					std::map<char, node_t*>::const_iterator f = p.find(buf[j]);
					if(f != p.end()) neu.push_back(f->second);
				}
				neu.swap(stack);
			}
		}
		std::sort(stack.begin(), stack.end());
		std::vector<node_t*>::const_iterator it = std::unique(stack.begin(), stack.end());
		printf("Case #%d: %d\n", i, it - stack.begin());
	}
	return 0;
}
