

#include <iostream>
using namespace std;


int main()
{
	freopen("E://A-small-attempt1.in","r",stdin);
	freopen("E://yyy.txt","w",stdout);
	int L,D,N;
	scanf("%d %d %d",&L,&D,&N);
	char src[5000][16];
	for(int i=0;i<D;i++)
		scanf("%s",src[i]);
	int t=1;
	while(t<=N)
	{
		char *p=new char[900];
		scanf("%s",p);
		char cmp[15][30];
		int k=0;
		for(int i=0;p[i];i++)
		{
			if(p[i]=='('){
				int v=0;
				for(;p[i]!=')';i++,v++)
				{
					cmp[k][v]=p[i];
				}
				cmp[k][v]='\0';
			}
			else {
				cmp[k][0]=p[i];
				cmp[k][1]='\0';
			}
			k++;
		}
		int sum=0;
		for(int i=0;i<D;i++)
		{
			bool l=true;
			for(int j=0;j<L;j++)
			{
				bool b=false;
				for(int v=0;cmp[j][v];v++)
				{
					if(cmp[j][v]==src[i][j]){
						b=true;
						break;
					}
				}
				if(!b){
					l=false;
					break;
				}
			}
			if(l)sum++;
		}
		delete p;
		cout<<"Case #"<<t<<": "<<sum<<endl;
		t++;
	}
	return 0;
}
