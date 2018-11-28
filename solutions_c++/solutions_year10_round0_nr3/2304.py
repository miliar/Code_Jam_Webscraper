#include<queue>
#include<fstream>
using namespace std;

int main(){
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");

	int ncases;
	fin>>ncases;
	for(int Case=1;Case<=ncases;Case++)
	{
		fout<<"Case #"<<Case<<": ";
		int r,k,n;
		fin>>r>>k>>n;
		queue<int> groups;
		for(int i=0;i<n;i++){
			int g;
			fin>>g;
			groups.push(g);
		}
		int count = 0;
		while(r--){
			int cur = 0;
			queue<int> ride;
			while(!groups.empty() && (groups.front() + cur <= k)){
				cur += groups.front();
				ride.push(groups.front());
				groups.pop();
			}
			count+=cur;
			while(!ride.empty()){
				groups.push(ride.front());
				ride.pop();
			}
		}
		fout<<count<<endl;
	}

	fin.close();
	fout.flush();
	fout.close();
}
