#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;
double wp[101],owp[101],oowp[101],rpi,tmp1,tmp2,wp1,tmp11,tmp22;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n;
    char ch;
    int a[101][101];
	scanf("%d",&t);
	for(int z=1; z<=t; z++){
	scanf("%d",&n);
	for (int i=0; i<n;i++){
		for (int j=0; j<n;j++){
			cin>>ch;			
			if (ch=='1') a[i][j]=1;
			if (ch=='0') a[i][j]=0;
			if (ch=='.') a[i][j]=-1;
			}
		}
	printf("Case #%d:\n",z);
	for (int i=0; i<n;i++){
	tmp1=count(a[i],a[i]+n,1);
	tmp2=count(a[i],a[i]+n,0);
	wp[i]=tmp1/(tmp1+tmp2);
	}
	for (int i=0; i<n;i++){
		tmp1=0.0;
		tmp2=0.0;
		for (int j=0; j<n;j++){
			if (a[i][j]!=-1){
						tmp11=count(a[j],a[j]+n,1);
						tmp22=count(a[j],a[j]+n,0);
						if (a[i][j]==1) tmp22--;
						if (a[i][j]==0) tmp11--;
						wp1=tmp11/(tmp11+tmp22);
				tmp1+=wp1;
				tmp2++;}
			owp[i]=tmp1/tmp2;
			
			}
		}
	for (int i=0; i<n;i++){
		tmp1=0.0;
		tmp2=0.0;
		for (int j=0; j<n;j++){
			if (a[i][j]!=-1){
				tmp1+=owp[j];
				tmp2++;}
			oowp[i]=tmp1/tmp2;
			}
		}
	for (int i=0; i<n;i++){
		rpi=0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
		printf("%.12lf\n",rpi);}
	
	
	
	}
    return 0;
}
