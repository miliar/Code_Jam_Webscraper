#include <iostream>
using namespace std;

typedef long long ll;

char ch[100];
ll hash[500];
ll a[100] , len;

ll Cal(ll index)
{
	ll temp , ret;
	ret = 0;
	temp = 1;
	for (int i=len -1 ; i>=0 ; i--){

		ret += (a[i] * temp);
		temp *= index;
	}

	return ret;
}	

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w"  ,stdout);
	ll n , cnt ,  total , ans , cas = 0;	
	scanf("%lld" , &n);
	while (n--){

		cas++;
		scanf("%s" , ch);
		len = strlen(ch);
		
		cnt = 0;
		memset(hash , 0 , sizeof(hash));
		for (ll i=0 ; i<len ; i++){

			if (hash[ch[i]] == 0){

				cnt++;
				hash[ch[i]] = 1;
			}
		}

		total = cnt;

		cnt = 0;
		memset(hash , -1 , sizeof(hash));
		hash[ch[0]] = 1;
		for (ll i=0 ; i<len ; i++){

			if (hash[ch[i]] != -1){

				a[i] = hash[ch[i]];
			}
			else{
				
				if (cnt == 0){

					hash[ch[i]] = 0;
					cnt += 2;
				}
				else{

					hash[ch[i]] = cnt;
					cnt++;
				}
				a[i] = hash[ch[i]];
			}
		}

		if (total == 1){

			total = 2;
		}
		ans = Cal(total);
		printf("Case #%lld: %lld\n" , cas , ans);
	}
	return 0;
}