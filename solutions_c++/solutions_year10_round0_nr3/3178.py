#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("in1.txt");
ofstream fout("out.txt");

const int dim = 1000;
int mas[dim];
int next[dim];
int sum[dim];
int zap[dim];
int n, k, r, t;

void nextpos(int firstpos){
	int s = 0;
	int zahod = 0;
	int i = firstpos;
	int cur = 0;
	int usedgroups = 0;
	while (i<n){
		if (cur+mas[i]<=k&&usedgroups<=n){
			cur = cur+mas[i];
			usedgroups++;
		}
		else if(usedgroups<n) {
			s = s+cur;
			cur=mas[i];
			zahod++;
			usedgroups=0;
		}
		i++;
	}

	i=0;
	zahod++;
	while (cur+mas[i]<=k&&usedgroups<n){
		cur = cur+mas[i];
		i++;
		usedgroups++;
	}
	s = s+cur;
	next[firstpos] = i;
	sum[firstpos] = s;
	zap[firstpos] = zahod;
}

int main(){

	fin>>t;
	
	for (int j=0;j<t;j++){
fin>>r>>k>>n;
	for (int i=0;i<n;i++)
	fin>>mas[i];

	 int no = 0;

	for (int i=0;i<n;i++)
		nextpos(i);

	int s = 0;
	int amount = 0;
	int first = 0;

	bool flag = true;
	while (amount<r){
		if (amount+zap[first]<=r&&flag){
			amount = amount + zap[first];
			s = s + sum[first];
			first = next[first];
		}
		else if (amount<r){
			flag = false;
			int cur = 0;
			while (cur<=k&&cur+mas[first]<=k){
				cur = cur + mas[first];
				first++;
			}
			s = s + cur;
			amount++;
		}
	}

	fout<<"Case #"<<j+1<<": "<<s<<endl;
	}	
/*
	for (int i=0;i<n;i++)
		cout<<i<<"  "<<next[i]<<"  "<<sum[i]<<"  "<<zap[i]<<endl;
*/
return 0;
}