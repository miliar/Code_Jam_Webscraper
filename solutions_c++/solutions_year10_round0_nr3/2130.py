#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
class Queue{
	public:
		long long N;
		vector<long long> list;
		long long cur;
		long long getmax(long long R,long long& group){
			long long pos = cur;
			long long num = 0;
			while(1){
				num += list[pos];
				if(num > R){
					num -= list[pos];
					cur = pos;
					return num;
				}
				//cout << "num" << num << "R" << R << endl;
				pos++;
                group++;

				if(pos >= N) pos = 0;
				if(pos == cur) return num;
			}
		}
};
long long solve(long long R,long long k,long long N,vector<long long>& list)
{
	long long rt = 0;
	long long totalR = R;
	Queue q;
	q.N = N;
	q.list = list;
	q.cur = 0;
	long long group = 0;
	while(R > 0){
		rt += q.getmax(k,group);
		R--;
        //cout << group << endl;
		group %= N;
		if(group == 0){
		    long long usedR = totalR - R;
		    long long getm = rt;
		    //cout << usedR << " " << getm << endl;
		    while(R > usedR){
		        R -= usedR;
		        rt += getm;
		        //cout << "here" << endl;
		    }
		}
	}
	return rt;
}
int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");

	long long C;
	in >> C;
	long long  R,k,N;
	for(long long  i = 1; i <= C; i++){
		in >> R >> k >> N;
		vector<long long> list;
		long long temp;
		for(long long j = 0; j < N; j++){
			in >> temp;
			list.push_back(temp);
		}
		out << "Case #" << i << ": " << solve(R,k,N,list) << endl;
	}
	return 0;
}

