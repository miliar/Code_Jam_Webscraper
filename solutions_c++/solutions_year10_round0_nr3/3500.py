#include <iostream>
#include <list>
#include <fstream.h>
using namespace std;


int main (int argc, char const *argv[]){
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T, casenr;
	in>>T;
	for(casenr=1;casenr<=T;casenr++){
		int R, k, N;
		in>>R>>k>>N;
		list<int> l;
		int i;
		for(i=1;i<=N;i++){
			int temp;
			in>>temp;
			l.push_back(temp);
		}
		long long int sum=0;
		for(i=1;i<=R;i++){
			int pr=0, times=1;
			while(pr+l.front()<=k&&times<=l.size()){
				times++;
				sum+=l.front();
				pr+=l.front();
				l.push_back(l.front());
				l.pop_front();
			}
				
		}
		out<<"Case #"<<casenr<<": "<<sum<<endl;
		//printf("Case #%d: %lld\n", casenr, sum);
	}
	
	return 0;
}