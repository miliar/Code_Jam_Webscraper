#include <iostream>
#include <string>
using namespace std;
string A[5100], B[510];
bool C[20][300];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int L,D,N,i,j,k,cnt;
	char c;
    scanf("%d%d%d",&L,&D,&N);
    for(i=0;i<D;i++) cin>>A[i];
    for(i=0;i<N;i++) cin>>B[i];
    for(i=0;i<N;i++)
    {
		cnt=0;
		k=0;
		memset(C,false,sizeof(C));
		for(j=0;j<L;j++)
		{
			if (B[i][k]!='(') {C[j][B[i][k]]=true;} else// cout<<j<<" "<<B[i][k]<<endl;} else
			{
				for(;;)
				{
					c=B[i][++k];
					if (c==')') break; else {C[j][c]=true;}// cout<<j<<" "<<c<<endl;}
				}
			}
			k++;
		}
		for(j=0;j<D;j++)
		{
			for(k=0;k<L;k++) if (!C[k][A[j][k]]) break;
			if (k==L) cnt++;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
//	system("pause");
	return 0;
}
