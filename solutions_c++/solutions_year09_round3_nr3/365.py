#include<iostream>
#include<conio.h>
#include<vector>
#include<map>
#include<algorithm>
#include<string>
#include<math.h>
#define max 1000

using namespace std;

int n,q;
vector<int> order;

int solve(void){

	int i,j;
	int count=0;
	int mark[max];
	for(i=0;i<max;i++)
		mark[i]=1;

	for(i=0;i<q;i++){

		int r,s;
		r=order[i];
		s=order[i]-2;
		mark[order[i]-1]=0;

		while(r<n && mark[r]!=0){
			count++;
			r++;
		}
		while(s>=0&&mark[s]!=0){
			count++;
			s--;
		}
	}
	
	return count;
}

int main(void){

	
	freopen("b.txt","r",stdin);
  freopen("output.txt","w",stdout);
	int cases,c;

	cin>>cases;

	for(c=0;c<cases;c++){
		int i,j;
		order.clear();

		cin>>n;
		cin>>q;
		int min=9999999;
		for(i=0;i<q;i++){
			cin>>j;
			order.push_back(j);
		}
		do{
			int temp;
			temp=solve();
			if(temp<min)
				min=temp;
		}
	while ( next_permutation(order.begin(),order.end()) );

	cout<<"Case #"<<c+1<<": ";
	cout<<min<<endl;
	
	}
	getch();
	return 0;
}