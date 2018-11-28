#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
using namespace std;


int main()
{

__int64  N=0;
int T, pd,pg;
int Nd;

freopen("A-large.in", "r", stdin);
freopen("OUTPUT.txt", "w", stdout);

scanf("%d",&T);
for(int Case=1;Case<=T;Case++){
	N=0;
	scanf("%l64d",&N);
	scanf("%d%d",&pd,&pg);
	Nd=100;

		if(pd<100&&pg==100)
	{printf("Case #%d: Broken\n",Case);
	continue;
	}
				if(pd==100&&pg==100)
	{printf("Case #%d: Possible\n",Case);
	continue;
	}
						if(pd==0&&pg==0)
	{printf("Case #%d: Possible\n",Case);
	continue;
	}
	if(pd>0&&pg==0){
	printf("Case #%d: Broken\n",Case);
	continue;
	
	}
	while(pd%2==0&&Nd%2==0){
		pd/=2;
		Nd/=2;

	}

	while(pd%5==0&&Nd%5==0){
		pd/=5;
		Nd/=5;

	}
	if(N<Nd)
	{printf("Case #%d: Broken\n",Case);
	continue;
	}

	printf("Case #%d: Possible\n",Case);

}



return 0;
}