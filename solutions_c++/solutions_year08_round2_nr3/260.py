#include<iostream>
#include<cstdio>
#include<vector>
#include<stdio.h>

using namespace std;
int main()
{
	int t,c;
	long long int m,n,i,a1,index;
	long long int pre,pos,dif;
	
	FILE *f1,*f2;
	f1=fopen("C-small.in","r");
	f2=fopen("C-small.out","w");
	
	fscanf(f1,"%d\n",&t);
	c=1;
	while(t--)
	{
		fscanf(f1,"%lld\n",&n);
		vector < long long int > v;
		vector < long long int > ans;
		int a[n];
		
		for(i=1;i<=n;i++)
		v.push_back(i);
		
		vector <long long int> :: iterator i1 = v.begin();
		
		m=n;
		pos=0,pre=0;	
		for(i=0;i<n;i++)
		{
			pre=pos;
			pos=(pos+i)%m;
			dif=pos-pre;
			
			i1=i1+dif;
			a[*(i1)-1 ]=i+1;
			v.erase(i1);
			m--;
		}
		
		fscanf(f1,"%lld\n",&index);
		for(i=0;i<index;i++)
		{
			fscanf(f1,"%lld\n",&a1);
			ans.push_back(a[a1-1]);
		}
		
		
		fprintf(f2,"Case #%d:",c);
		for(i=0;i<index;i++)
		fprintf(f2," %lld",ans[i]);
		fprintf(f2,"\n");
		
		c++;
		
	}
	fclose(f1);
	fclose(f2);
	return 0;
}	 
				
		
		
