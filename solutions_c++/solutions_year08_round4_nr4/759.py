#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("D-small-attempt0.in.txt");
  ofstream out("d.out");
#define cin in
#define cout out
#endif


string s;
int k;
int ans;

/*
  È«ÅÅÁĞËã·¨
*/
#define MAXN 100
int count;

void _gen_perm(int* a,int n,int m,int l,int* temp,int* tag){
	int i;
	if (l==m)
	{
		string cur;
		for(int i = 0; i < s.size(); i++)
		{
			int index = i % k;
			cur += s[temp[index]-1 + (i - index)];
		}
		
		int xx = 0;
		for(int i = 0; i < cur.size(); i++)
			if(i == 0 || cur[i] != cur[i-1])
				xx ++;
		if(xx < ans)
			ans = xx;
	}
	else
		for (i=0;i<n;i++)
			if (!tag[i]){
				temp[l]=a[i],tag[i]=1;
				_gen_perm(a,n,m,l+1,temp,tag);
				tag[i]=0;
			}
}

void gen_perm(int n,int m){
	int a[MAXN],temp[MAXN],tag[MAXN]={0},i;
	for (i=0;i<n;i++)
		a[i]=i+1;
	_gen_perm(a,n,m,0,temp,tag);
}




int main()
{
	int cs;
	cin>>cs;
	for(int ct = 1; ct <= cs; ct ++)
	{
		cout << "Case #"<<ct<<": ";
		cin >> k >> s;
		ans = s.size();
		gen_perm(k,k);
		cout << ans << endl;
	}
}
