#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

const int NMAX = 16 * 1024;
int arr[NMAX];
int k;
int n;
pair<int,ll> next(int cur){
	ll w = 0;
	int i = cur;
	while (1){
		if (w > k - arr[i]) break;
		w += arr[i];
		i = (i + 1) % n;
		if (i == cur) break;
	}
	return make_pair(i,w);
}

vector<ll> beforeCircle;
vector<ll> circle;
int pos[NMAX];

void extractCircle(int position){
	for (int i = position; i < beforeCircle.size(); i++)
		circle.push_back(beforeCircle[i]);
	beforeCircle.resize(position);
}

void extract(){
//	printf("--extracting--\n");
	memset(pos,-1,sizeof(pos));
	int cur = 0;	
	pos[0] = 0;
	while (1){
		pair<int,ll> nextGr = next(cur);
//		printf("%d %lld\n",nextGr.first,nextGr.second);
		beforeCircle.push_back(nextGr.second);
		if (pos[nextGr.first] != -1){
			extractCircle(pos[nextGr.first]);
			return;
		}
		pos[nextGr.first] = beforeCircle.size();		
		cur = nextGr.first;
	}
}

ll sum(vector<ll> & vec, int cnt){
	ll result = 0;
	for (int i = 0; i < cnt; i++)
		result += vec[i];
	return result;
}

ll countMoney(int R){
	extract();
	if (beforeCircle.size() >= R)
		return sum(beforeCircle, R);
	ll result = sum(beforeCircle, beforeCircle.size());
	R -= beforeCircle.size();
	ll circleMoney = sum(circle, circle.size());
//	printf("circleMoney = %lld\n",circleMoney);
	result += circleMoney * (R / circle.size());
	result += sum(circle, R % circle.size());
	return result;
}

void doTest(int testNumber){
	beforeCircle.clear();
	circle.clear();
	int R; 
	//scanf("%d%d%d",&R,&k,&n);
	cin >> R >> k >> n;
	for (int i = 0; i < n; i++)
		scanf("%d",&arr[i]);
	ll result = countMoney(R);
	printf("Case #%d: %lld\n",testNumber,result);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i++)
		doTest(i + 1);		

	return 0;
}