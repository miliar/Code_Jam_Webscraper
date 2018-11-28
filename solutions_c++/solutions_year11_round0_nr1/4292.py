/*#include <iostream>
#include <stdio.h>

using namespace std;
const int maxn = 105;
struct Item
{
	char type;
	int pos;
}item[maxn];
int t,n,cur_o,cur_b,next_o,next_b,ix;

int main()
{
	int i,ca = 1,counts,ans; char tt;

	scanf("%d",&t);

	while(t--)
	{
		scanf("%d",&n);

		for(i = 0;i < n;++i)
		{
			scanf("%c",&tt);
			scanf("%c %d",&item[i].type,&item[i].pos);
		}

		for(i = 0;i < n;++i)
		{
			if(item[i].type == 'O')
			{
				item[i].type = 'A';
				cur_o = item[i].pos;
				break;
			}
		}

		for(i = 0;i < n;++i)
		{
			if(item[i].type == 'B')
			{
				item[i].type = 'A';
				cur_b = item[i].pos;
				break;
			}
		}

		cur_o = cur_b = 1;
		counts = ans = 0;

		while(counts<n)
		{
		}
	}
}*/

#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
	int T,i;
	freopen("in.txt","r",stdin);
 	freopen("out.txt","w",stdout);

	cin>>T;
	int count = 1;
	while ( T-- ){
		int N;
		cin>>N;
		int times = 0,pre = 0;
		char temp;
		int pos[120]; 
		int OB[120];
		int current[2] = {1,1};
		for (i = 0; i < N; i++ ){
			cin>>temp>>pos[i];
			if ( temp == 'O' ) OB[i] = 0;
			else OB[i] = 1;
		}
		for ( i = 0; i < N; i++ ){
			if ( i != 0 && OB[i] == OB[i-1] ){
				pre = abs(pos[i] - current[ OB[i] ]) + 1 + pre;
				times = times + abs(pos[i] - current[ OB[i] ]) + 1;
			}
			else
			{
				if ( pre > abs( pos[i] - current[ OB[i] ])){
					pre = 1;
					times+=pre;
				}
				else{
					pre = abs(pos[i] - current[ OB[i] ]) - pre + 1;
					times+=pre;
				}
			}
			current[ OB[i] ] = pos[i];
		}
		cout<<"Case #"<<count++<<": "<<times<<endl;
	}
	return 0;
}