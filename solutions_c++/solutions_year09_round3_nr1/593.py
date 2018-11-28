#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <set>
#include <numeric>

using namespace std;

#define SZ(A) (A).size()
#define ALL(A) (A).begin(), (A).end()
#define SORT(A) sort(ALL(A))
#define REP(I,N) for(int I=0, I<N ; I++)
#define PB push_back

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<long long> vl;
typedef vector<vl> vvl;

int main(void){

	int T;
	cin >> T;
	for(int t=1 ; t<=T ; t++){
		string num;
		cin >> num;
		int cnt = 0;
		vector<int> conv(40, -1);
		int j=1;
		for(int i=0 ; i<SZ(num) ; i++){
			if('a' <= num[i] && num[i] <= 'z'){
				cnt += conv[num[i]+10-'a'] == -1;
				if(conv[num[i]+10-'a'] == -1){
					conv[num[i]+10-'a'] = j;
					j++;
				}
				num[i] = '0' + conv[num[i]+10-'a'];
			}else{
				cnt += conv[num[i]-'0'] == -1;
				if(conv[num[i]-'0'] == -1){
					conv[num[i]-'0'] = j;
					j++;
				}
				num[i] = '0' + conv[num[i]-'0'];
			}
		}
//		cout << num << endl;
//		cout << "a : " << cnt << endl;

//		for(int i=0 ; i<SZ(conv) ; i++)
//			cout << conv[i] << " ";
//		cout << endl;
		cnt = max(cnt,2);

		unsigned long long sum = 0.;
		for(int i=0 ; i<SZ(num) ; i++){
			if(num[i] == '1')
				sum += 1;
			else if( num[i] > '2')
				sum += num[i]-'0'-1;
			sum *= cnt;
		}
		sum /= cnt;
		cout <<"Case #"<<t<<": "<< sum << endl;
	}

	return 0;
}
