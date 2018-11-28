#include<iostream>
#include<map>
#include<stdio.h>
#include<string.h>
#include<set>
using namespace std;
string in=  "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string out= "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	map<char,char>M;
	set<char>S;
	for(int i=0;i<in.size();i++)M[in[i]]=out[i],S.insert(out[i]);
	cerr<<M.size()<<endl;
	for(char x='z';x>='a';x--)if(!M.count(x))
	{
		for(char y='a';y<='z';y++)if(!S.count(y)){M[x]=y;cerr<<x<<" "<<M[x];S.insert(y);break;}
	}
	cerr<<M.size()<<endl;
	//cout<<M.size()<<endl;
	int n;
	scanf("%d\n",&n);
	
	char A[1000];
	//gets(A);
	for(int x=1;x<=n;x++)
	{
		gets(A);
		int a=strlen(A);
		cout<<"Case #"<<x<<": ";
		for(int i=0;i<a;i++)cout<<M[A[i]];cout<<endl;
	}
	return 0;
}