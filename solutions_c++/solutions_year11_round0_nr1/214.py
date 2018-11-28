// A.cpp : 定义控制台应用程序的入口点。
//
#include <string>
#include <iostream>

using namespace std;

inline int abs(int k)
{
	return k>=0?k:-k;
}

int Solve()
{
	int n, p1, p2, t1, t2;
	cin >> n;
	string r[110];
	int pos[110];
	for(int i = 0; i<n; ++i)
		cin >> r[i] >> pos[i];
	p1 = p2 = 1;
	t1 = t2 = 0;
	for(int i = 0; i<n; ++i){
		if(r[i] == "O"){
			t1 += abs(p1-pos[i])+1;
			p1 = pos[i];
			if(t1 < t2+1)
				t1 = t2+1;
		}else{
			t2 += abs(p2-pos[i])+1;
			p2 = pos[i];
			if(t2 < t1+1)
				t2 = t1+1;
		}
	}
	if(t1 < t2)
		t1 = t2;
	return t1;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int nCase;
	cin >> nCase;
	for(int i = 1; i<=nCase; ++i)
		printf("Case #%d: %d\n", i, Solve());
	fclose(stdin);
	fclose(stdout);
	return 0;
}

