#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <math.h>

using namespace std;

vector<long long int> reverse(vector <long long int> a)
{
	vector <long long int> ans;
	for (int i=a.size()-1; i>=0; i--)
		ans.push_back(a[i]);
	return ans;
}
long long int getMin (int P, int K, vector <long long int> freq)
{

//cout<<P<<"\t"<<K<<"\t"<<freq.size()<<endl;
long long int cost=0;
sort( freq.begin(), freq.end());
freq=reverse(freq);

if (P*K<freq.size()) return -1;

for (int i=0;  i<freq.size(); i++)
{
	cout<<freq[i]<<", ";
}
cout<<endl;
int counter=1;
//cout<<"K is: "<<K<<endl;
for (int i=0;  i<freq.size(); i+=K)
{
	for ( int j=i; j<i+K && j<freq.size(); j++)
{			cost+=counter*freq[j];
	cout<<freq[j]<<"*"<<counter<<"+";
} cout<<"\t";
	//if (i%K==0)
	counter++;
}
//cout<<"Cost: "<<counter;

cout<<endl;
return cost;

}
 int main()
{
	ifstream fin;
	fin.open ("Desktop/A-small-attempt3.in");
	ofstream fout;
	fout.open("Desktop/A-small.out");

	char abc[10];
	
	 int N;
	fin>>N;
	
//N=1;
	for ( int i=0; i<N; i++)
	{
		 int P, K, L;
		vector <long long int> freq;
		
		fin>>P>>K>>L;
		for (int k=0; k<L; k++)
		{
			long  int tmp;
			fin>>tmp;
			freq.push_back(tmp);
		}	
//		cout<<"Main K is: "<<K<<endl;
		long  int ans=getMin(P, K, freq);
		cout<<"Case #"<<i+1<<": "<<ans<<endl; 
		if (ans>=0)
					fout<<"Case #"<<i+1<<": "<<ans<<endl; 
		else
				fout<<"Case #"<<i+1<<": "<<"Impossible"<<endl; 
				
	}			
	
	getchar();
}
