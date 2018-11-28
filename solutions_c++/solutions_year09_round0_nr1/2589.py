#include"iostream.h"
#include"stdio.h"
#include"vector.h"
using namespace std;
int main()
{
	int L,D,N,i,j,k,p,r,m,n,t,sum,count;
	char c[5000][15];
	char s[500];
	FILE *fp;
	int B[500];
	cin>>L>>D>>N;
	fp=fopen("D:\\SM\\result.txt","w");
	vector<vector<int> > A(L,vector<int>(0));
	for(i=0;i<D;i++)   cin>>c[i];
	for(p=0;p<N;p++)
	{
		cin>>s;
		n=strlen(s);
		t=0;  count=0;
		if(n==L)
		{
			for(i=0;i<L;i++) { A[t].push_back((int)s[i]); t++;}
        }
		else
		{   for(i=0;i<n;i++)
			{
				if(s[i]=='(')
				{
					for(j=i+1;j<n;j++)
					{
						if(s[j]<='z'&&s[j]>='a') A[t].push_back((int)s[j]);
						else { m=j; t++; break;}
					}
					i=m;
				}
				else
				{
					A[t].push_back((int)s[i]);
					t++;
				}
			}
		}
		for(i=0;i<D;i++)
		{
			for(j=0;j<L;j++)
			{
				for(k=0;k<A[j].size();k++)
				{
					if((int)c[i][j]==A[j][k]) B[j]=1;
				}
			}
			sum=0;
			for(r=0;r<L;r++)
			{
				sum=sum+B[r];
			}
			if(sum==L) count++;
			memset(B,0,500);
		}
		cout<<"Case #"<<p+1<<": "<<count<<endl;
		fprintf(fp,"Case #%d: %d\n",p+1,count);
        for(i=0;i<L;i++) A[i].clear();
	}
	fclose(fp);
}
