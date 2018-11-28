#include<cstdio>
#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream fin;
	fin.open("A.in");
	freopen("A.out","w",stdout);
	int T;
	fin>>T;
	for (int TT=1;TT<=T;TT++){
		long long n;
		int x,y;
		fin>>n>>x>>y;
		if ((y==0&&x>0)||(y==100&&x<100))printf("Case #%d: Broken\n",TT);
		else {
			int c=100;
			for (int i=100;i>=2;i--)if (c%i==0&&x%i==0){
				c/=i;x/=i;
			}
			if (n>=c)printf("Case #%d: Possible\n",TT);
			else printf("Case #%d: Broken\n",TT);
		}
	}
	return 0;
}
