#include <iostream>



using namespace std;





int grid[101][101];
int grid_status[101][101];
int basin_count;


int H,W;

void dfs(int i,int j) {
  //cout<<i<<" "<<j<<endl;
  int min_alt=20000; int min_i=-1,min_j=-1;
  if(i-1>=0 && grid[i-1][j]<grid[i][j] && grid[i-1][j]<min_alt) {
    min_alt=grid[i-1][j];
    min_i=i-1;
    min_j=j;
  }
  
  if(j-1>=0 && grid[i][j-1]<grid[i][j] && grid[i][j-1]<min_alt) {
    min_alt=grid[i][j-1];
    min_i=i;
    min_j=j-1;
    
  }
  
  if(j+1<W && grid[i][j+1]<grid[i][j] && grid[i][j+1]<min_alt) {
    min_alt=grid[i][j+1];
    min_i=i;
    min_j=j+1;
  }
  
  if(i+1<H && grid[i+1][j]<grid[i][j] && grid[i+1][j]<min_alt) {
    min_alt=grid[i+1][j];
    min_i=i+1;
    min_j=j;
    
  }
  
  if(min_i!=-1 && min_j!=-1) {
    if(grid_status[min_i][min_j]!=-1) {
      basin_count=grid_status[min_i][min_j];
    }
    else {
      dfs(min_i,min_j);
    }
  }
  grid_status[i][j]=basin_count;

} 




int main() {
  
  int T;
  cin>>T;
  int case_num=1;
  while(T--) {
    
    
    cin>>H;
    cin>>W;
    for(int i=0;i<H;i++) {
      for(int j=0;j<W;j++) {
	cin>>grid[i][j];
	grid_status[i][j]=-1;
      }
    }
    

    basin_count=0;
    int mbc=0;
    for(int i=0;i<H;i++) {
      for(int j=0;j<W;j++) {
	if(grid_status[i][j]==-1) {
	  if(basin_count<mbc)
	    basin_count=mbc;
	  //cout<<"start:"<<endl;
	  dfs(i,j);
	  if(mbc==basin_count)
	    mbc++;
	}
      }
    }
    
    char basins[27];
    for(int i=0;i<27;i++) 
      basins[i]='\0';
    char start='a';

    for(int i=0;i<H;i++) {
      for(int j=0;j<W;j++) {
	if(basins[grid_status[i][j]]=='\0') {
	  basins[grid_status[i][j]]=start;
	  grid_status[i][j]=start;
	  start++;
	}
	else {
	  grid_status[i][j]=basins[grid_status[i][j]];
	}
      }
    }
    cout<<"Case #"<<case_num<<":"<<endl;
    for(int i=0;i<H;i++) {
      for(int j=0;j<W;j++) {
	cout<<(char)grid_status[i][j];
	if(j==W-1) {
	  cout<<endl;
	}
	else
	  cout<<" ";
      }
    }
    case_num++;
  }
  return 0;
}
      
    
