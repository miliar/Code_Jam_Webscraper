//============================================================================
// Name        : C.cpp
// Author      : Artem A. Khizha
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>

using namespace std;

int main() {
    long tnum;
    long g[1000], c[1000];
    long long s[1000];
	cin >> tnum;
	for (long ti = 1; ti <= tnum; ti++) {
	    memset(c, (char)-1, sizeof(c));
	    memset(s, 0, sizeof(s));
	    long r, n, k;
	    cin >> r >> k >> n;
	    for (long i = 0; i < n; i++)
	        cin >> g[i];
	    long cur = 0, prev;
	    long cnt = 0;
	    while (c[cur] == -1 && r != cnt++) {
	        //cout << "Moving from " << cur;
	        prev = cur;
            c[cur] = cnt;
	        s[cnt] = g[cur];
	        cur = (cur+1 < n)? cur+1 : 0;
	        while (s[cnt] <= k && prev != cur) {
	            if (s[cnt] + g[cur] > k)
	                break;
	            s[cnt] += g[cur];
	            cur = (cur+1 < n)? cur+1 : 0;
	        };
	        s[cnt] += s[cnt-1];
	        //cout << " to " << cur << endl;
	    }
	    if (c[cur] == -1)  {
	        cout << "Case #" << ti << ": " << s[cnt-1] << endl;
	        continue;
	    }
	    long m = cnt - c[cur] + 1;
	    long p = c[cur] - 1;
	    //cout << "Period " << m << endl;
	    //cout << "Phase " << p << endl;
	    if (m == 0)
	        cerr << "AAAAA!" << endl;
	    cnt = (r - p)/m;
	    long long sum = s[p]+(s[p+m]-s[p])*cnt;
	    for (long i = 0; i < (r-p)%m; i++)  {
	        long long st = 0;
	        prev = cur;
            while (st <= k) {
                if (st + g[cur] > k)
                    break;
                st += g[cur];
                cur = (cur+1 < n)? cur+1 : 0;
                if (prev == cur)
                    break;
            };
            //cout << st << endl;
            sum += st;
        }
	    cout << "Case #" << ti << ": " << sum << endl;
	}
	return 0;
}
