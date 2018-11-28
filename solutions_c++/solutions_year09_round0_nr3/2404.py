#include <iostream>
#include <string>
using namespace std;


int parseit(string str,int index)
{
	string f = "welcome to code jam";
	int ret = 0,k;
	
	if(index==19) { return 1; }
	
	for(k=0;k<str.length();k++)
	{
		if(str[k]==f[index])
		{
			ret = (ret + parseit(str.substr(k+1),index+1)) % 10000;
		}
   	}
	return ret;
}

int main()
{
	int N,i,res;
	string inp,kch;
	
	cin >> N;
	getline(cin,kch);

	for (i=0;i<N;i++)
	{
		res = 0;
		getline(cin,inp);
		//cout << inp << endl;
		res = parseit(inp,0);		
		printf("Case #%d: %04d\n",i+1,res);
		inp.clear();
	}

}
