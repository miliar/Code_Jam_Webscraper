#include<iostream>
#include<stack>
#include<algorithm>
#include<vector>

using namespace std;
typedef pair <int,int> par;

struct vert{
	vector <par> adj;
	int visitado;
	int altura;
	char l;
}G[101][101];

int h,w;
char mapa2[10][10],label;
int mapa1[10][10];
stack <par> pilha;

par caminho(int y, int x){
	int alt[4];
	par r;
	r.first=-1; r.second=-1;
	alt[0]=alt[1]=alt[2]=alt[3]=50000;
	if(y-1>=0) alt[0]=G[y-1][x].altura;
	if(x-1>=0) alt[1]=G[y][x-1].altura;
	if(x+1<w) alt[2]=G[y][x+1].altura;
	if(y+1<h) alt[3]=G[y+1][x].altura;
	sort(alt, alt+4);
	//for(int i=0; i<=3; i++) cout<<alt[i]<<" ";
	//cout<<endl;
		if(y-1>=0) if(alt[0]==G[y-1][x].altura && G[y][x].altura>G[y-1][x].altura){
			r.first=x; r.second=y-1;		
			//cout<<"Norte\n";
			return r;
		}
		if(x-1>=0) if(alt[0]==G[y][x-1].altura && G[y][x].altura>G[y][x-1].altura){
			r.first=x-1; r.second=y;		
			return r;
		}
		if(x+1<w) if(alt[0]==G[y][x+1].altura && G[y][x].altura>G[y][x+1].altura){
			r.first=x+1; r.second=y;		
			return r;
		}
		if(y+1<h) if(alt[0]==G[y+1][x].altura && G[y][x].altura>G[y+1][x].altura){
			r.first=x; r.second=y+1;		
			return r;
		}
		if(r.first==-1){
			r.first=x; r.second=y;
		}
	return r;
		
		
}


int main(){
	par x, vpilha;
	int n, caso=1,parou;
	vert temp;
	cin>>n;
	for(int z=0; z<n; z++){
		cin>>h>>w;
		for(int i=0; i<h; i++) for(int j=0; j<w; j++){
			G[i][j].l=0;
			cin>>G[i][j].altura;
			G[i][j].adj.clear();
			G[i][j].visitado=0;
		}
		/*for(int i=0; i<h; i++){
		       	for(int j=0; j<w; j++){
				cout<<G[i][j].visitado<<" ";
			}
			cout<<endl;
		}*/

		//cout<<caminho(1,1).first<<"\t"<<caminho(1,1).second<<endl;
		for(int i=0; i<h; i++) for(int j=0; j<w; j++){
			x=caminho(i,j);
			//cout<<"I="<<i<<"\t"<<"J="<<j<<endl;
			//cout<<"x=("<<x.first<<","<<x.second<<")\n";
			if(!(x.first==j && x.second==i)){
				G[i][j].adj.push_back(x);
				x.first=j; x.second=i;
				G[caminho(i,j).second][caminho(i,j).first].adj.push_back(x);
			}
		}
		//cin>>temp;
		/*for(int i=0; i<h; i++){
			for(int j=0; j<w; j++){
				cout<<"( ";
				for(int k=0; k<G[i][j].adj.size(); k++)
					cout<<G[i][j].adj[k].first<<","<<G[i][j].adj[k].second<<" ";
				cout<<" )";
			}
			cout<<endl;
		}*/
		vpilha.first=vpilha.second=0;
		pilha.push(vpilha);
		G[0][0].l='a'; label='a'; int parada=0, linha,coluna;
		/*for(int i=0; i<h; i++){
		       	for(int j=0; j<w; j++){
				cout<<G[i][j].visitado<<" ";
			}
			cout<<endl;
		}*/
		while(parada<h*w){
			while(!pilha.empty()){
				//cout<<"fim\n";
				vpilha=pilha.top();
				linha=vpilha.first; coluna=vpilha.second;
					G[linha][coluna].visitado=1; parada++;
				G[linha][coluna].l=label;
				pilha.pop();
				//cout<<"Tamanho da pilha: "<<pilha.size()<<endl;
				for(int i=0; i<G[linha][coluna].adj.size(); i++){
					if(G[G[linha][coluna].adj[i].second][G[linha][coluna].adj[i].first].visitado==0){
						//cout<<"ok\n";
						//G[G[linha][coluna].adj[i].second][G[linha][coluna].adj[i].first].l=label;
						vpilha.first=G[linha][coluna].adj[i].second;
						vpilha.second=G[linha][coluna].adj[i].first;
						pilha.push(vpilha);
					}

				}
				
			}
			label++;
		/*for(int i=0; i<h; i++){
		       	for(int j=0; j<w; j++){
				cout<<G[i][j].visitado<<" ";
			}
			cout<<endl;
		}*/
			int flag=0;
			for(int m=0; m<h; m++){ 
				//cout<<m<<endl;
				for(int n=0; n<w; n++){
					//cout<<G[m][n].visitado;
					if(G[m][n].visitado==0){
						//cout<<"fim2\n";
						vpilha.first=m; vpilha.second=n;
						pilha.push(vpilha);
						flag=1;
						break;
					}
				}
				//cout<<endl;
				if(flag) break;
			}
		/*for(int i=0; i<h; i++){
		       	for(int j=0; j<w; j++){
				cout<<G[i][j].visitado<<" ";
			}
			cout<<endl;
		}*/
			//cin>>parou;				
			//cout<<"fim\n";
		}
		cout<<"Case #"<<caso<<":"<<endl;
		for(int i=0; i<h; i++){
			cout<<G[i][0].l;
			for(int j=1; j<w; j++) cout<<" "<<G[i][j].l;
			cout<<endl;
		}
		caso++;
	}
		
		

}
