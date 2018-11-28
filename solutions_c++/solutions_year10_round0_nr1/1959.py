#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <bitset>

using namespace std;

int main()
{
    freopen("ina","r",stdin);
    freopen("outa","w",stdout);
    int cas=1,n,t,k,i;
    scanf("%d",&t);
	for (cas=1; cas<=t; cas++)
    {
        cin>>n>>k;
        k++;
        if (!(k%(1<<n))) cout<<"Case #"<<cas<<": ON\n";
        else cout<<"Case #"<<cas<<": OFF\n";
    }

	return 0;
}
