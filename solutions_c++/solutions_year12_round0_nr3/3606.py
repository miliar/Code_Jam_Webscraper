
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdio>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>

using namespace std;

bool
check(int a, int b){
char x[8];
char y[8];
string q,w;
	
	itoa (b,y,10);
	itoa (a,x,10);
	q=x;
	w=y;
	w=w+w;
	//cout<<q<<" "<<w<<endl;
	for (int i=0;i<w.length()-q.length();i++){
		int c=0;
		for (int j=0;j<q.length();j++){
			int qwer=i+j;
			
			if (q.at(j)==w.at(qwer))
				c++;
			else break;	
		}
		if(c==q.length())
			return true;
	}
	return false;
}

int
main()
{  
	int n;
	ofstream fout("3ton.out");
    ifstream fin("ton.in");
	fin>>n;
	for (int be=0; be<n; be++){
		int a; 
		int b;
		int ans=0;
		fin>>a;
		fin>>b;
		for (int i=a;i<b;i++){
			for (int j=i+1;j<=b;j++){
				if (check(i,j))
					ans++;
			}
		}
		fout<<"Case #"<<be+1<<": "<<ans<<endl;
	}
	


//	system("Pause");
//	cout<<0<<endl;
    return 0;
}


