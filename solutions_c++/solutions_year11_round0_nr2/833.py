#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <deque>

using namespace std;

#define reep(i,f,t) for(int i=f ; i<int(t) ; ++i)
#define rep(i,n) reep(i, 0, n) 

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

int main()
{
	int n;
	scanf("%d", &n);
	rep(i, n){
		vector<char> str;
		char comb[26][26] = {{0}};
		bool opps[26][26] = {{false}};
		int c, d, m;
		scanf("%d", &c);
		rep(j, c){
			char a[3];
			scanf("%*c%c%c%c", &a[0], &a[1], &a[2]);
			comb[a[0]-'A'][a[1]-'A'] = a[2];
			comb[a[1]-'A'][a[0]-'A'] = a[2];
		}

		scanf("%d", &d);
		rep(j, d){
			char a[2];
			scanf("%*c%c%c", &a[0], &a[1]);
			opps[a[0]-'A'][a[1]-'A'] = true;
			opps[a[1]-'A'][a[0]-'A'] = true;
		}

		scanf("%d", &m);
		scanf("%*c");
		rep(j, m){
			char el;
			scanf("%c", &el);
			str.push_back(el);

			char nowcomb = comb[el-'A'][str[str.size()-2]-'A'];
			if(str.size()>=2 && nowcomb){
				str.pop_back();
				str[str.size()-1] = nowcomb;
			}
			
			el = str[str.size()-1];
			rep(k, str.size()-1){
				if(opps[str[k]-'A'][el-'A']){
					str.clear();
					break;
				}
			}
		}

		printf("Case #%d: [", i+1);
		rep(j, str.size())
			printf("%s%c", j?", ":"", str[j]);
		puts("]");
	}

	return 0;
}

