#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

int main()
{
	int T;
	fin >> T;
	for(int caseID=1; caseID<=T; caseID++) {
		int N, S, p;
		fin >> N >> S >> p;
		map<int, int> m1;
		for(int i=0; i<N; i++) {
			int tmp;
			fin >> tmp;
			m1[tmp]++;
		}

		int total=0;
		map<int,int>::const_reverse_iterator ri;
		for(ri=m1.rbegin(); ri!=m1.rend(); ri++) {
			int x = (*ri).first;
			int n = (*ri).second;
			if(x%3==0 && x/3>=p)
				total += n;
			else if (x%3==1 && (x-1)/3+1>=p)
				total += n;
			else if (x%3==2 && (x-2)/3+1>=p)
				total += n;
			else if (S!=0 && p-2>=0 && (x==3*p-3 || x==3*p-4)){
				if(n<S) {
					total += n;
					S -= n;
				}
				else {
					total += S;
					S = 0;
				}
			}
			else {
				continue;
			}
		}
		fout << "Case #" << caseID << ": ";
		fout << total << endl;
	}

	return 0;
}
