/**Author Nasini Madhava Rao**/
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
#include<climits>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
int dfs(int p,int q,vvi &arr,vvi &map,int count,int &used){
	if(arr[p][q]!=-1){
		used =0;
		return arr[p][q];
	}
	else{
		static int x[]={-1,0,0,1};
		static int y[]={0,-1,1,0};int min=INT_MAX,index;
		inc(i,4){
			int a=p+x[i],b=q+y[i];
			if(a>=0 && b>=0 && a<sz(arr) && b<sz(arr[0])){
					if(min>map[a][b]){
						min=map[a][b];
						index =i;
					}
			}
		}
		if(min<map[p][q]){
			return arr[p][q] = dfs(p+x[index],q+y[index],arr,map,count,used);
		}
		else{
				used =1;
				arr[p][q] = count;
				return count;
		}
	}
}
int main(){

	int nt;
	cin>>nt;
	for(int i=1;i<=nt;i++){
		int m,n;
		cin>>m>>n;
		vvi map(m,vi(n));
		inc(p,m)
			inc(q,n)
				cin>>map[p][q];
		vvi arr(m,vi(n,-1));
		int count =1;
		inc(p,m)
			inc(q,n)
				if(arr[p][q]==-1){
					int used=0;
					dfs(p,q,arr,map,count,used);
					if(used)
						count++;
				}
		cout<<"Case #"<<i<<":\n";
		inc(p,m){
			inc(q,n){
				printf("%c ",arr[p][q]+'a'-1);
			}
			puts("");
		}
			
	}
return EXIT_SUCCESS;

}
