#include <iostream>
using namespace std;
char strC[100][10];
char strD[100][10];
char matC[300][300];
char matD[300][300];
char str[200];
char res[200];
int main()
{
	int T,i,j,k,C,D,N;
	int nn,nnt;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for(i=1;i<=T;++i)
	{
		memset(matC,0,sizeof(matC));
		memset(matD,0,sizeof(matD));
	
		cin>>C;
		for(j=0;j<C;++j)
		{
			cin>>strC[j];
			matC[strC[j][0]][strC[j][1]]=strC[j][2];
			matC[strC[j][1]][strC[j][0]]=strC[j][2];
		}
		cin>>D;
		for(j=0;j<D;++j)
		{
			cin>>strD[j];
			matD[strD[j][0]][strD[j][1]]=1;
			matD[strD[j][1]][strD[j][0]]=1;
		}
		cin>>N;
		cin>>str;
		nn=0;
		for(j=0;j<N;++j)
		{
			if(nn==0)
			{
				res[nn++]=str[j];
				continue;
			}
			if(matC[str[j]][res[nn-1]]!=0)
			{
				res[nn-1]=matC[str[j]][res[nn-1]];
				continue;
			}
			nnt=0;
			for(k=0;k<nn;++k)
			{
				if(matD[str[j]][res[k]]!=0)
				{
					nnt=1;
					nn=0;
					break;
				}
			}
			if(nnt==0)
				res[nn++]=str[j];
			
		}
		cout<<"Case #"<<i<<": "<<'[';
		for(j=0;j<nn;++j)
		{
			if(j==0)
				cout<<res[j];
			else
				cout<<", "<<res[j];
		}
		cout<<']'<<endl;
	}
	return 0;
}