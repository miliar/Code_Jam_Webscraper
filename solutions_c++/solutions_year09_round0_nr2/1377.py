#include<cstdio>
#include<cstring>

char label(int A[][102], int L[][102], int x, int y,int &h, int &w,char &u)
{
if(L[x][y]!=0) return L[x][y];
int dh[]={1,0,0,-1};
int dw[]={0,1,-1,0};
int ma=10000,mp=-1;

for(int j=0;j<4;j++)
{
	int nh=x+dh[j];
	int nw=y+dw[j];
	if(nh<0 || nw<0 || nh>=h || nw>=w || A[nh][nw]>=A[x][y]) continue;
	if(A[nh][nw]<=ma) {ma=A[nh][nw]; mp=j; }	
}
if(mp==-1) // a sink 
{
L[x][y]=u++;
return L[x][y];
}
else
{
L[x][y]=label(A,L,x+dh[mp],y+dw[mp],h,w,u);
return L[x][y];
}

}

int main()
{
int num,h,w,A[102][102];
scanf("%d",&num);

for(int i=0;i<num;i++)
{
scanf("%d %d",&h,&w);

	for(int j=0;j<h;j++)
	for(int k=0;k<w;k++)
	scanf("%d",&A[j][k]);

int L[102][102]={0};
char u='a';

for(int j=0;j<h;j++)
for(int k=0;k<w;k++)
if(L[j][k]==0)
label(A,L,j,k,h,w,u);

printf("Case #%d:\n",i+1);

for(int j=0;j<h;j++)
{
for(int k=0;k<w;k++)
if(k==0) printf("%c",L[j][k]);
else printf(" %c",L[j][k]);
printf("\n");
}


}

return 0;
}

