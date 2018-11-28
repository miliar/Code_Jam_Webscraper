#include<iostream>
#include<string>
#include<vector>
using namespace std;
pair<int,int> bfs(vector<vector<int> > m,int i,int j,int a,int b){
	bool enter;
	pair<int,int> temp;
	while(true){
		int min=m[i][j];
		enter = false;
		int min_i = -1, min_j = -1;
		if(i-1 >= 0) {						//north
			if(m[i-1][j] < min)				
			{
				min_i=i-1;
				min_j=j;
				min = m[i-1][j];
				enter = true;
			}
		}
		if(j-1>=0) {						//west
			if(m[i][j-1] < min)				
			{
				min_j=j-1;
				min_i=i;
				min = m[i][j-1];
				enter = true;
			}
		}
		if(j+1<b) {						//east
			if(m[i][j+1] < min)				
			{
				min_j=j+1;
				min_i=i;
				min = m[i][j+1];
				enter = true;
			}
		}
		if(i+1 < a) {
			if(m[i+1][j] < min)				//south
			{
				min_i=i+1;
				min_j=j;
				min = m[i+1][j];
				enter = true;
			}
		}
		if(enter == false)
			break;
		i = min_i;
		j = min_j;
	}
	temp = make_pair(i,j);
	return temp;
}
main(){
	int n;
	cin>>n;
	int z;
	for(z=1;z<=n;z++){
		int a,b;
		cin>>a>>b;
		vector<vector<int> > m(a,vector<int> (b));
		int i,j;
		for(i=0;i<a;i++)
			for(j=0;j<b;j++)
				cin>>m[i][j];
		vector<vector<char> > output(a,vector<char> (b,'.'));
		int incr = 97;
		pair<int,int> p;
		int x,y;
		for(i=0;i<a;i++){
			for(j=0;j<b;j++){
				p=bfs(m,i,j,a,b);
				x = p.first;
				y = p.second;
				if(output[x][y]=='.'){
					output[x][y]=char(incr);
					incr++;
				}
				output[i][j] = output[x][y];
			}
		}
		cout<<"Case #"<<z<<":"<<endl;
		for(i=0;i<a;i++){
			for(j=0;j<b;j++){
				cout<<output[i][j]<<" ";
			}
			cout<<endl;
		}
		
	}
}
