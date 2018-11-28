#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <cmath>
#include <list>
#include <vector>

using namespace std;

const int maxn = 1000;
int numbers[maxn];
int n;
string line;
int low, high, digits;

void read() {
	scanf("%d",&low);
	scanf("%d",&high);

//	printf("n:%d\n",n);
//	for (int i=0;i<n;i++)
//	{
//		scanf("%d", &numbers[i]);	
//printf("i:%d numbers[i]:%d\n",i,numbers[i]);
//	}

}

int process()
{
	int hits = 0;
	int lowlim = pow(10,digits-1);
	int highlim = pow(10,digits)-1;	
	int diglow = floor(log10(low))+1;
	int dighigh = floor(log10(high))+1;
	vector<int>used(2000000,0);
	//cout<<"low, high, diglow, dighigh:"<<low<<" "<<high<<" "<<diglow<<" "<<dighigh<<endl;
	//cout<<"lowlim, highlim "<<lowlim<<" "<<highlim<<endl;
	if(lowlim>high)
		return 0;
	if(highlim<low)
		return 0;
	if(diglow==digits)
		lowlim = low;
	if(dighigh==digits)
		highlim = high;
//	cout<<"testing from "<<lowlim<<" to "<<highlim<<endl;
	list<int>mylist;
	int d,val,temp;	
	list<int>::iterator it=mylist.begin();	
	for(int k=lowlim;k<=highlim;k++)
	{
		if(used[k]==0)
		{		
		mylist.clear();
		mylist.push_back(k);
		used[k]=1;
		val=k;
		for(d=0;d<digits;d++)
		{
			temp = val%10;
			val = val-temp;
			val = val/10;
			val = val+temp*pow(10,digits-1);
			if(val<=highlim && val>=lowlim)
			{
				mylist.push_back(val);
				used[val]=1;
			}
		}
		mylist.sort();
//		cout << "mylist contains:";
//		for (it=mylist.begin(); it!=mylist.end(); ++it)
//    			cout << " " << *it;
//		cout << endl;
		mylist.unique();
//		cout << "post unique mylist contains:";
//		for (it=mylist.begin(); it!=mylist.end(); ++it)
//    			cout << " " << *it;
//		cout << endl;
		hits+= .5*(mylist.size())*(mylist.size()-1);
		}
	}

	return hits;
}

int main()
{
	int i,t;
	int k;
	int count;
	scanf("%d",&t);
	getline(cin,line);
	for(i = 1; i<=t; i++)
	{
		count = 0;
		printf("Case #%d: ", i);
		read();
//		cout<<low<<" to "<<high;

		for(digits=2; digits<8;digits++)
			count += process();		
		
		cout<<count;
		printf("\n");
	}
	return 0;
}
