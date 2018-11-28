#include<iostream>
using namespace std;
struct Matrix
{
	int a[2][2];
};
Matrix getm(int b[2][2])
{
		Matrix t;
		t.a[0][0]=b[0][0];
		t.a[0][1]=b[0][1];
		t.a[1][0]=b[1][0];
		t.a[1][1]=b[1][1];
		return t;
}
Matrix mul(Matrix x,Matrix y)
{
		Matrix t;
		int i,j;
		memset(t.a,0,sizeof(t.a));
		for(i=0;i<2;++i)
		{
			for(j=0;j<2;++j)
			{
				t.a[i][j]=(x.a[i][0]*y.a[0][j]+x.a[i][1]*y.a[1][j])%1000;
				while(t.a[i][j]<0)t.a[i][j]+=1000;
			}
		}
		return t;
}
int main()
{
	//freopen("in.txt","r",stdin);
		//freopen("out.txt","w",stdout);
	int t,p=0,n,ans;
	int b[2][2]={28,6,6,2};
	int c[2][2]={6,1,-4,0};
	Matrix che,init;
	for(scanf("%d",&t);t--;)
	{
		che=getm(c);
	    init=getm(b);
		scanf("%d",&n);
		n--;
		while(n)
		{
			if(n&1)init=mul(init,che);
			che=mul(che,che);
			n>>=1;
		}
		ans=init.a[0][1];
		printf("Case #%d: ",++p);
		if(ans==0)printf("999\n");
		else if(ans>100)printf("%d\n",ans-1);
		else if(ans<101&&ans>10)printf("0%d\n",ans-1);
		else if(ans<11&&ans>0)printf("00%d\n",ans-1);
	}
	return 0;
}