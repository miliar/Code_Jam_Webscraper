#include <cstdio>
#include <iostream>
using namespace std;

int calc_factor(long long n)
{
	int i;
	int div[8] = {100, 50, 25, 20, 10, 5, 2, 1};
	
	for(i=0; n%div[i]; i++) {continue;}
		
	return 100/div[i];
}

int main()
{
	long long T, N, pd, pg, fd;
	bool possible = true;
	
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		possible = true;
		cin >> N >> pd >> pg;
		cout << "Case #" << t << ": ";
		
		fd = calc_factor(pd);		
		if(fd > N || (pg == 0 && pd != 0) || (pg == 100 && pd != 100) || (pd == 0 && pg == 100) || (pd == 100 && pg == 0))
			possible = false;
		
		if(possible) cout << "Possible" << endl;
		else cout << "Broken" << endl;
	}
	return 0;
}
