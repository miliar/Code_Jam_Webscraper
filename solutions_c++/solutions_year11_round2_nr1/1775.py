#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

#define F(i,a,b) for(i=a;i<=b;++i)
#define CLR(a) memset(a,0,sizeof(a))

char a[101][111];
int n;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int t,cs=0,i,k;

	cin >> t;
	int den[101],num[101];
	long double wp[101],owp[101],tot,oowp[101],dd,nn;

	while(t--)
	{
		cin >> n; CLR(den); CLR(num);
		F(i,1,n){
			scanf("%s",&a[i][1]);
			F(k,1,n)
				if(a[i][k]!='.'){
					++num[i];
					if(a[i][k]=='1')
						++den[i];
				}
			if(num[i]==0) ++num[i];
		}

		F(i,1,n){
			wp[i] = (long double)(den[i])/(long double)(num[i]);
		//	cout << wp[i] << " " << den[i] << " " << num[i] << endl;
		}

		F(i,1,n){
			owp[i]=0; tot = 0;
			F(k,1,n)
				if(a[i][k]!='.'&&i!=k){
					++tot;
					dd = (long double)(den[k]);
					nn = (long double)(num[k]);

					//printf("(%d %d) - (%d %d)\n",i,k,den[k],num[k]);

					--nn; //if(nn<0.5) ++nn;
					if(a[i][k]=='0') --dd;

					//printf("(%d %d) - (%Lf %Lf)\n",i,k,dd,nn);

					owp[i] += dd/nn;
					//cout << "owp " << i << " " << owp[i] << endl;
				}
			if(tot<0.1) tot = 1;
			owp[i] = owp[i]/tot;
		//	cout << "owp " << owp[i] << endl;
		}

		F(i,1,n){
			oowp[i] = 0,tot = 0;
			F(k,1,n)
				if(a[i][k]!='.'){
					++tot;
					oowp[i] += owp[k];
				}
			if(tot<0.1) tot=1;
			oowp[i] = oowp[i]/tot;
		}

		printf("Case #%d:\n",++cs);
		F(i,1,n)
			printf("%.10Lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);

		//printf("\n\n\n\n");
	}

	return 0;
}