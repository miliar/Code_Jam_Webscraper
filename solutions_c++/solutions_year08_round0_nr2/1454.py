#include <iostream>
using namespace std;
int ty[400];

int quicksort_partition(int L[], int Lbb, int Ubb)
{
int iPivValue;
int i;
int iPivPos;
iPivValue = L[Ubb];
iPivPos = Lbb - 1;
for (i=Lbb; i<=Ubb-1; i++)
{
if (L[ i ] <= iPivValue)
{
iPivPos++;
swap(L[iPivPos], L[ i ]);swap(ty[iPivPos],ty[i]);
}
}
iPivPos++;
swap(L[iPivPos], L[Ubb]);swap(ty[iPivPos], ty[Ubb]);
return iPivPos;
}

void quicksort(int L[], int Lbb, int Ubb)
{
int iPiv;
if (Lbb < Ubb)
{
iPiv = quicksort_partition(L, Lbb, Ubb);
quicksort(L, Lbb, iPiv - 1);
quicksort(L, iPiv + 1, Ubb);
}
return;
}

int main(){

	freopen("B-large.in","r",stdin);
	freopen("2o.txt","w",stdout);
	long i,j,n;
	int t,na,nb,nat[100][2],nbt[100][2],h1,m1,h2,m2,tim[400],al,p,a,b,ac,bc;

	scanf("%d\n",&n);
	for(i=0;i<n;++i){
		scanf("%d\n",&t);
		scanf("%d%d\n",&na,&nb);
		for(j=0;j<na;++j){
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			nat[j][0]=h1*60+m1;
			nat[j][1]=h2*60+m2+t;
		}
		for(j=0;j<nb;++j){
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			nbt[j][0]=h1*60+m1;
			nbt[j][1]=h2*60+m2+t;
		}
		p=0;
		for(j=0;j<na;++j,p+=2){
			tim[p]=nat[j][0]*10;ty[p]=1;tim[p+1]=nat[j][1]*10-1;ty[p+1]=2;
		}
		for(j=0;j<nb;++j,p+=2){
			tim[p]=nbt[j][0]*10;ty[p]=3;tim[p+1]=nbt[j][1]*10-1;ty[p+1]=4;
		}
		al=na*2+nb*2;
		quicksort(tim,0,al-1);


		a=0;b=0;ac=0;bc=0;
		for(j=0;j<al;++j)
			switch (ty[j]){
				case 1:if (ac==0) ++a;else --ac;break;
				case 2:++bc;break;
				case 3:if (bc==0) ++b;else --bc;break;
				case 4:++ac;break;
		}
		
		cout<<"Case #"<<i+1<<": "<<a<<" "<<b<<endl;

	
	
	}
	return 0;

}