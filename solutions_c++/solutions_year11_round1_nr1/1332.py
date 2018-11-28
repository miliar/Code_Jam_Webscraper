#include<vector>
#include<iostream>
#include<fstream>
#include<stdio.h>

using namespace std;

bool possible(long long int N, long long int  Pd, long long int Pg){
	if(Pd < 100 && Pg == 100)
		return false;
	else if(Pd > 0 && Pg == 0)
		return false;
	for(long long int D = 1; D <= N; D++){
		long long int win_today100 = D * Pd;
		if(win_today100 / D == Pd && win_today100 % 100 == 0)
			return true;
	}
	return false;
}

int main(int argc, char *argv[])
{
	ifstream ifs(argv[1]);
	int T;
	ifs >> T;
	for(int i=0;i<T;i++){
		long long int N, Pd, Pg;
		ifs >> N >> Pd >> Pg;

		cout << "Case #" << i+1 << ": ";
		if(possible(N, Pd, Pg))
			cout << "Possible";
		else
			cout << "Broken";
		cout << endl;
	}
	return 0;
}
