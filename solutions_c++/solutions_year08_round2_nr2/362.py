#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <fstream>
#include <set>
#include <algorithm>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int T,t;
int a,b,p;
int pr[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997};
int last;
vector<int> vec;

bool isprime(int x) {
	int i;
	for(i=2;i*i<=x;i++)if(x%i==0)return false;
	return true;
}

int main() {
	int i,j,k,ind;
	int ret;
	bool bb;
	ret=0;
	int N=168;
	set<int> s,s1;
	cout<<pr[N-1]<<endl;
	//for(i=2;i<=1000;i++)if(isprime(i)){ret++;}
	//for(i=0;i<pr.size();i++)fout<<pr[i]<<",";
	//fout<<endl;
	//cout<<ret<<endl;
	fin>>T;
	vec.resize(1001);
	for(t=1;t<=T;t++) {
		fin>>a>>b>>p;
		ind=0;
		for(i=0;i<N;i++)if(pr[i]<=p)ind=i;
		//cout<<ind<<" "<<pr[ind]<<endl;
		if(b<a)swap(a,b);
		last=1;
		for(i=a;i<=b;i++) {
			vec[i]=last++;
			s.clear();
			for(j=i-1;j>=a;j--) {
				for(k=ind;k<N;k++) if(pr[k]>=p) {
					if(i%pr[k]==0 && j%pr[k]==0){s.insert(vec[j]);vec[j]=vec[i];break;}
				}
			}
			while(!s.empty()) {
				s1.clear();
				for(j=i-1;j>=a;j--) {
					if(s.find(vec[j])!=s.end()) {
						s1.insert(vec[j]);vec[j]=vec[i];
					}
				}
				s=s1;
			}
		}
		//for(i=a;i<=b;i++)cout<<vec[i]<<" ";cout<<endl;
		ret=0;
		for(i=a;i<=b;i++) {
			bb=false;
			for(j=i-1;j>=a;j--){
				if(vec[j]==vec[i]){bb=true;break;}
			}
			if(!bb)ret++;
		}
		fout<<"Case #"<<t<<": "<<ret<<endl;
	}
	return 0;
}