#include <fstream.h>
#define MAXX 1001
ifstream in("/Users/SunKim/Desktop/Codejam3/Untitled/p3.in");
ofstream out("/Users/SunKim/Desktop/Codejam3/Untitled/p3.out");

int n,m;
int data[MAXX+1];
int cycle[MAXX+1];
int visit[MAXX+1];
int cnt;

int getcycle(int initial, int pos,int cnt){
	if(pos==initial) return cnt;
	visit[pos]=1;
	return getcycle(initial,data[pos],cnt+1);
}
int main(){
	int i;
	in >> n;
	for(int z=0;z<n;z++){
		in >> m;
		cnt=0;
		for(i=1;i<=MAXX;i++){
			data[i]=0;
			cycle[i]=0;
			visit[i]=0;
		}
		for(i=1;i<=m;i++){
			in >> data[i];
		}
		for(i=1;i<=m;i++){
			if(visit[i]==0){
				visit[i]=1;
				cycle[i]=getcycle(i,data[i],1);
				if(cycle[i]>1) cnt+=cycle[i];
			}
		}
		out << "Case #" << z+1 << ": " << cnt << ".000000\n";
	}
	return 0;
}