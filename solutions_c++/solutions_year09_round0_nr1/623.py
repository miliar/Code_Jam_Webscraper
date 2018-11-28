#include<iostream>
#include<string>
#include<vector>
#include<stdio.h>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})
int main()
{
    int L = GI;
    int D = GI;
    int N = GI;
    vector<string> ip;
    for(int i = 0; i < D; ++i)
    {
	string ss ;
	cin >> ss;
	ip.push_back(ss);
    }
    for(int nc = 1; nc <= N; ++nc)
    {
	string str;
	cin >> str;
	printf("Case #%d: ",nc);
	int toc[L+1][27];
	memset(toc,0,sizeof toc);
	int ind = 0,var = 0;
	while(ind < str.size())
	{
	    if(str[ind] == '(')
	    {
		ind++;
		while(str[ind] != ')')
		{
		    toc[var][str[ind]-'a'] = 1;
		    ind++;
		}
		ind++;
		var++;
	    }
	    else
	    {
		toc[var][str[ind]-'a'] = 1;
		var++;
		ind++;
	    }
	}
	long long int ret = 0;
	for(int i = 0; i < D; ++i)
	{
	    bool ff = true;
	    for(int j = 0 ; j < L; ++j)
	    {
		if(!toc[j][ip[i][j]-'a'])
		{
		    ff =  false;
		    break;
		}
	    }
	    if(ff) ret++;
	}
	cout << ret << endl;
    }
}
