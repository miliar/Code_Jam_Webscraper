#include "stdio.h"
#include "iostream"
#include "string.h"
#include "math.h"
#include "string"
#include "vector"
#include "set"
#include "map"
#include "queue"
#include "list"
#include "stack"

using namespace std;

int len,d,qu;

char dic[5100][20];
char str[1000];
char mp[20][30];
int mpn;
void divide()
{
	int i,j,k;
	for(i=0;i<20;i++)
		for(j=0;j<30;j++)
			mp[i][j]=0;
	i=0;
	j=0;
	k=-1;
	bool flag=0;
	while(str[i]){
		if(str[i]=='('){
			i++;
			k++;
			flag=1;
			continue;
		}
		else if(str[i]==')'){
			i++;
			j=0;
			flag=0;
			continue;
		}
		else{
			if(flag){
				mp[k][j]=str[i];
				j++;
			}
			else{
				k++;
				j=0;
				mp[k][j]=str[i];
			}
			i++;
			continue;
		}
	}
	mpn=k;
	if(mp[mpn][0]!=0) mpn++;
}

int deal()
{
	int start,mapi;
	int cnt=0;
	int dici,pos;
	bool flag;
	for(dici=0;dici<d;dici++){
		flag=0;
		for(start=0;start<=len-mpn;start++){
			for(pos=0;pos<mpn;pos++){
				mapi=0;
				while(mp[pos][mapi]){
					if(mp[pos][mapi]==dic[dici][start+pos])
						break;
					else mapi++;
				}
				if(mp[pos][mapi]==0) break;
			}
			if(pos>=mpn){
				flag=1;
				break;
			}
		}
		if(flag) cnt++;
	}
	return cnt;
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d%d%d",&len,&d,&qu);
	int i;
	for(i=0;i<d;i++){
		scanf("%s",dic[i]);
	}
	for(i=1;i<=qu;i++){
		cout<<"Case #"<<i<<": ";
		scanf("%s",str);
		divide();
		cout<<deal()<<endl;
	}
}