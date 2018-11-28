#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
#include<sstream>

typedef long long LL;

#define FOR(i, a, b)   for(LL i=a;i<b;i++)
#define RFOR(i, a, b)  for(LL i=a-1;i<=b;i--)
#define REP(i, a)      FOR(i, 0, a)
#define RREP(i, a)     RFOR(i, a, 0)
#define PB(x)          push_back(x)
#define BP()           pop_back()
#define SZ()           size()
#define LEN()          length()
#define BG             begin()
#define ED             end()

using namespace std;

int main()
{
	LL t, a, b, num, ans;
	string str, s, r;
	stringstream ss;
	vector<LL> vn;
	bool twice;
	
	scanf("%lld", &t);
	
	REP(i, t){
		scanf("%lld %lld", &a, &b);
		ans = 0;

		for(LL k = a; k <= b; k++){
			ss.clear();
			ss << k;
			ss >> str;
			
			r = str;
			vn.clear();	
					
			REP(j, str.length()){
				ss.clear();
				ss << r;
				ss >> num;
				
				if(num < k && num >= a){
					twice = false;
					REP(z, vn.SZ()){
						if(num == vn[z])
							twice = true;
					}
					
					vn.PB(num);
					
					if(!twice)
						ans++;

				}
				
				if(str.LEN() > 1){
					s = str.substr(str.LEN()-1 - j, j+1);
					r = s + str.substr(0, str.LEN()-1 - j);
					//cout << str << endl;
				}
			}	
			
		}
		
		printf("Case #%lld: %lld\n", i+1, ans);
		
	}
	
    return 0;
}