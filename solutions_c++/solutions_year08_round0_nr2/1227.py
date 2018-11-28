#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

struct node {
	int start , finish;
	bool operator < (const node &o) const {
		if(start < o.start) return 1;
		else if(start == o.start) {
			if(finish < o.finish) return 1;
		}
		return 0;
	};
}temp;

vector<struct node> vec[2];
vector<struct node> :: iterator iter ,rm;

int ncase , delayTime ,a,b;
int cnt[2];

void clearVar(void) {
	cnt[0] = 0;
	cnt[1] = 0;
	vec[0].clear();
	vec[1].clear();
}

int convertString(char a , char b) {
	return (a-'0')*10 + (b-'0');
}

void rcvInput(void) {

	char str[10];
	int hour,min;
	int i;

	for(i=0;i<a;i++) {
		scanf("%s",str);
		hour = convertString(str[0] , str[1]);
		min = convertString(str[3] , str[4]);
		temp.start = hour*60 + min;
		scanf("%s",str);
		hour = convertString(str[0] , str[1]);
		min = convertString(str[3] , str[4]);
		temp.finish = hour*60 + min;
		vec[0].push_back(temp);
	}

	for(i=0;i<b;i++) {
		scanf("%s",str);
		hour = convertString(str[0] , str[1]);
		min = convertString(str[3] , str[4]);
		temp.start = hour*60 + min;
		scanf("%s",str);
		hour = convertString(str[0] , str[1]);
		min = convertString(str[3] , str[4]);
		temp.finish = hour*60 + min;
		vec[1].push_back(temp);
	}

}

void process(void) {
	while(!vec[0].empty() || !vec[1].empty()) {
		if(vec[0].empty()) {
			cnt[1] += vec[1].size();
			return;
		}
		else if(vec[1].empty()) {
			cnt[0] += vec[0].size();
			return;
		}
		
		int site = (vec[0].at(0) < vec[1].at(0))? 0 : 1;
		iter = vec[site].begin();
		cnt[site]++;

		while(iter != vec[0].end() && iter != vec[1].end()) {
			temp.start = iter->finish + delayTime;
			temp.finish = iter->finish + delayTime;
			rm = iter; 

			iter = upper_bound(vec[!site].begin() , vec[!site].end() , temp);
			vec[site].erase(rm);
			site = !site;

		}
	}
}

int main() {
	freopen("large.in","r",stdin);	
	freopen("large.sol","w",stdout);
//	freopen("out.txt","w",stdout);
	int x ,i;
	char str[10];
	scanf("%d",&ncase);

	for(x=1;x<=ncase;x++) { // x for the number of case
		
		clearVar();

		scanf("%d",&delayTime);
		scanf("%d%d",&a,&b); // a is A to B , b is B to A
		
		rcvInput();
		sort(vec[0].begin() , vec[0].end());
		sort(vec[1].begin() , vec[1].end());

		process();

		printf("Case #%d: %d %d\n",x ,cnt[0] ,cnt[1]);
	}

	return 0;
}
