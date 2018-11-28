#include <bitset>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <deque>
#include <vector>
#include <list>
#include <queue>
#include <string>
using namespace std;
ofstream fout("B-large.out");
ifstream fin("B-large.in");
int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		int C;
		fin >> C;
		int combine[26][26];
		bool oppose[26][26];
		for(int i=0;i<26;i++){
			for(int j=0;j<26;j++){
				combine[i][j] = -1;
				oppose[i][j] = false;
			}
		}
		
		for(int i=0;i<C;i++){
			char a, b, c;
			fin >> a >> b >> c;
			combine[a-'A'][b-'A'] = c-'A';
			combine[b-'A'][a-'A'] = c-'A';
		}
		int D;
		fin >> D;
		for(int i=0;i<D;i++){
			char a, b;
			fin >> a >> b;
			oppose[a-'A'][b-'A'] = true;
			oppose[b-'A'][a-'A'] = true;
		}
		
		vector<int> ll;
		int N;
		fin >> N;
		for(int i=0;i<N;i++){
			char c;
			fin >> c;
			int tt = c - 'A';
			
			if(!ll.empty() && combine[ll.back()][tt] != -1){
				int asdasfa = ll.back();
				ll.pop_back();
				ll.push_back(combine[asdasfa][tt]);
			} else {
				bool ccccc = false;
				for(int j=0;j<ll.size();j++){
					if(oppose[ll[j]][tt]){
						ccccc = true;
						ll.clear();
						break;
					}
				}
				if(!ccccc){
					ll.push_back(tt);
				}
			}
			//for(int j=0;j<ll.size();j++){
			//	cout << ll[j] << " ";
			//}
			//cout << endl;
		}
		
		fout << "Case #"<< s+1 << ": [";
		for(int i=0;i<ll.size();i++){
			fout << (char)(ll[i] + 'A');
			if(i < ll.size() - 1){
				fout << ", ";
			}
		}
		fout << "]\n";
		//cout << endl;
	}
}
