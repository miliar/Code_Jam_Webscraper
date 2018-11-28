#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef long long LL;
typedef long double LD;

typedef vector<int> VI;


#define MM 1000000

vector<LL> pr;

int join[1100][1100];
int col[1100];

void draw(LL i, LL c, LL B){

	queue<int> q;
	q.push(i);
	while(q.size()){
		int x=q.front();
		q.pop();
		col[x]=c;
		for(int j=i+1;j<=B;j++)
		if(!col[j] && join[x][j])
			q.push(j);
	}
}

int main()
{
	pr.push_back(2);
	pr.push_back(3);
	int N=pr.size();
	
	for(LL i=5;i<MM;i+=2){
		bool good=1;
		for(int j=0;j<N;j++){
			if(pr[j]*pr[j]>i)
				break;
			if( (i%pr[j])==0 ){
				good=0;
				break;
			}
		}
		if(!good)
			continue;
		pr.push_back(i);
		N++;
	}

	int ttt;
	cin >> ttt;
	for(int cutest=1;cutest<=ttt;cutest++){
		LL A,B,P;
		cin >> A >> B >> P;
		
		
		memset(join,0,sizeof(join));
		memset(col,0,sizeof(col));
		
		int X0=0;
		while(pr[X0]<P)
			X0++;

		for(int i=A;i<=B;i++)
		for(int j=A+1;j<=B;j++)
			for(int x=X0;pr[x]<=j;x++){
				if(pr[x]<P)
					continue;
				if(i%pr[x])
					continue;
				if(j%pr[x])
					continue;
				join[i][j]=join[j][i]=1;
			}
		
		int nCol=1;
		for(int i=A;i<=B;i++)
		if(!col[i]){
			draw(i,nCol,B);
			nCol++;
		}
		printf("Case #%d: %d\n",cutest,nCol-1);

	}

}
