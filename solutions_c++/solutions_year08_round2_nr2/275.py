#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OU.txt");
	ifstream FILE("IN.txt");
	
	vector <bool> primi(1001, true);
	primi[0]=false;
	primi[1]=false;
	vector <int> pp;
	for (int i=2; i<1001; i++) if (primi[i]) {
		pp.push_back(i);
		for (int h=i+i; h<1001; h+=i) primi[h]=false;	
		}
	
//	for (int i=0; i<pp.size(); i++) cout<<pp[i]<<"\n";
//	system("PAUSE");	
	int Num;
	FILE>>Num;
	for (int z=1; z<=Num; z++) {
		cout<<z<<"\n";
		int A,B,P;
		FILE>>A>>B>>P;
		int F=B-A+1;
		vector <vector <bool> > d(F, vector <bool> (F,false));
		
		for (int i=0; i<F; i++) for (int j=0; j<F; j++) {
			for (int z=0; z<pp.size(); z++) if (pp[z]>=P) {
				if ((i+A)%pp[z]==0 && (j+A)%pp[z]==0) {z=pp.size(); d[i][j]=true;}
				}
			}
		
		vector <bool> visited(F, false);
		
		vector <int> color(F);
		
		int coun=0;
		for (int i=0; i<F; i++) if (visited[i]==false) {
			coun++;
			vector <int> que;
			que.push_back(i);
			visited[i]=true;
			int u;
			while (que.size()>0) {
				u=que[que.size()-1];
				color[u]=coun;
				que.pop_back();
				for (int j=0; j<F; j++) if (d[j][u]==true) if (visited[j]==false) {
					visited[j]=true;
					que.push_back(j);
					}
				}
			}
//		if (z==8) for (int i=0; i<F; i++) cout<<i+A<<" "<<color[i]<<"\n";
//		cout<<"\n";
/*		
		vector <int> col(F);
		for (int i=0; i<F; i++) col[i]=i;
		for (int i=0; i<F; i++) for (int j=i+1; j<F; j++) if (d[i][j]==true) {
			if (col[j]<col[i]) col[i]=col[j];
			else col[j]=col[i];
			}
		if (z==8) for (int i=0; i<F; i++) cout<<A+i<<" "<<col[i]<<"\n";
		cout<<"\n\n";
		
		set<int> m;
		for (int i=0; i<F; i++) m.insert(col[i]);
*/		
		OUT<<"Case #"<<z<<": "<<coun<<"\n";
		}
	FILE.close();
	OUT.close();
	system("PAUSE");
	return 0;
	}
