// square.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
using namespace std;
char data[50][100];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	int cas, tcas = 0;
	cin>>cas;
	bool yes;
	while(tcas<cas) {
		tcas++;
		int row, col;
		cin>>row>>col;
		yes = true;
		for(int i = 0 ; i < row ; i++)
			scanf("%s",data[i]);

		for(int i = 0 ; i < row ; i++) {
			for(int j = 0 ; j < col ; j++) {
				if(data[i][j] == '#') {
					if(i+1<row&&j+1<col&&data[i+1][j]=='#'&&data[i][j+1]=='#'&&data[i+1][j+1]=='#'){
						data[i][j] = '/', data[i][j+1]='\\', data[i+1][j]='\\', data[i+1][j+1]='/';
					}
					else
					{
						yes = false;
						break;
					}
				}
			}
		}
		cout<<"Case #"<<tcas<<":"<<endl;
		if(yes) {
			
			for(int i = 0 ; i < row ; i++)
				printf("%s\n",data[i]);
		}
		else cout<<"Impossible"<<endl;
	}
	return 0;
}

