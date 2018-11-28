
#include<stdio.h> 
#include<math.h> 
#include<string.h> 
#include<stdlib.h> 
#include<iostream>

using namespace std;
typedef int Node;

int cmp(const void* t1,const void* t2) { 
	Node * a; /*ָ������Ԫ�����͵�ָ��*/
	Node * b; 
	a = (Node * )t1; 
	b = (Node * )t2; 
	if((*a) < (*b))  return 1; /*��С��������*/
	if((*a) > (*b))  return -1; 
	return 0; 
} 

int main() 
{ 
	int n,p,k,l;
	int a[1002];
	cin >> n;
	for (int ri=1;ri<=n;++ri){
		cin >> p >> k >> l;
		for (int i=0;i<l;++i){
			cin >> a[i];
		}
		cout << "Case #" << ri << ": ";
		if (p*k<l)
		{
			cout << "Impossible" << endl;
			continue;
		}
		qsort(a, l, sizeof(Node), cmp);
		int ans=0;
		int i=0,j=0;
		while(i<l)
		{
			++j;
			int sum=0;
			for ( int ii=0;ii<k && i+ii<l;++ii)
				sum+=a[i+ii];
			ans+=sum*j;
			i=i+k;
		}
		cout << ans << endl;
	}
			
	

//	system("PAUSE");
	return 0;
	
} 


