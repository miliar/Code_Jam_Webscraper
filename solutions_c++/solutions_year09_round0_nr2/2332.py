#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
using namespace std;
char val,b[200][200];
int a[200][200],h,w;
void initial(int x,int y)
{
	int flag=0,sm=a[x][y];
	if (x-1>=0 && a[x-1][y]<sm) {sm=a[x-1][y];flag=1;}
	if (y-1>=0 && a[x][y-1]<sm) {sm=a[x][y-1];flag=2;}
	if (y+1<w && a[x][y+1]<sm) {sm=a[x][y+1];flag=3; }
	if (x+1<h && a[x+1][y]<sm) {sm=a[x+1][y];flag=4; }
	if (flag==0) {b[x][y]=val; val++;}
	else if (flag==1) {b[x][y]=val; initial (x-1,y);}
	else if (flag==2) {b[x][y]=val; initial (x,y-1);}
	else if (flag==3) {b[x][y]=val; initial (x,y+1);}
	else if (flag==4) {b[x][y]=val; initial (x+1,y);}	
}
char basin(int x,int y)
{
	int flag=0,sm=a[x][y];
	if (b[x][y]>='a' && b[x][y]<='z') return(b[x][y]);
	if (x-1>=0 && a[x-1][y]<sm) {sm=a[x-1][y];flag=1;}
	if (y-1>=0 && a[x][y-1]<sm) {sm=a[x][y-1];flag=2;}
	if (y+1<w && a[x][y+1]<sm) {sm=a[x][y+1];flag=3; }
	if (x+1<h && a[x+1][y]<sm) {sm=a[x+1][y];flag=4; }
	if (flag==0) {b[x][y]=val; val++;}
	else if (flag==1) {b[x][y]=basin(x-1,y);}
	else if (flag==2) {b[x][y]=basin(x,y-1);}
	else if (flag==3) {b[x][y]=basin(x,y+1);}
	else if (flag==4) {b[x][y]=basin(x+1,y);}	
	return (b[x][y]);
}
int main()
{
	int T;
	FILE * rf=fopen("B-large.in","r");
	FILE * wf=fopen("bsans.in","w");
	fscanf (rf,"%d",&T);
	for (int i=0;i<T;i++)
	{
		fscanf (rf,"%d%d",&h,&w);
		for (int j=0;j<h;j++) for (int k=0;k<w;k++) {fscanf (rf,"%d",&a[j][k]); b[j][k]='0';}
		b[0][0]='a';
		val='a';
		initial(0,0);
		fprintf (wf,"Case #%d:\n",i+1);
		for (int j=0;j<h;j++){ for (int k=0;k<w;k++) {if (b[j][k]<'a' || b[j][k]>'z') b[j][k]=basin(j,k); fprintf (wf,"%c ",b[j][k]);} fprintf (wf,"\n");}
	}
	return 0;
}
