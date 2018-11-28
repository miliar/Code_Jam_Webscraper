#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<vector>
#include <iomanip>
#include<cmath>
using namespace std;
float p[100001];
float part1[100001];
float part2[100001];
float list[100005];
float ans[100001];
int power[4]={1,2,4,8};
int main()
{
	int T,a,b; cin>>T;
	for(int i=0; i< T; i++)
	{
		cin>>a>>b;
		for(int j=0; j<a; j++)
		{ cin>>p[j];}
//		part1[a-1]=p[a-1];

		part2[0]=p[0];	
//		cout<<p[0];			
//		for(int k=a-2; k>=0; k--) {part1[k]=p[k]+part1[k+1];}	
//		cout<<(p[1]);
		for(int k=1; k<a; k++) {part2[k] = part2[k-1]*p[k];}
//		for(int l=0; l<a;l++) {cout<<part2[l]<<endl; }
		int s=0;
		while(s<=a+1)
		{
			if(s==a+1)
			{list[s] = b+2;}
			else if(s==a)
			{list[s] = a+b+1;}
			else
			{list[s] = ((part2[a-s-1]* (b-a+1 + 2*s)) + (1-part2[a-s-1])*(b+1+b-a+1 + 2*s)) ;
//						cout<<endl<<(part2[a-s-1]* (b-a+1 + 2*s))<<' '<<(1-part2[s-1])*(b+1+b-a+1 + 2*s)<<' ';
			}
			//(power[a-s-1] -1)*
			//cout<<s<<' '<<list[s];
			s++;
		}
		float qw=list[0];
		for(int j=0; j<= a+1; j++)
		{ if(qw>list[j]) qw=list[j];}
		  cout.precision(5);
		cout<<"Case #"<<(i+1)<<": ";cout<<setprecision (6) <<qw<<endl;
	}
/*for(int i=0;i<;i++0){}
*/	
}
