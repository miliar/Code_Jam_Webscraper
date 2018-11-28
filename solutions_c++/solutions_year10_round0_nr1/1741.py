#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");




int main(void)
{

	int ttt;
	cin >> ttt;
	int ct = 0;
	
	
	
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		
		int n,k;
		string ans = "OFF";
		
		cin >> n >> k;
		k++;
		if(k%(1<<n)==0)
			ans="ON";
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}

