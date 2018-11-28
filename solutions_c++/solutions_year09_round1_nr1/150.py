#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

int dynamic[11][11814486];

int getDynamic(int, int);

int main(void)
{
	memset(dynamic, -1, sizeof(dynamic));

	int t;
	cin>>t;
	string data;
	getline(cin, data);

	for(int caseN=1;caseN<=t;caseN++)
	{
		getline(cin, data);
		istringstream it(data);

		vector <int> dat;
		int temp;
		while(it>>temp) { dat.push_back(temp); }

		reverse(dat.begin(), dat.end());

		int ans;
		for(int i=2;;i++)
		{
			if(i<0) printf("a\n");
			bool flag=true;

			for(int j=0;j<dat.size();j++) if(!getDynamic(dat[j], i)) { flag=false; break; }
			if(flag) { ans=i; break; }
		}

		printf("Case #%d: %d\n", caseN, ans);
	}

	return 0;
}

int getDynamic(int base, int tar)
{	
	int &ret=dynamic[base][tar];
	if(ret!=-1) return ret;

	ret=false;

	if(tar==1) ret=true;
	else
	{
		int curBase=1;
		while(curBase<=tar) curBase*=base;

		curBase/=base;
		int next=0;
		while(tar>0) { int curDigit=tar/curBase; next+=curDigit*curDigit; tar%=curBase; curBase/=base; }
		ret=getDynamic(base, next);
	}

	return ret;
}
