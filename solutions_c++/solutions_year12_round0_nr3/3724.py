#include<iostream>
#include<map>
#include<stdio.h>
#include<string.h>
#include<set>
using namespace std;
bool menor(char *A,int a,char*B,int b)
{
	if(a<b)return 1;
	if(a>b)return 0;
	for(int i=0;i<a;i++){
		if(A[i]<B[i])return 1;
		else if(A[i]>B[i])return 0;
			}
	return 0;
}
bool check(char *A,int a,char *X,int x,char *Y,int y,char *B)
{
	if(B[0]=='0')return 0;
	if(!menor(A,a,B,a))return 0;
	if(!menor(B,a,Y,y))return 0;
	if(!menor(X,x,B,a))return 0;
	return 1;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	scanf("%d\n",&n);
	
	char A[1000];
	char X[100],Y[100];
	char B[100];
	//gets(A);
	for(int x=1;x<=n;x++)
	{
		int a,b;
		cin>>a>>b;
		sprintf(X,"%d",a-1);
		sprintf(Y,"%d",b+1);
		int u,v;
		u=strlen(X);
		v=strlen(Y);
		long long res=0;
		
		for(int i=a;i<=b;i++)
		{
			sprintf(A,"%d",i);
			int q=strlen(A);
			set<int>S;
			for(int j=1;j<=q-1;j++)
			{
				
				for(int h=0;h<j;h++)B[h]=A[h+q-j];
				for(int h=j;h<q;h++)B[h]=A[h-j];
				B[q]=A[q];
				int s=0;
				for(int i=0;i<q;i++)
				{
					s=10*s+(int)(B[i]-'0');
				}
				if(S.count(s))continue;
				S.insert(s);
			//	cout<<(string)A<<" "<<(string)B<<endl;cout<<check(A,q,X,u,Y,v,B)<<endl;
				if(check(A,q,X,u,Y,v,B))res++;
			}
		}
		cout<<"Case #"<<x<<": ";cout<<res;cout<<endl;
	}
	return 0;
}