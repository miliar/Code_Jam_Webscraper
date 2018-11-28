#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
int t[20][20];
int check(int a, int b, int len){
	int x=0;
	int y=0;
	for(int i=0; i<len; i++)
	for(int j=0; j<len; j++){
		if(i==0&&j==0) continue;
		if(i==0&&j==len-1) continue;
		if(i==len-1&&j==0) continue;
		if(i==len-1&&j==len-1) continue;

		x+=t[i+a][j+b]*(i*2-len+1);
		y+=t[i+a][j+b]*(j*2-len+1);
		//cerr<<i << " " << j<< " " <<t[i+a][j+b] <<endl;
		//cerr<<x<<endl;
		//cerr<<y<<endl;

	}
	if(x==0&&y==0)
		return true;
	return false;
}
void doo()
{
	int n, m, nouse;
	cin >> n >> m >> nouse;
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			while(1){
				char c;
				cin >> c;
				if(c>='0' && c<='9'){
					t[i][j]=c-'0';
					break;
				}
			}
			//cerr<<t[i][j];
		}
		//cerr<<endl;
	}
	int ans=0;
	//check(1,1,5);
	//return ;
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			for(int t=3; ; t++){
				if(i+t>n)
					break;
				if(j+t>m)
					break;
				if(check(i, j, t)){
					if(ans<t){
						//cerr<<i<< " " << j << " " << t <<endl;
						ans=t;
					}
				}
			}
		}
	}
	if(ans==0)
		cout<<" IMPOSSIBLE";
	else
		cout<<" "<<ans;
}
int main()
{
	int ncase;
	cin >> ncase;
	for(int i=0; i<ncase; i++)
	{
		cout<<"Case #"<<i+1<<":";
		doo();
		cout<<endl;
	}
}
