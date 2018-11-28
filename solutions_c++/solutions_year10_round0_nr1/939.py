/*
 * A.cpp
 *
 *  Created on: 2010-5-8
 *      Author: LK_TMP
 */
#include<iostream>
#include<cstdio>
using namespace std;
int n,k,t;

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>n>>k;
		n=(1<<n)-1;
		cout<<"Case #"<<i<<": ";
		if((k&n)==n) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
	fclose(stdin);	fclose(stdout);
	return 0;
}



