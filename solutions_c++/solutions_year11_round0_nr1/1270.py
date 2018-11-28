#include<fstream>
#include<vector>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("a.out");
int t,n,i,j,poz[2],k,x;
vector<int> a[2],p;
char c;
void inain(int b){
	if(poz[b]>a[b][0])poz[b]--;
	else if(poz[b]<a[b][0])poz[b]++;
}
int main()
{
	fin>>t;
	for(j=1;j<=t;j++){
		fin>>n;
		poz[0]=poz[1]=1; k=0;
		for(i=1;i<=n;i++){fin>>c>>x;
			if(c=='O'){a[0].push_back(x);p.push_back(0);}
			else {a[1].push_back(x);p.push_back(1);}
		}
		while(p.size()!=0){
			if(a[p[0]][0]==poz[p[0]]){
				k++;
				a[p[0]].erase(a[p[0]].begin());
				inain((p[0]+1)%2);
				p.erase(p.begin());
			}
			else {
				inain(1);
				inain(0);
				k++;
			}
		}
		fout<<"Case #"<<j<<": "<<k<<'\n';
	}
	return 0;
}