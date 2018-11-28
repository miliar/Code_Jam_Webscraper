#include <iostream>
using namespace std;

char com[40][5];
char opp[30][5];
char inv[110];
char res[110];

int main()
{
	freopen("pb.in", "r", stdin);
	freopen("pb.out", "w", stdout);

	int T,t;
	int n,c,d;
	int i,j,k,len;

	cin>>T;
	for(t=1; t<=T; t++)
	{
		cin>>c;
		for(i=0; i<c; i++)
		{
			cin>>com[i];
		}

		cin>>d;
		for(i=0; i<d; i++)
		{
			cin>>opp[i];
		}

		cin>>n>>inv;

		memset(res, 0, sizeof res);
		res[0]=inv[0];
		len=1;

		for(i=1; i<n; i++)
		{
			res[len++]=inv[i];
			if(len>1)
			{
				for(j=0; j<c; j++)
				{
					if((com[j][0]==res[len-1] && com[j][1]==res[len-2]) || (com[j][1]==res[len-1] && com[j][0]==res[len-2]))
					{
						res[len-2]=com[j][2];
						len--;
						break;
					}
				}
				for(j=0; j<d; j++)
				{
					if(opp[j][0]==res[len-1])
					{
						for(k=0; k<len-1; k++)
						{
							if(res[k]==opp[j][1])
							{
								len=0;
								break;
							}
						}
						if(k!=len)
							break;
					}
					if(opp[j][1]==res[len-1])
					{
						for(k=0; k<len-1; k++)
						{
							if(res[k]==opp[j][0])
							{
								len=0;
								break;
							}
						}
						if(k!=len)
							break;
					}
				}
			}
		}

		cout<<"Case #"<<t<<": [";
		if(len>0)
			cout<<res[0];
		for(i=1; i<len; i++)
			cout<<", "<<res[i];
		cout<<"]"<<endl;
	}
	return 0;
}
