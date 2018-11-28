/*

Name: Takvir Hossain Tusher
E-Mail : tusher205@gmail.com

*/

#include <cstring>
#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define rep(i,m) for(long i=0;i<(long)(m);i++)
#define rep2(i,n,m) for(long i=n;i<(long)(m);i++)

//#define SMALL
#define LARGE

#ifdef SMALL
    #define N_MAX 6
#endif
#ifdef LARGE
    #define N_MAX 100
#endif

int T;
multimap<long,long> refMap;

bool checkValue(int k, int v){
    if (refMap.count(k) <= 0)
        return false;
    else{
        multimap<long,long>::const_iterator it;
        pair<multimap<long,long>::iterator, multimap<long,long>::iterator> ii;
        ii = refMap.equal_range(k);
        for(it = ii.first; it != ii.second; ++it){
            if(it->second == v)
                return true;
        }
    }

    return false;
}

bool checkMap(long k, long v){
    if( k == v)
        return true;

    if (checkValue(k,v))
        return true;
    else if (checkValue(v,k))
        return true;
    else
        return false;
}

int getDigits(int n){
    if (n <= 9)
        return 1;
    else if((n/10) <10)
        return 2;
    else if((n/10) <100)
        return 3;
    else if((n/10) <1000)
        return 4;
    else if((n/10) <10000)
        return 5;
    else if((n/10) <100000)
        return 6;
    else if((n/10) <1000000)
        return 7;
    else if((n/10) <10000000)
        return 8;

    else
        return 0;
}

long getX(long n, int digits){
    switch(digits){
        case 2:
            n = n*10;
            break;
        case 3:
            n = n*100;
            break;
        case 4:
            n = n*1000;
            break;
        case 5:
            n = n*10000;
            break;
        case 6:
            n = n*100000;
            break;
        case 7:
            n = n*1000000;
            break;
        case 8:
            n = n*10000000;
            break;
        default:
            n = 0;
    }
    return n;
}

long getY(int digits){
    long n = 0;
    switch(digits){
        case 2:
            n = 11;
            break;
        case 3:
            n = 111;
            break;
        case 4:
            n = 1111;
            break;
        case 5:
            n = 11111;
            break;
        case 6:
            n = 111111;
            break;
        case 7:
            n = 1111111;
            break;
        case 8:
            n = 11111111;
            break;

        default:
            n = 1;
    }
    return n;
}

long shiftDigit(long n, int digits){
    int last_d = n%10;
    long d = n/10;
    return getX(last_d,digits)+d;
}

long recycle(long n, int digits, long min, long max){
    long count =0;
    long shift = n;

    rep2(i,1,digits){
        shift = shiftDigit(shift, digits);
        if (shift < min || shift > max)
            continue;
        if(!checkMap(n,shift)){
            refMap.insert(pair<long,long>(n,shift));
            count++;
        }
    }

    return count;
}

int main() {
#ifdef SMALL
	freopen("C-small-attempt1.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif

    long min, max;
	cin >> T;
	rep2(nn,1,T+1) {
        cin>>min>>max;

        int digits = getDigits(max);
        long count = 0;

		printf("Case #%d: ", nn);
        refMap.clear();

		if (max <= 11)
            cout<<count<<endl;
        else{
            rep2(nm,min,max+1){
                long x = getX(1,digits);
                long y = getY(digits);
                if ((nm%x) == 0 || (nm%y) == 0)
                    continue;

                count += recycle(nm,digits,min,max);
            }
            cout<<count<<endl;
        }

	}
	return 0;
}
