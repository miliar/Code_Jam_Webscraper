#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstring>

using namespace std;
int dx[] = {-1,0,0,1};
int dy[] = {-0,-1,1,0};
int	 H , W , cur;
int arr[10001][1001];
int res[10001][10001];
struct dato{
	int peso ,x , y , id;
	dato(int p, int xx, int yy , int idd){peso = p ,x = xx, y = yy , id = idd;}
	dato(){}
};
bool operator < (dato a , dato b){
	if(a.peso != b.peso)
		return a.peso<b.peso;
	else
		return a.id<b.id;
}
bool valido(int x , int y){return x>=0&&x<H && y>=0&&y<W;}
	
void encuentra(int x , int y , int &color){
	int alt = arr[x][y];
	int minx = -1, miny = -1;
	bool wan = false;
	vector<dato> op;
	for(int i = 0 ; i < 4 ; i++){
		if(valido(x+dx[i],y+dy[i])){
			if(arr[x+dx[i]][y+dy[i]] < alt){
					alt = arr[x+dx[i]][y+dy[i]];
					minx = x+dx[i] , miny = y+dy[i];
					wan = true;
			}
		}
	}
	if(!wan){
		color = cur;
		res[x][y] = cur;
		cur++;
		return;
	}
	else{
		if(res[minx][miny] == -1){
			encuentra(minx,miny,color);
			res[x][y] = color;
			res[minx][miny] = color;
			return;
		}
		else{	
			res[x][y] = res[minx][miny];
			color = res[minx][miny];
			return;
		}
	}
}

int main(){
	int T ;
	cin>>T;
	for(int t = 0 ; t < T ; t++){
		cin>>H>>W;
		memset(arr,0,sizeof(arr));
		memset(res,-1,sizeof(res));
		for(int i = 0 ; i < H ; i++)
			for(int j = 0 ; j < W ; j++)
				cin>>arr[i][j];
		cur = 0;
		int color;
		for(int i = 0 ; i < H ; i++)
			for(int j = 0 ; j < W ; j++)
				if(res[i][j]==-1){
					encuentra(i,j,color);
					res[i][j] = color;
				}
		cout<<"Case #"<<t+1<<":"<<endl;
		vector<int> temp ;
		for(int i = 0 ; i < H ; i++){
			for(int j = 0 ; j < W ; j++){
				temp.push_back(res[i][j]);
			}			
		}
		int actual = 0;
		char flag;
		vector<char>trad(30,' ');
		for(int i = 0 ; i < temp.size() ; i++){
			if(trad[temp[i]] == ' '){
				trad[temp[i]] = actual+'a';
				actual++;
			}
		}
		for(int j = 0 ; j < H ; j++){
			for(int i = 0 ; i < W ; i++){
				if(i == 0)
					cout<<trad[res[j][i]];				
				else
					cout<<" "<<trad[res[j][i]];				
			}
			cout<<endl;				
		}
	}
	return 0;
}
