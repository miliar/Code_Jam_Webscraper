#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<cmath>
#include<string>
using namespace std;

const int len = 150;
int d[len];

int cmpnum(char a[],char b[])
{
	int i,na = strlen(a),nb = strlen(b);
	if(na!=nb)return na-nb;
	for(i=0;i<nb;i++)
	{
		if(a[i]!=b[i])return a[i]-b[i];
	}
	return 0;
}
void mul(char *a,char *b,char *c)
{
	int i,j,na=strlen(a),nb=strlen(b);
	for(i=0;i<=na+nb;i++)d[i]=0;
	for(i=na-1;i>=0;i--)
	{
		for(j=nb-1;j>=0;j--)
		{
			d[na+nb-2-i-j]+=(a[i]-'0')*(b[j]-'0');
		}
	}
	for(i=0;i<na+nb;i++)
	{
		d[i+1]+=d[i]/10;
		d[i]%=10;
	}
	j=na+nb-1;
	if(d[j]==0)j--;
	for(i=0;j>=0;j--,i++)c[i]=d[j]+'0';
	c[i]='\0';
	int nc=strlen(c);
	for(i=0;i<nc-1&&c[i]=='0';i++);
	for(j=0;i<=nc;i++)c[j++]=c[i];
}

void sub(char *a,char *b,char *c)
{
	int i,j,na=strlen(a),nb=strlen(b);
	int mn=na;
	for(i=0;i<mn;i++)d[i]=0;
	for(i=na-1;i>=0;i--)d[na-1-i]+=a[i]-'0';
	for(i=nb-1;i>=0;i--)d[nb-1-i]-=b[i]-'0';
	for(i=0;i<mn;i++)
	{
		if(d[i]<0)
		{
			d[i+1]--;
			d[i] += 10;
		}
	}
	j=mn-1;
	while(j-1>=0 && d[j]==0)j--;
	for(i=0;j>=0;j--,i++)c[i]=d[j]+'0';
	c[i]='\0';
}
//div四个参数要独立
void div(char a[],char b[],char c[],char r[])
{
	strcpy(r,a);
	char tmp[len];
	int i,j,k = 0;
	int na = strlen(a),nb = strlen(b);
	r[nb] = '\0';
	c[0] = '0',c[1] = '\0';
	for(i=nb-1;i<na;i++)
	{
		char cl = '0',cr = '9';
		while(cl<=cr)
		{
			char mid = (cl+cr)/2;
			tmp[1] = '\0';
			tmp[0] = mid;
			mul(tmp,b,tmp);
			if(cmpnum(tmp,r)<=0)cl = mid+1;
			else cr = mid-1;
		}
		c[k++] = cr;
		c[k] = '\0';
		if(c[0]=='0')k--;

		tmp[1] = '\0';
		tmp[0] = cr;
		mul(tmp,b,tmp);
		sub(r,tmp,r);

		j = strlen(r);
		if(r[0]=='0')j--;
		r[j] = a[i+1];
		r[j+1] = '\0';
	}
	if(r[0]=='\0')r[1] = '\0',r[0] = '0';
}

void add(char *a,char *b,char *c)
{
	int i,j,na=strlen(a),nb=strlen(b);
	int mn=na>nb?na:nb;
	for(i=0;i<mn+1;i++)d[i]=0;
	for(i=na-1;i>=0;i--)d[na-1-i]+=a[i]-'0';
	for(i=nb-1;i>=0;i--)d[nb-1-i]+=b[i]-'0';
	for(i=0;i<mn;i++)
	{
		d[i+1]+=d[i]/10;
		d[i]%=10;
	}
	j=mn-1;
	if(d[j+1]>0)j++;
	for(i=0;j>=0;j--,i++)c[i]=d[j]+'0';
	c[i]='\0';
}

int n;
char tnum[1005][len],num[1005][len],nn[len],c[len],r[len];

void gcd(char a[],char b[]){
	if(cmpnum(b,"0")==0)strcpy(nn,a);
	else{
		div(a,b,c,r);
		strcpy(c,b);
		strcpy(b,r);
		strcpy(a,c);
		gcd(a,b);
	}
}

int ind[1005];
bool cmp(int x,int y){
	if(cmpnum(num[x],num[y])<0)return true;
	return false;
}
int main(){
	//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int i,j,k,t,nc = 0;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		int tn = n;
		for(i = 0;i<n;i++){
			scanf("%s",num[i]);
			strcpy(tnum[i],num[i]);
			ind[i] = i;
		}
		sort(ind,ind+n,cmp);
		for(i = 0;i<n;i++){
			strcpy(num[i],tnum[ind[i]]);
		}
		for(i = 1;i<n;i++){
			if(cmpnum(num[i],num[0])>0){
				sub(num[i],num[0],num[i]);
			}else{
				sub(num[0],num[i],num[i]);
			}
		}
		for(i = 1,j = 1;i<n;i++){
			if(strcmp("0",num[i])!=0){
				strcpy(num[j++],num[i]);
			}
		}
		n = j;
		if(n==1){
			printf("Case #%d: 0\n",++nc);
			continue;
		}
		for(i = 2;i<n;i++){
			gcd(num[1],num[i]);
			strcpy(num[1],nn);
		}
		div(num[0],num[1],c,r);
		sub(num[1],r,nn);
		if(strcmp(r,"0")==0)strcpy(nn,"0");
		printf("Case #%d: %s\n",++nc,nn);
	}
    return 0;
}