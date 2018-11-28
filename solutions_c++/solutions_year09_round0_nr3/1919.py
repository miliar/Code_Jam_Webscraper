#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

const char* CH = "welcome to code jam";
int N,L,LL;
long long res;
char str[600];
char ostr[20];
void func(int i,int j)
{
	if(j==L-1)
	{
		for(int k=i;k<LL;++k)
		{
			if(str[k] == CH[j])
				++res;
		}
	}
	else if(j<L)
	for(int k=i;k<LL;++k)
	{
		if(str[k]==CH[j])
			func(k+1,j+1);
	}
	
}
int main(int argc, char *argv[])
{
	FILE* ifp = freopen("C-small-attempt0.in","r",stdin);
	//FILE* ifp = freopen("C.in","r",stdin);
	FILE* ofp = freopen("C-small-attempt0.out","w",stdout);

	L = strlen(CH);
	cin>>N;
	getchar();
	for(int ii=0;ii<N;++ii)
	{
		cin.getline(str,600);
		LL = strlen(str);
		res = 0;
		func(0,0);
		sprintf(ostr,"Case #%d: %04ld",ii+1,res%10000);
		cout<<ostr<<endl;
	}
}
