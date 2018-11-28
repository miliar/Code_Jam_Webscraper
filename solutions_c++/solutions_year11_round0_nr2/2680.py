#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <deque>
#include <algorithm>
#include <functional>

using namespace std;

typedef long long int int64_t;
typedef long long unsigned int uint64_t;

enum Movement{
	COMBINE, CLEAR
};

struct Rule{
	Movement move;
	char a, b, res;
	Rule(Movement m, char ta, char tb, char tc=0x7F): move(m), a(min(ta,tb)), b(max(ta,tb)), res(tc)
	{}
	bool operator<(const Rule& r) const
	{
		if(move != r.move){
			if(move == COMBINE)
				return true;
			return false;
		}
		if(a != r.a)
			return a < r.a;
		return b < r.b;
	}
};

void print_stack(stack<char>& stk)
{
	if(stk.empty())
		return ;
	const char top = stk.top();
	stk.pop();
	if(!stk.empty()){
		print_stack(stk);
		printf(", %c", top);
	}else
		printf("%c", top);
}

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for(int ts=1;ts<=T;ts++){
		int combine, oppose;
		scanf("%d", &combine);
		set<Rule> rule;
		for(int i=0;i<combine;i++){
			char comb_list[4];
			scanf("%s", comb_list);
			rule.insert(Rule(COMBINE, comb_list[0], comb_list[1], comb_list[2]));
		}
		scanf("%d", &oppose);
		for(int i=0;i<oppose;i++){
			char cler_list[4];
			scanf("%s", cler_list);
			rule.insert(Rule(CLEAR, cler_list[0], cler_list[1]));
		}
		int invoke;
		map<char, int> exist;
		stack<char> stk;
		scanf("%d", &invoke);
		char inv_str[105];
		scanf("%s", inv_str);
		for(int i=0;i<invoke;i++){
			char add = inv_str[i];

			if(stk.empty()){
				stk.push(add);
				exist[add]++;
				continue;
			}

			set<Rule>::iterator it;
			//do{
				char top = stk.top();
				if((it = rule.find(Rule(COMBINE, top, add))) != rule.end()){
					stk.pop();
					exist[top]--;
				}
				if(it != rule.end())
					add = it->res;
			//}while(it != rule.end() && !stk.empty());

			bool clear = false;
			map<char,int>::iterator itc;
			for(itc=exist.begin();itc!=exist.end();itc++){
				if(itc->second > 0 && rule.find(Rule(CLEAR, add, itc->first)) != rule.end()){
					clear = true;
					while(!stk.empty()){
						exist[stk.top()]--;
						stk.pop();
					}
					break;
				}
			}

			if(!clear){
				stk.push(add);
				exist[add]++;
			}
		}
		printf("Case #%d: [", ts);
		print_stack(stk);
		puts("]");
	}
	return 0;
}

