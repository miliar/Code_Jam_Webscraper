#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
using namespace std;

ifstream fin("file\\input.txt");
ofstream fout("file\\output.txt");

int main()
{
	int nCases = 0, nButtons = 0, ans = 0;
	
	fin >> nCases;
	for(int i = 0; i < nCases; ++ i)
	{
		fin >> nButtons;

		int op = 1, ot = 0, bp = 1, bt = 0;ans = 0;
		char ob = '\0'; int p = 0;
		for(int j = 0; j < nButtons; ++ j)
		{
			fin >> ob >> p;
			if(ob == 'O'){
				int dt = abs(op-p);
				if(ot+dt <= ans){
					ot = ans;
					op = p;
				}
				else{
					dt -= abs(ans-ot);
					ans += dt;
					ot = ans;
					op = p;
				}
				++ ot; ++ ans;
			}
			else{
				int dt = abs(bp-p);
				if(bt+dt <= ans){
					bt = ans;
					bp = p;
				}
				else{
					dt -= abs(ans-bt);
					ans += dt;
					bt = ans;
					bp = p;
				}
				++ bt; ++ ans;
			}
		}
		fout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	//system("pause");
	return 0;
}