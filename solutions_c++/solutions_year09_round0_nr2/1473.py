#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
using namespace std;

main(){
	ofstream fout ("A-small.out");
	ifstream fin ("A-small.in");
	int T;
	fin>>T;
	for (int k=0;k<T;k++){
		int H,W;
		fin>>H>>W;
		vector<int> vysky(H*W);	
		for(int i=0;i<(H*W);i++){
			int pom;
			fin>>pom;
			vysky[i]=pom;
		}
		vector<vector<int> > a(H*W);
		for(int i=0;i<(H*W);i++){
			int minP=-1;
			int min=vysky[i];
			if (i>=W && vysky[i-W]<min){
				min = vysky[i-W];
				minP=0;
			}
			if ((i%W)!=0 && vysky[i-1]<min){
				min = vysky[i-1];
				minP=1;
			}
			if ((i%W)!=W-1 && vysky[i+1]<min){
				min = vysky[i+1];
				minP=2;
			}
			if (i<(W*(H-1)) && vysky[i+W]<min){
				min = vysky[i+W];
				minP=3;
			}
			//pridaj hranu
			switch(minP)
			{
			case 0:
				a[i].push_back(i-W);
				a[i-W].push_back(i);
				break;
			case 1:
				a[i].push_back(i-1);
				a[i-1].push_back(i);
				break;
			case 2:
				a[i].push_back(i+1);
				a[i+1].push_back(i);
				break;
			case 3:
				a[i].push_back(i+W);
				a[i+W].push_back(i);
				break;
			}
		}
		//search
		vector<int> visited(H*W,0);
		vector<int> part(H*W,-1);
		int akt=0;
		for(int i=0;i<(H*W);i++){
			if (visited[i]==0){
				queue<int> q;
				visited[i]=1;
				q.push(i);
				while (!q.empty()){
					for(int j=0;j<a[q.front()].size();j++){
						if (visited[a[q.front()][j]]==0){
							visited[a[q.front()][j]]=1;
							q.push(a[q.front()][j]);
						}
					}
					part[q.front()]=akt;
					q.pop();
				}
				akt++;
			}
		}
		fout<<"Case #"<<k+1<<":"<<endl;
		for(int i=0;i<H;i++){
			for(int j=0;j<W;j++){
				fout<<char(part[W*i+j]+'a');
				if (j<W-1){
					fout<<" ";
				}
			}
			fout<<endl;
		}
		
	}
	fout.close();
}
