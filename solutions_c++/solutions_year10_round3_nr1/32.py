#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
using namespace std;
const int maxn=1010;

struct Node{
	int a,b;
	bool operator<(const Node &other)const{
		return b<other.b;
	}
} node[maxn];

int n;
int total;
int num[maxn];
int tmp[maxn];

void MergeSort(int l,int r)
{
	if(r>l){
		int mid=(l+r)/2;
		MergeSort(l,mid);
		MergeSort(mid+1,r);
		int i=l,j=mid+1,k=l;
		while(i<=mid && j<=r){
			if(num[i]>num[j]){
				tmp[k++]=num[j++];
				total+=mid-i+1;
			}
			else tmp[k++]=num[i++];
		}
		while(i<=mid)
			tmp[k++]=num[i++];
		while(j<=r)
			tmp[k++]=num[j++];
		for(i=l;i<=r;i++)
			num[i]=tmp[i];
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,ca,i;
	cin>>t;
	for(ca=1;ca<=t;ca++){
		cin>>n;
		for(i=0;i<n;i++)
			cin>>node[i].a>>node[i].b;
		sort(node,node+n);
		for(i=0;i<n;i++)
			num[i]=node[i].a;
		total=0;
		MergeSort(0,n-1);
		cout<<"Case #"<<ca<<": "<<total<<endl;
	}
	return 0;
}