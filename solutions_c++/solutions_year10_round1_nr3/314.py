#include <cstdio>
#include <cstdlib>
#include <string>
#include <utility>
#include <map>

#define mp make_pair
#define fi first
#define se second

using namespace std;

int t, a1, a2, b1, b2;
map<pair<int, int>, char> m;

int gcd(int a, int b)
{
    if (b == 0)
    	return (a);
   	return (gcd(b, a % b));
}    

int done(int a, int b)
{
    int c;
    map<pair<int, int>, char>::iterator itr;

    if (a > b)
    	return (done(b, a));
   	if (a == 0)
   		return (1);
  	c = gcd(a, b);
  	a /= c;
  	b /= c;
  	itr = m.find(mp(a, b));
  	if (itr != m.end())
  		return (itr -> se);
	if (! done(b % a, a))
		return (m[mp(a, b)] = 1);
	if (b % a + a < b && ! done(a, b % a + a))
		return (m[mp(a, b)] = 1);
	return (m[mp(a, b)] = 0);
}

int main()
{
    int i, a, b, ans;
    /*
    for (a = 1; a <= 100; a++)
    	for (b = a; b <= 100; b++)
    		if (done(a, b)) {
    			printf("%d %d\n", a, b);
    			break;
   			} 			
    */
    m.clear();
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
        ans = 0;
        for (a = a1; a <= a2; a++)
        	for (b = b1; b <= b2; b++) {
        		ans += done(a, b);
            }
  		printf("Case #%d: %d\n", i + 1, ans);
    }    
    
    return (0);
}

    
