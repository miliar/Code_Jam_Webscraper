#include<iostream.h>
#include<conio.h>
#include<string.h>
void main()
{
	int L,D,N,match[500],r,c;
	char word[5000][16],token[425];
	cin>>L;
	cin>>D;
	cin>>N;
	for(int i=0;i<D;i++)
	{
		cin>>word[i];
	}
	for(i=0;i<N;i++)
	{
		match[i]=0;
		cin>>token;
		for(int k=0;k<D;k++)
		{
			r=0;
			for(int j=0;j<strlen(token);)
			{
				c=0;
				if(token[j]=='(')
				{
					j++;
					while(token[j]!=')')
					{
						if(token[j]==word[k][r]&&c==0)
						{
							c=1;r++;
						}
						j++;
					}
					j++;
				}
				else
				{
					if(token[j]==word[k][r])
					{
						c=1;r++;
					}
					j++;
				}
				if(c==0)
					break;
			}
			if(c)
				match[i]++;
		}
	}
	for(i=0;i<N;i++)
	{
		cout<<"Case #"<<i+1<<": "<<match[i]<<"\n";
	}
}

