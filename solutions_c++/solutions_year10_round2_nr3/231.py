#include<iostream>
using namespace std;
const int P=100003;
int fmem[510][510];
int cmem[510][510];
bool cmark[510][510]={false};
bool fmark[510][510]={false};
int c(int n,int m)
{
	if(n>m||n<0) return 0;
	if(n==0||n==m) return 1;
	if(cmark[n][m]) return cmem[n][m];
	int res=(c(n,m-1)+c(n-1,m-1))%P;
	cmem[n][m]=res;
	cmark[n][m]=true;
	return res;
}
int f(int n,int num)
{
    if(num<=0||num>=n) return 0;
    if(num==1) return 1;
    if(fmark[n][num]) return fmem[n][num];
    int i,res=0,d=n-num-1;
    int s=num-d-1;
	if(s<1)s=1;
    for(i=s;i<num;i++)
    {
        res=(res+(__int64)f(num,i)*c(num-i-1,d))%P;
    }
    fmem[n][num]=res;
    fmark[n][num]=true;
    return res;
}
int calc(int n)
{
    int i,res=0;
    for(i=1;i<n;i++)
        res=(res+f(n,i))%P;
    return res;
}
int main()
{
    int t,n,cas;
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d",&n);

        printf("Case #%d: %d\n",cas,calc(n));
    }
    return 0;
}
