// freecell.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
using namespace std;
int main()
{
	freopen("D:\\Statistics\\freecell\\A-small-attempt3.in","r",stdin);
	freopen("result.txt","w",stdout);
	int cas;
	cin>>cas;
	int icase = 0;
	while(icase<cas) {
		icase++;

		int n, pd, pg;
		cin>>n>>pd>>pg;

		int fenmu=100;
		for(int i = 2 ; i < 100 ; i++) {
			while(pd%i==0&&fenmu%i==0) {
				pd/=i;
				fenmu/=i;
			}
		}
		bool can = true;
		if(n>=fenmu) {
			if(fenmu!=1) {
				if(pg==100)can = false;
			}
		}
		else can = false;

		if(pd==0&&pg!=0||pg==0&&pd!=0)
			can = false;

		cout<<"Case #"<<icase<<": ";
		if(can) {
			cout<<"Possible"<<endl;
		}
		else cout<<"Broken"<<endl;

	}
	return 0;
}

