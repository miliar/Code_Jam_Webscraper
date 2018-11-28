#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	char digit[128];
	char number[100];
	int T, X;
	int base, i, len;
	long long res;

	scanf("%d", &T);
	X = 0;
	while (T--)
	{
		memset(digit, -1, sizeof(digit));
		scanf("%s", number);
		len = strlen(number);

		base = 0;
		for(i=0; i<len; i++) {
			if(digit[ number[i] ] == -1){
				digit[ number[i] ] = base++;
			}
		}

		digit[ number[0] ] = 1;
		for(i=1; i<len; i++) {
			if(number[i] != number[0]){
				digit[ number[i] ] = 0;
				break;
			}
		}

		//
		if(base == 1) base = 2;
		res = digit[ number[0] ];
		for(i=1; i<len; ++i) {
		    res *= base;
		    res += digit[ number[i] ];
		}

		cout << "Case #" << (++X) << ": " <<res<<endl;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
