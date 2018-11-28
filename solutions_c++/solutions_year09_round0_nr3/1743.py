#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>

using namespace std;

#define M 19

int main()
{
    char w[M]={'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm'};
    int o[M+1];

    char s[500];
    int N;
    cin >> N;
    int count;
    int index;
    cin.getline(s,1);

    for (int cn(1); cn<=N; ++cn)
    {
	for (int i(0); i<M; ++i)
	    o[i]=0;
	o[M]=1;
	cin.getline(s,500);
	count=0;
	for (index=0; s[index]; ++index);

	for (--index; index>=0; --index)
	{
	    for (int j(0); j<M; ++j)
	    {
		if (w[j] == s[index])
		{
		    o[j]+=o[j+1];
		    if (o[j]>=1000) o[j]-=1000;
		}
	    }
	}

	count=o[0];

	cout << "Case #" << cn << ": ";
	if (count<10) cout << "000";
	else if (count<100) cout << "00";
	else if (count<1000) cout << "0";

	cout << count <<endl;
    }


    return 0;
}
