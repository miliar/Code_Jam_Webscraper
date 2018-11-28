#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool visit[1100];
long long group[1100];
long long ng;
long long r;
long long k;
long long num[1100];
long long com[1100];
long long test;
int main(){
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");
	long long t;
	ifs>>t;
	test = 1;
	while(t--){
		ifs>>r>>k>>ng;
		long long tt = 0;
		long long cc = 0;
		for(long long i = 0; i != ng; ++i){
			ifs>>group[i];
			num[i] = 0;
			visit[i] = false;
		}
		long long p = 0;
		
		while(visit[p] == false){
			visit[p] = true;
			com[p] = cc;
			long long a = 0;
			long long beg = p;
			while(1){
				a += group[p];
				if(a > k){
					a -= group[p];
					break;
				}
				p = p + 1;
				if(p == ng)
					p = 0;
				if(beg == p)
					break;
			}
			tt += a;
			num[cc++] = tt;
		}
		
		
		long long g = 0;
		if(p != 0){
			long long temp = r - com[p];
			long long lenr = cc - com[p];
			long long round = temp / lenr;
			long long left = temp % lenr;
			g += round * (num[cc-1] - num[com[p] - 1]) + num[com[p] - 1];
			if(left != 0)
				g += num[com[p] + left - 1] - num[com[p]-1];
		}else{
			long long round = r / cc;
			long long left = r % cc;
			g += round * num[cc-1];
			if(left != 0)
				g += num[left - 1];
		}
		ofs<<"Case #"<<test<<": "<<g<<endl;
		++test;
	}
	return 0;
}