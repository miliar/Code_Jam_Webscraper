#include <iostream>
using namespace std;

int main()
{
	int T, C,D,N, n;
	
	int c[26][26], d[26][26], cur[26],i,j,k;
	char res[110];
	char ta, tb, tc;
	char base[]={'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
	cin>>T;
	for(int i = 0; i < T; i++)
	{
		memset(c,0,sizeof(int)*26*26);
		memset(d,0,sizeof(int)*26*26);
		memset(cur,0,sizeof(int)*26);
		n=0;
		cin>>C;
		for( j = 0; j< C; j++)
		{
			cin>>ta>>tb>>tc;
			c[ta-'A'][tb-'A'] = tc;
			c[tb-'A'][ta-'A'] = tc;
		}
		cin>>D;
		for( j = 0; j < D; j++)
		{
			cin>>ta>>tb;
			d[ta-'A'][tb-'A'] = 1;
			d[tb-'A'][ta-'A'] = 1;		
		}
		cin>>N;
		
		for( j = 0; j < N; j++)
		{
			cin>> tc;
			if(n==0) {
				res[n++] = tc; 
				cur[tc-'A']+=1;
				continue;
				}
				
			if(c[res[n-1]-'A'][tc-'A']==0 && c[tc-'A'][res[n-1]-'A']==0)
			{
				for(k = 0; k< 8; k++)
				{
					if(cur[base[k]-'A']>0 && d[base[k]-'A'][tc-'A'] ==1)
						{
						n = 0;
						memset(cur,0,sizeof(int)*26);
						break;
						}
				}
				if(k==8)
				{
					res[n++]=tc;
					cur[tc-'A']+=1;
				}
			}
			else
			{	if(cur[res[n-1]-'A']>0)
					cur[res[n-1]-'A'] -= 1;
			 	res[n-1] = c[res[n-1]-'A'][tc-'A'];
			 	cur[res[n-1]-'A'] += 1;
			}
		
		}
		cout<<"Case #"<<(i+1)<<": [";
		for(j = 0; j < n; j++)
		{
			if(j>0) cout<<", ";
			cout<<res[j];
		}
		cout<<"]\n";
	}
	
}
