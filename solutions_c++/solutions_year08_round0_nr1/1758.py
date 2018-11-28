#include <stdio.h>
#include <queue>
#include <string>
#include <map>
#include <vector>

#define INF 1000000
using namespace std;


int edges[1000*110][110];
int vis[1000*110];
int dists[1000*110];

int main(){

	char temp[200];

	int numCases;
	int sMax, qMax;
	scanf("%d\n",&numCases);
	for(int g = 0;g<numCases;g++){
		map<string,int> mapa;
		vector<int> proibidas;
		scanf("%d\n",&sMax);//,&qMax);
		for(int i=0;i<sMax;i++){
			string a = (string) gets(temp);
			//printf("%d %d got %s\n",numCases,i,(char*) a.c_str());
			mapa[a]=i;
		}
		scanf("%d\n",&qMax);
		if(qMax==0){
			printf("Case #%d: %d\n",g+1,0);
			continue;
		}
		for(int i=0;i<qMax;i++){
			string a = (string) gets(temp);
			//printf("got %s(%d)\n",(char*) a.c_str(),mapa[a]);
			proibidas.push_back(mapa[a]);
		}




		//inicializa Dijkstra
		priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q;	

		for(int i=0;i<sMax*qMax;i++){
			for(int j=0;j<qMax;j++){
				edges[i][j]=-1;
			}
			dists[i]=INF;
			vis[i]=0;
		}

		for(int i=0;i<sMax;i++){
			if(i!=proibidas[0]){
				q.push(make_pair(0,i));	
				vis[i]=1;
				dists[i]=0;
			}
		}

		//inicializa grafo
		for(int q=0;q<qMax-1;q++){
			for(int s=0;s<sMax;s++){		
				for(int sDest=0;sDest<sMax;sDest++){			

					if(sDest==proibidas[q+1]){
						edges[q*sMax+s][sDest]=INF;
					}
					else if(s==sDest){
						edges[q*sMax+s][sDest]=0;
					}
					else{
						edges[q*sMax+s][sDest]=1;
					}
				}			
			}
		}
		
		while(!q.empty()){
			pair<int,int> t = q.top(); q.pop();
			//printf("Next in queue v:%d d:%d\n",t.second,t.first);
			int nodeDist = t.first;
			int node = t.second;
			vis[node]=1;
			if(node/sMax==qMax-1) continue;
			for(int i=0;i<sMax;i++){
				int nextNode = (node/sMax+1)*sMax+i;

				int edgeToNextNode = edges[node][i];
				//printf(" Nextnode %d edgeweight %d\n",nextNode,edgeToNextNode);
				if((!vis[nextNode])&&(edgeToNextNode!=INF)){
					int alt = nodeDist+edgeToNextNode;
					if(alt<dists[nextNode]){
					//	printf("inserting alt %d for node %d",alt,nextNode);
						dists[nextNode]=alt;
						q.push(make_pair(alt, nextNode));
					}
				}
			}
		}
		/*printf("Distancias\n");	
		for(int i=0;i<sMax*qMax;i++){
			printf("%d: %d\n",i,dists[i]);
		}*/
		int menor = dists[(qMax-1)*sMax];
		for(int i=(qMax-1)*sMax;i<(qMax)*sMax;i++){
			if(dists[i]<menor){
				menor = dists[i];
			}
		}
		printf("Case #%d: %d\n",g+1,menor);



	}
	/*





	 */


}