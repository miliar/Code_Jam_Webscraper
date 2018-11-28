#include<iostream>
#include<vector>
#include<string>

using namespace std;

int dx[4]={0, -1, 1, 0};
int dy[4]={-1, 0, 0, 1};
vector<vector<int> > dirs;
vector<vector<int> > alts;
vector<vector<int> > islands;
vector<vector<char> > res;
vector<int> sinks;
int H, W;

void make_dirs_sinks(){
	sinks.clear(); sinks.resize(0);
	dirs.clear(); dirs.resize(H, vector<int>(W, -1));
	int x,y;
	for(int j=0; j<H; j++){
		for(int k=0;k<W; k++){
			 int minalt = alts[j][k]; int besti=-1; 
			//cout<<j<<" "<<k<<" "<<alts[j][k]<<"\n";
			for(int i=0; i<4; i++){
				x=k+dx[i]; y=j+dy[i];
				if(x>=0 && x<W && y>=0 && y<H){
					if(alts[y][x]<minalt){
						minalt=alts[y][x]; besti=i;
					}
				}
			}
				dirs[j][k]=besti;
				if(besti<0){sinks.push_back(j);sinks.push_back(k);}
			
			//cout<<dirs[j][k]<<"\n";
		}
	}
	
}

void rec(int x, int y, int c){
	int x1, y1;
	islands[y][x]=c;
	for(int j=0; j<4; j++) {
			x1=x+dx[j]; y1=y+dy[j];	
			if(x1>=0 && x1<W && y1>=0 && y1<H && dirs[y1][x1]!=-1){
				if(abs(dirs[y1][x1]+j)==3){
					rec(x1, y1, c);
				}
			}
	}
	
}
void make_islands(){
	islands.clear(); islands.resize(H, vector<int>(W, -1));
	int x,y, x1, y1;
	for(int i=0; i<sinks.size()/2; i++ ){

		y=sinks[i*2]; x=sinks[i*2+1];  
		rec(x, y, i);
		
	}
	
}
void make_res() {
	res.clear(); res.resize(H, vector<char>(W, '0'));
	int nc=sinks.size()/2; char let='a';
	vector<char> sets(nc, '0'); 
	for(int j=0; j<H; j++){
		for(int k=0;k<W; k++){
			int c1 = islands[j][k];
			if(sets[c1]=='0'){
			         sets[c1]=let; let++; 
			}
		}
	}
	for(int j=0; j<H; j++){
		for(int k=0;k<W; k++){
			res[j][k] = sets[islands[j][k]];
		}
	}
}

int main(){
	int T;
	cin>>T;              
	for(int i=0; i<T; i++){
		
//input
	        cin>>H>>W;
	alts.clear(); alts.resize(H, vector<int>(W, -1));
		
		for(int j=0; j<H; j++){
			for(int k=0;k<W; k++){
				cin>>alts[j][k];
			}
		}


//body                                                        
                make_dirs_sinks();                            
		make_islands();        
		make_res();                     
		
//output
		cout<<"Case #"<<i+1<<":\n";
		for(int j=0; j<H; j++){
			for(int k=0;k<W; k++){
				cout<<res[j][k]<<" ";
			}
			cout<<"\n" ;
		}
	}
	
}
