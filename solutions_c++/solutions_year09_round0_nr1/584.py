#include<iostream>
using namespace std;
char data[5000][15];
int check[5000];
int cand[26];

int cmp(const void *a ,const void *b)
{
	return strcmp((char*)a,(char*)b);
}

int main()
{
	int l,d,n;
	while(cin>>l>>d>>n)
	{
		for(int i=0;i<d;i++)
			cin>>data[i];
		qsort(data,d,sizeof(data[0]),cmp);
		for(int k=0;k<n;k++)
		{
			char qur[26*15+6];
			cin>>qur;
			int p=0,q=0;
			for(int i=0;i<strlen(qur);i++)
			{
				if(qur[i]==')')
				{
					/*for(int j=0;j<26;j++)
						if(cand[j] == 1)
							cout<<(char)(j+'a')<<" ";
					cout<<endl;*/
					for(int j=0;j<d;j++)
					{
						if(check[j] == 0 && cand[data[j][p]-'a'] == 1)
							check[j] = 0;
						else
							check[j]=1;
					}
					for(int j=0;j<26;j++)
						cand[j]=0;
					q=0;
					p++;
				}
				else if(q == 0 && qur[i] != '(')
				{
					//cout<<"x"<<endl;
					for(int j=0;j<d;j++)
					{
						if(check[j] == 0 && data[j][p] == qur[i])
							check[j] = 0;
						else
						{
							//cout<<check[j]<<" "<<data[j][p]<<" "<<qur[i]<<endl;
							check[j]=1;
						}
					}
					p++;
				}
				else if(qur[i] == '(')
					q=1;
				else if(q == 1)
					cand[qur[i]-'a']=1;
					
			}
			int sum=0;
			for(int i=0;i<d;i++)
			{
				if(check[i] == 0)
				{
					//cout<<data[i]<<endl;
					sum++;
				}
				check[i]=0;
			}
			cout<<"Case #"<<k+1<<":";
			cout<<" "<<sum<<endl;
		}
	}
	return 0;
}
