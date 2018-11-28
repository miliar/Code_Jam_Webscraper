#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]){
	int i,j;
	ifstream in("C-small.in");
	ofstream out("C-small.out");
	int T,R,k,N,count,money,begin,end,run;
	
	int g[1000];
	in>>T;
	for (i=0;i<T;i++){
		money = 0;
		run = 0;
		in>>R>>k>>N;
		for (j=0;j<N;j++) {
			in>>g[j];
		}
		begin=0;end = 0;
		
		while(run<R){
			count = 0;
			while (count + g[end] <= k) {
				count += g[end];
				end = (end + 1) % N;
				if (end == begin)
					break;
			}
			begin = end;
			money += count;
			run++;
		}
		out<<"Case #"<<i+1<<": "<<money<<endl;
	}

}