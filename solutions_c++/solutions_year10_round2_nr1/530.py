#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


set<string> s;

int main(int argc, char **argv)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int icase=0; icase<t; icase++){
		int n, m;
		char str[110];

		scanf("%d%d", &n, &m);
		
		s.clear();
		
		for(int i=0; i<n; i++){
			 
			scanf("%s", str);
			s.insert(string(str));
		}
		
		int counter=0;
		set<string>::iterator it;
		for(int i=0; i<m; i++){
			scanf("%s", str);
			char tmp[110];

			for(int j=0; str[j]!='\0'; j++)
			{
				tmp[j]=str[j];
				tmp[j+1]='\0';

				if(str[j+1]=='\0' || str[j+1]=='/'){
					it=s.find(string(tmp));
					if(it == s.end()){
						counter++;
						s.insert(string(tmp));
					}
				}
			}
		}
		printf("Case #%d: %d\n", icase+1, counter);
	}

	return 0;
}