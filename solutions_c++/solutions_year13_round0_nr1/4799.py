#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <map>
#include <string>

#define n 4
using namespace std;

int main()
{
	int t;
	char mp[256];
	string str[4];
	cin >> t;
	for(int T=1;T<=t;T++)
	{
		memset(mp,0,sizeof(mp));
		for(int i=0;i<n;i++)
			cin >> str[i];
		int ow,xw;
		ow=xw=0;
		for(int i=0;i<n;i++)
		{
			mp['T']=mp['O']=mp['X']=0;
			for(int j=0;j<n;j++)
				mp[str[i][j]]++;
			if( mp['O'] == 4 || ( mp['O'] == 3 && mp['T'] == 1 ) ) ow=1;
			if( mp['X'] == 4 || ( mp['X'] == 3 && mp['T'] == 1 ) ) xw=1;
		}
		int dots=mp['.'];
		for(int i=0;i<n;i++)
		{
			mp['T']=mp['O']=mp['X']=0;
			for(int j=0;j<n;j++)
				mp[str[j][i]]++;
			if( mp['O'] == 4 || ( mp['O'] == 3 && mp['T'] == 1 ) ) ow=1;
			if( mp['X'] == 4 || ( mp['X'] == 3 && mp['T'] == 1 ) ) xw=1;
		}
		mp['T']=mp['O']=mp['X']=0;
		for(int j=0;j<n;j++)
			mp[str[j][j]]++;
		if( mp['O'] == 4 || ( mp['O'] == 3 && mp['T'] == 1 ) ) ow=1;
		if( mp['X'] == 4 || ( mp['X'] == 3 && mp['T'] == 1 ) ) xw=1;
		mp['T']=mp['O']=mp['X']=0;
		for(int j=0;j<n;j++)
			mp[str[j][n-j-1]]++;
		if( mp['O'] == 4 || ( mp['O'] == 3 && mp['T'] == 1 ) ) ow=1;
		if( mp['X'] == 4 || ( mp['X'] == 3 && mp['T'] == 1 ) ) xw=1;

		if( ow && xw )
			printf("Case #%d: Draw\n",T);
		else if( ow || xw )
			printf("Case #%d: %c won\n",T,(ow)?'O':'X');
		else if ( dots )
			printf("Case #%d: Game has not completed\n",T);
		else
			printf("Case #%d: Draw\n",T);
	}
	return 0;
}