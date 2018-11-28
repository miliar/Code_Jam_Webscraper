#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

////file selection
void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}
//ENDTEMPLATE_BY_ACRUSH_TOPCODER_extends_by_RSTanvir

int main()
{
    SetInputFile();

	long tc,tcounter;
	__int64 n,pd,pg;

	cin >> tc;
	tcounter = 0;

	while(tcounter++<tc)
	{
		scanf("%I64d %I64d %I64d",&n,&pd,&pg);

//		printf("%I64d %I64d %I64d\n",n,pd,pg);
		if((pg==100 && pd<100) || (pg==0 && pd>0))
			cout << "Case #" << tcounter << ": " << "Broken"<<endl;
		else
		{
			bool flag = false;
			for(int i=1;i<=100&&i<=n&&!flag ;i++)
			{
				if((pd * i)%100==0)
					flag = true;
			}

			if(flag)
				cout << "Case #" << tcounter << ": " << "Possible"<<endl;
			else 
				cout << "Case #" << tcounter << ": " << "Broken"<<endl;
		}
	}
	
    return 0;
}
