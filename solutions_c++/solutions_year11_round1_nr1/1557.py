// codejam_raa.cpp : 定义控制台应用程序的入口点。
//


#include <iostream>
#include <fstream>

using namespace std;


bool possible(int n, int pd, int pg)
{
	if(pg == 100 & pd != 100)
		return false;
	if(pg == 0 & pd != 0)
		return false;
	if(pd == 0)
		return true;
	bool su = false;
	int i ;
	for(i = 1; i <= 100 && i <= n; i++)
	{
		if( (i * pd) % 100 == 0){
			su = true;
			break;
		}

	}
	return su;
}
int main(int argc, char* argv[])
{
	ifstream in(argv[1]);
	int n;
	in >> n;
	int case_count = 1;
	while(n -- > 0)
	{
		int tn, tpd, tpg;
		in >> tn;
		in >> tpd;
		in >> tpg;
		bool p = possible(tn ,tpd, tpg);
		if(p)
		{
			cout<<"Case #"<<case_count++<<": Possible"<<endl;
		}else
		{
			cout<<"Case #"<<case_count++<<": Broken"<<endl;
		}
	}
	return 0;
}


