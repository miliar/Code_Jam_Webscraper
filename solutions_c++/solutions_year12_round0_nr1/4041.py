#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main()
{
	int T;
	char line[101];
	char trad[101] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

//{'ay','bh','ce','ds','eo','fc','gs','hx','id','ju','ki','lg','ml','nb','ok','pr','qz','rt','sn','tw','uj','vp','wf','xm','ya','zq';

	scanf("%d *%c",&T);
	for(int i=1; i<=T; i++)
	{
		gets(line);	
		printf("Case #%d: ",i);
		for(int j=0; j<strlen(line); j++)
		{
			if(line[j] == ' ') cout << " ";
			else cout << trad[line[j]-'a'];
		}
		cout << endl;
	}
	return 0;	
}
