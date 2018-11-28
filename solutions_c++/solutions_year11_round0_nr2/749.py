#include<iostream>
using namespace std;
char C[40][3];
char D[40][2];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	int i;
	int c;
	int d;
	int n;
	int j = 1;
	cin>>T;
	int k;
	int l;
	while(j <= T)
	{
		char N;
		char temp;
		char result[101];
		int len = 0;
		cin>>c;
		for ( i = 0 ; i < c ; i++)
		{
			cin>>C[i];
		}
		cin>>d;
		for (i = 0 ; i < d ; i++)
		{
			cin>>D[i];
		}
		cin>>n;
		for (i = 0 ; i < n ; i++)
		{
			cin>>N;
			if(len == 0)
			{
				result[0] = N;
				len++;
			}
			else
			{
				bool ischange = false;
				temp = result[len - 1];
				for(l = 0 ; l < c ; l ++)		
				{
					if((temp == C[l][0] && N == C[l][1] )||(temp == C[l][1] && N == C[l][0]))
					{
						result[len-1] = C[l][2];
						ischange = true;
						break;
					}
				}
				if(!ischange)
				{
					result[len] = N;
					len ++;
					for(l = 0; l < d ; l ++)
					{
						for(k = 0; k < len ; k ++)
						{
							temp = result[k];
							if((temp == D[l][0] && N == D[l][1] )||(temp == D[l][1] && N == D[l][0]))
							{
								len = 0;
								break;
							}
						}
					}
				}
			}
		}
		cout<<"Case #"<<j++<<": [";
		if(len > 0)
		{
			cout<<result[0];
			if(len > 1)
			{
				for( i = 1 ; i < len ; i ++)
				{
					cout<<", "<<result[i];
				}
			}
			cout<<"]"<<endl;
		}
		else
		{
			cout<<"]"<<endl;
		}
	}
	return 0;
}