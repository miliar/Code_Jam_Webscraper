#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int c,d,Tcase,n,i,j,k,pos;
	int dchange[26][26];
	bool cchange[26][26],flag;
	char op[4],ch,mode[111],str[111];
	//freopen("input.txt","r",stdin);
	//ofstream cout("output.txt");
	cin>>Tcase;
	for( i = 1 ; i <= Tcase ; i++)
	{
		cin>>c;
		memset(cchange,0,sizeof(cchange));
		memset(dchange,-1,sizeof(dchange));
		flag = pos = 0 ;
		for( j = 0 ; j < c ; j++)
		{
			scanf("%s",op);
			dchange[op[0]-'A'][op[1]-'A'] = op[2];
			dchange[op[1]-'A'][op[0]-'A'] = op[2];
		}
		cin>>d;
		for( j = 0 ; j < d ; j++)
		{
			scanf("%s",op);
			cchange[op[0]-'A'][op[1]-'A'] = 1;
			cchange[op[1]-'A'][op[0]-'A'] = 1;
		}
		scanf("%d %s",&n,mode);
		for( j = 0 ; j < n ; j++)
		{
			if(pos==0)
			{
				str[pos++] = mode[j];
			}
			else
			{
				if(dchange[str[pos-1]-'A'][mode[j]-'A']>-1)	//dop
				{
					str[pos-1] = dchange[str[pos-1]-'A'][mode[j]-'A'];
				}
				else
				{
					for ( k = flag = 0 ; k < pos ; k++)
					{
						if(cchange[str[k]-'A'][mode[j]-'A'])
						{
							pos = 0 ;
							flag = 1 ;
							break;
						}
					}
					if(!flag)	str[pos++] = mode[j];
				}
			}
		}
		cout<<"Case #"<<i<<": [";
		for( j = 0 ; j < pos-1 ; j++)
			cout<<str[j]<<", ";
		if(pos>0)	cout<<str[j];
		cout<<"]"<<endl;
	}
	return 0;
}