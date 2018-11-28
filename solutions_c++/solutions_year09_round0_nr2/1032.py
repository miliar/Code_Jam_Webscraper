#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int alti[101][101];
char ans[101][101];
int graph[101][101][4];
int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};
char current;
int H,W,T;

void dfs(int p, int q){

	if(ans[p][q]=='0'){
		ans[p][q] = current;
		
		int x,y;
		
		for(int i=0; i<4; i++){
			x = p+dx[i];
			y = q+dy[i];
			
			if(graph[p][q][i] && ans[x][y]=='0'){
				dfs(x,y);
			}
		}
	}
	return;
}

bool inside(int i,int j){
	
	if(0<=i && i<H && 0<=j && j<W)
	return true;
	
	return false;
}

int main(){
 
  cin>>T;

  for(int i=0; i<T; i++){
    cin>>H>>W;

    for(int j=0; j<H; j++){
      for(int k=0; k<W; k++){
    	cin>>alti[j][k];
      }
    }

    for(int j=0; j<H; j++)
      for(int k=0; k<W; k++)
    	ans[j][k] = '0';

   	memset(graph,0,sizeof(graph));

    for(int j=0; j<H; j++){
      for(int k=0; k<W; k++){
   
		int jn,kn,jw,kw,je,ke,js,ks;
		jn = j-1;
		kn = k;
		jw = j;
		kw = k-1;
		je = j;
		ke = k+1;
		js = j+1;
		ks = k;

		int min=11111;

		if(inside(jn,kn) && alti[jn][kn]<min)
		  min = alti[jn][kn];

		if(inside(jw,kw) && alti[jw][kw]<min)
		  min = alti[jw][kw];

		if(inside(je,ke) && alti[je][ke]<min)
		  min = alti[je][ke];

		if(inside(js,ks) && alti[js][ks]<min)
		  min = alti[js][ks];

		//cout<<"min "<<min<<endl;

		if(min<alti[j][k]){
		  if(inside(jn,kn) && alti[jn][kn]==min){
			graph[j][k][0] = true;
			graph[jn][kn][3] = true;
			//cout<<j<<" "<<k<<" "<<jn<<" "<<kn<<endl;
		  }
		  else if(inside(jw,kw) && alti[jw][kw]==min){
			graph[j][k][1] = true;
			graph[jw][kw][2] = true;
			//cout<<j<<" "<<k<<" "<<jw<<" "<<kw<<endl;
		  }
		  else if(inside(je,ke) && alti[je][ke]==min){
			graph[j][k][2] = true;
			graph[je][ke][1] = true;
			//cout<<j<<" "<<k<<" "<<je<<" "<<ke<<endl;
		  }
		   else if(inside(js,ks) && alti[js][ks]==min){
			graph[j][k][3] = true;
			graph[js][ks][0] = true;
			//cout<<j<<" "<<k<<" "<<js<<" "<<ks<<endl;
		  }
		}
      }
    }
      
     
    current = 'a';

    for(int j=0; j<H; j++){
      for(int k=0; k<W; k++){
		if(ans[j][k]=='0'){
		  dfs(j,k);
		  current = (char)((int)current+1);
		}
      }
    }

    cout<<"Case #"<<i+1<<":"<<endl;

    for(int j=0; j<H; j++){
      cout<<ans[j][0];
      for(int k=1; k<W; k++){
    	cout<<" "<<ans[j][k];
      }
      cout<<endl;
    }

  }

  return 0;
}
