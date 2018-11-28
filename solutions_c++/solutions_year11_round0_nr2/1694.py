#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<vector<int> > VII;
typedef vector<PII> VPII;

typedef vector<double> VD;
typedef vector<string> VS;

typedef long long LL;

struct triplet{
	char a, b, c;
};
struct duo{
	char a, b;
};

int main(){ 	
	int cases;
	scanf("%d\n", &cases);
	
	for(int caseNr = 1; caseNr <= cases; caseNr++){
		// go for it!	
		printf("Case #%d: ", caseNr);
		
		vector<char> stack;
		vector<triplet> combine; 	// maps/sets would be better..
		vector<duo> opposed;		// but vectors are fast enought here
		
		// READ
		int C;
		scanf("%d ", &C);
		for(int i=0;i<C;i++){
			triplet temp;
			scanf("%c%c%c ", &temp.a, &temp.b, &temp.c);
			combine.push_back(temp);
		}
		int D;
		scanf("%d ", &D);
		for(int i=0;i<D;i++){
			duo temp;
			scanf("%c%c ", &temp.a, &temp.b);
			opposed.push_back(temp);
		}
		
		// SIMULATE
		int N;
		scanf("%d ", &N);
		for(int i=0;i<N;i++){
			char c;
			scanf("%c", &c);
			stack.push_back(c);
			
			if(stack.size() > 1){
				char c1 = stack[stack.size()-1];
				char c2;
				
				// "Each pair of base elements may only appear together in one combination"
				
				// COMBINE elemets
				// "If the two elements from a pair appear at the end of the element list, then both elements of the pair will be immediately removed, and they will be replaced by the element they form"
				c2 = stack[stack.size()-2];
				for(int j=0;j<C;j++){
					triplet t = combine[j];
					if ((t.a == c1 && t.b == c2) || (t.b == c1 && t.a == c2)){
						stack.pop_back();
						stack.pop_back();
						stack.push_back(t.c);
						goto magic;
					}
				}
				
				// OPPOSED elements
				// "it is opposed to something in your element list, then your element list will be cleared"
				for(int k=0;k<stack.size() - 1;k++){
					c2 = stack[k];
					for(int j=0;j<D;j++){
						duo d = opposed[j];
						if ((d.a == c1 && d.b == c2) || (d.b == c1 && d.a == c2)){
							stack.clear();
							goto magic;
						}
					}
				}
				
				magic:;
			}
		}
		
		// PRINT SOLUTION
		printf("[");
		for(unsigned int i=0;i<stack.size();i++){
			printf("%c", stack[i]);
			if(i!=stack.size()-1)
				printf(", ");
		}
		printf("]\n");
		
		fflush(stdout);
	}
	
	return 0;
}
