#include<iostream>
#include<algorithm>
#include<set>
#include <math.h>

using namespace std;

int main(){
int n;
cin>>n;
for(int i=0;i<n;i++)
{
	int a,b;
	cin>>a>>b;
	bool checked[b-a+1];
	int total=0;
	for(int j=0;j<b-a+1;j++) checked[j]=false;
	for(int j=0;j<b-a+1;j++)
	{
		if(checked[j]) continue;
		set<int> eqv;
		int current = j+a;
		int ndig=0;
		while(current>0){
			current=current/10;
			ndig++;
		}
		current = j+a;
		eqv.insert(current);
		for(int k=0;k<ndig-1;k++)
		{
			int ldig=current%10;
			current=current/10;
			current+=ldig*pow(10,ndig-1);
			if(ldig==0||current<a||current>b) continue;
			else
			{
				eqv.insert(current);
				checked[current-a]=true;
			}
		}
		int size=eqv.size();
		if(size>0){
			//for (set<int>::iterator it=eqv.begin(); it!=eqv.end(); ++it)
			//cout << " " << *it;
			if(size>=2) total+=size*(size-1)/2;
		}
		
	}
	cout<<"Case #"<<i+1<<":"<<" "<<total<<endl;
}
return 0;
}

