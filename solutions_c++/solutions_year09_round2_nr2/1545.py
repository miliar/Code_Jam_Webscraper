#define INPUT "C:\\Documents and Settings\\www\\My Documents\\Visual Studio 2005\\Projects\\CodeJam\\CodeJam\\B-small-attempt4.in"
#define OUTPUT INPUT ".out"
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cassert>
#include<fstream>
#include<cstdio>

using namespace std;

int main()
{
	freopen(INPUT,"r",stdin);
	freopen(OUTPUT,"w",stdout);
	int T; scanf("%d",&T);
	int t = 1;
	while(T--) {
		int N ; scanf("%d",&N);
		int nN = N;
		int nN1 = N,sz = 0;
		vector<int> num;
		vector<int> nnum;
		
			
		
		while(nN1) {
			sz++;
			nN1 /= 10;
		}
		num.resize(sz);
		int k = 0;
		while(nN) {
			num[k] = nN % 10;
			nN /= 10;
			k++;
		}
		reverse(num.begin(),num.end());
		
		nnum = num;
		next_permutation(num.begin(),num.end());
		if(num.size() == 1) {
			num.push_back(0);
			goto here;
		}
		int newnum = num[0];
		for(int i = 1 ; i < num.size() ; ++i) {
			newnum *= 10;
			newnum += num[i];
		}
		if(num[0] == 0) {
			if((N % 10) == 0) {
				int nnN = N;
				int cnt = 0;
				while((nnN % 10) == 0) {
					nnN /= 10;
					cnt ++;
				}
				int sz1 = 0;
				int nnnN = nnN;
				while(nnN) {
					sz1++;
					nnN /= 10;
				}
				vector<int> num1(sz1);
				int k = 0;
				while(nnnN) {
					num1[k] = nnnN % 10;
					nnnN /= 10;
					k++;
				}
				reverse(num1.begin(),num1.end());
				next_permutation(num1.begin(),num1.end());
				vector<int> p;
				p.push_back(num1[0]);
				for(int i = 0 ; i < cnt + 1 ; ++i)
					p.push_back(0);
				if(num1.size() > 1)
					for(int i = 1 ; i < num1.size() ; ++i)
						p.push_back(num1[i]);
				num.resize(p.size());
				num = p;
				goto here;
			}
		}
		if(newnum <= N && (num[0] != 0)) {
			vector<int> p(num.size() + 1);		
			p[0] = num[0];
			p[1] = 0;
			for(int i = 1 ; i < num.size() ; ++i)
				p[i + 1] = num[i];
			num.resize(p.size());
			num = p;
			goto here;
		}

		here:;
		printf("Case #%d: ",t++);
		for(int i = 0 ; i < num.size() ; ++i)
			printf("%d",num[i]);
		printf("\n");
		
	}
}