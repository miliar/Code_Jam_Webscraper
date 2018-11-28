// c.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fin = freopen("input.txt", "r", stdin);
	FILE* fout = freopen("output.txt", "w", stdout);
	
	int T;
	cin>>T;
	for(int t=0; t<T; t++){
		int n;
		scanf("%d", &n);

		int mas;
		int mask = 0, min = 2000000;
		long sum = -2000000;

		for(int i=0; i<n; i++){
			scanf("%d", &mas);
			mask ^= mas;
			if(mas<min){
				sum+=min;
				min = mas;
			}else
				sum+=mas;
		}

		cout<<"Case #"<<t+1<<": ";
		if(mask) cout<<"NO"<<endl;
		else cout<<sum<<endl;		
	}

	fclose(fin);
	fclose(fout);
	return 0;
}

