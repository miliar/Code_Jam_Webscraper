#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;
const int MAXN = 1000;

int t,r,k,n;
int g[MAXN],next[MAXN];
long long sum[MAXN];

int main(){
	ifstream fin("test.in");
	ofstream fout("test.out");
	fin>>t;
	for(int time=0;time<t;++time){
		fin>>r>>k>>n;
		for(int i=0;i<n;++i){
			fin>>g[i];
		}
		for(int i=0;i<n;++i){
			int j = (i+1)%n;
			sum[i] = g[i];
			while(sum[i]+g[j]<=k && j!=i){
				sum[i]+=g[j];
				j = (j+1)%n;
			}
			next[i] = j;
		}
		long long total = 0;
		int pos = 0;
		for(int i=0;i<r;++i){
			total+=sum[pos];
			pos = next[pos];
		}
		fout<<"Case #"<<time+1<<": "<<total<<endl;
		cout<<time+1<<endl;
	}
}