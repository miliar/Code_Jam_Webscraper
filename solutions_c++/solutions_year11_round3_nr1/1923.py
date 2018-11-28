#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
char graph[100][100];
char graph1[100][100];
char rr[100][100];

int main()
{


	int i,j,cnt,t;

	int kase = 1;
	cin >> t;
	while(t--){
		int n,m;
		cin >> n >> m;

		memset(graph,0,sizeof graph);
		memset(rr,0,sizeof rr);
		memset(graph1,0,sizeof graph1);

		for(i=0;i<n;i++){
			cin >>	graph[i];
			for(j=0;j<m;j++)
				graph1[i][j] = graph[i][j];
		}

		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(graph1[i][j] =='#'){
					graph1[i][j] ='@';
					graph1[i][j+1] ='@';
					graph1[i+1][j] ='@';
					graph1[i+1][j+1] ='@';
					rr[i][j] ='/';
					rr[i][j+1] ='\\';
					rr[i+1][j] ='\\';
					rr[i+1][j+1] ='/';
				}else if(graph1[i][j] =='.' )rr[i][j] ='.';

		bool flag=true;
		for(i=0;i<n+1;i++)
			for(j=0;j<m+1;j++)
				if(graph1[i][j] == '@'){
					if(graph[i][j] !='#')
						flag=false;
				}

		cout <<"Case #"<<kase++<<":"<<endl;
		
		if(!flag)
			cout << "Impossible"<<endl;
		else{
			for(i=0;i<n;i++,cout <<endl)
				for(j=0;j<m;j++)
					cout <<rr[i][j];

		}
	}
}
