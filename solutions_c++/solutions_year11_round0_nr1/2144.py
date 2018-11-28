// c.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
#include <vector>
#include <math.h>

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fin = freopen("a.in", "r", stdin);
	FILE* fout = freopen("output.txt", "w", stdout);
	
	int T;
	cin>>T;
	for(int t=0; t<T; t++){
		int n;
		cin>>n;
		vector<int> O, B;

		int o_pos = 1, b_pos = 1;
		char last = 'f', first;

		for(int i=0; i<n; i++){
			char c;
			int v;
			cin>>c>>v;
			if(last == 'f') first = c;
			if(c == 'O'){
				int tmp = v;
				v=abs(v-o_pos);
				o_pos = tmp;
				if(last == c) O[O.size()-1]+=v+1;
				else{
					O.push_back(v);
					if(B.size()>0){
						O[O.size()-1]-=B[B.size()-1]+1;
						if(O[O.size()-1]<0) O[O.size()-1]=0;
					}
				}
			}
			else{
				int tmp = v;
				v=abs(v-b_pos);
				b_pos = tmp;
				if(last == c) B[B.size()-1]+=v+1;
				else{
					B.push_back(v);
					if(O.size()>0){
						B[B.size()-1]-=O[O.size()-1]+1;
						if(B[B.size()-1]<0) B[B.size()-1]=0;
					}
				}
				
			}
			last = c;
		}

		

		long sum = 0;
		if(first == 'O'){
			for(int i = 0; i<__max(O.size(), B.size()); i++){
				if(i<O.size()) sum+=O[i]+1;
				if(i<B.size()) sum+=B[i]+1;
			}
		}else{
			for(int i = 0; i<__max(O.size(), B.size()); i++){
				if(i<B.size()) sum+=B[i]+1;
				if(i<O.size()) sum+=O[i]+1;				
			}
		}
		/*for(int i = 0; i<__max(O.size(), B.size()); i++){
			if(i>=O.size()) sum+=B[i];
			else if(i>=B.size()) sum+=O[i];
			else {
				sum+=__max(B[i], O[i]);
				if(B[i] == O[i]) sum++;
			}
		}*/

		cout<<"Case #"<<t+1<<": "<<sum<<endl;
	}

	fclose(fin);
	fclose(fout);
	return 0;
}

