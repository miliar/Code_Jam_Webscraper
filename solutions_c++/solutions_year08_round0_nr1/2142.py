#include <iostream>
#include <map>
#include <string>

using namespace std;

const int ENGINE	=	100;
const int QUERIES	=	1000;

int switches(int eng_cnt, int queries[], int que_cnt)
{
	if(que_cnt <= 0)
		return 0;
	
	static int pos[ENGINE];
	memset(pos, -1, sizeof(pos));
	int cnt = 0, last = 0;
	for(int i = 0; i < que_cnt && cnt < eng_cnt; ++i) {
		if(pos[queries[i]] < 0) {
			++cnt;
			last = pos[queries[i]] = i;
		}
	}

	if(cnt < eng_cnt)
		return 0;
	else
		return 1 + switches(eng_cnt, queries + last, que_cnt - last);
}

int main()
{
	int N, S, Q;
	map<string, int> dict;
	char buf[128];
	static int query[QUERIES];
	cin >> N;
	for(int k = 1; k <= N; ++k) {
		cin >> S;
		cin.getline(buf, 128);
		dict.clear();
		for(int i = 0; i < S; ++i){
			cin.getline(buf, 128);
			dict[string(buf)] = i;
			cerr << "i = " << i << " line = " << buf << endl;
		}	
		cin >> Q;
		cerr << Q << endl;
		cin.getline(buf, 128);
		for(int j = 0; j < Q; ++j){
			cin.getline(buf, 128);
			query[j] = dict[string(buf)];
			cerr << buf << endl;
		}
		
		cout << "Case #" << k << ": " 
			<< switches(S, query, Q) << endl;
	}
	return 0;
}

