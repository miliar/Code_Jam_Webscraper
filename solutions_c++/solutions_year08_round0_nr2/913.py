#include<stdio.h>

//#define MAX 1001
#define MAX 2000
#define swap(a,b) a^=b^=a^=b

int T;

int N,M;


char data_departure[10],data_arrival[10];
int departure[MAX],arrival[MAX],where[MAX];
int i,j,k;

int Time;

int tree[2][MAX];
int t[2];
int cnt[2];

FILE *fout=fopen("output.txt","w");

void abstraction(int x)
{
	int tp=1;

	tree[x][1]=tree[x][t[x]];
	tree[x][t[x]]=100000;
	t[x]-=1;

	do{
		if( tree[x][ tp*2 ] < tree[x][tp*2 +1]){
			if(tree[x][tp*2] < tree[x][tp]){
				swap(tree[x][tp*2],tree[x][tp]);
				tp*=2;
			}
			else{
				if(tree[x][tp*2+1] < tree[x][tp]){
					swap(tree[x][tp],tree[x][tp*2+1]);
					tp=tp*2+1;
				}
				else
					break;
			}
		}
		else{
			if(tree[x][tp*2+1] < tree[x][tp]){
				swap(tree[x][tp],tree[x][tp*2+1]);
				tp=tp*2+1;
			}
			else{
				if(tree[x][tp*2] < tree[x][tp]){
					swap(tree[x][tp*2],tree[x][tp]);
					tp=tp*2;
				}
				else
					break;
			}
		}
	}while(1);
}

void insert(int a,int x)
{
	int tp;

	t[x]+=1;
	tp=t[x];
	tree[x][t[x]]=a;

	while(tp>1){
		if(tree[x][tp] < tree[x][tp/2]){
			swap(tree[x][tp],tree[x][tp/2]);
			tp/=2;
		}
		else
			break;
	}
}

void process()
{

	t[0]=t[1]=0;

	for(i=1;i<=500;i++){
		tree[0][i]=100000;
		tree[1][i]=100000;
	}

	cnt[0]=cnt[1]=0;

	for(i=1;i<=N+M;i++){
		if(where[i] == 1){
			if( tree[0][1] <= departure[i] ){
				abstraction(0);
				insert(arrival[i],1);
			}
			else{
				cnt[0]+=1;
				insert(arrival[i],1);
			}
		}
		else{
			if( tree[1][1] <= departure[i] ){
				abstraction(1);
				insert(arrival[i],0);
			}
			else{
				cnt[1]+=1;
				insert(arrival[i],0);
			}
		}

	}

}

int main(void)
{
	FILE *fin=fopen("input.txt","r");

	fscanf(fin,"%d",&T);

	FILE *fout=fopen("output.txt","w");


	for(int test=1;test<=T;test++){
		fscanf(fin,"%d",&Time);

		fscanf(fin,"%d%d",&N,&M);

		for(i=1;i<=N;i++){
			fscanf(fin,"%s %s",data_departure,data_arrival);

//			departure[i]=data_departure[0]-'0'*1000+(data_departure[1]-'0')*100 + (data_departure[3]-'0')*10+(data_departure[4]-'0');
//			arrival[i] = data_arrival[0]-'0'*1000+(data_arrival[1]-'0')*100 + (data_arrival[3]-'0')*10+(data_arrival[4]-'0') + Time;
			departure[i]=((data_departure[0]-'0')*10+(data_departure[1]-'0'))*60 + (data_departure[3]-'0')*10+(data_departure[4]-'0');
			arrival[i] = ((data_arrival[0]-'0')*10+(data_arrival[1]-'0'))*60 + (data_arrival[3]-'0')*10+(data_arrival[4]-'0') + Time;
			where[i]=1;
		}
		for(i=1;i<=M;i++){
			fscanf(fin,"%s %s",data_departure,data_arrival);

//			departure[N+i]=(data_departure[0]-'0')*1000+(data_departure[1]-'0')*100 + (data_departure[3]-'0')*10+(data_departure[4]-'0');
//			arrival[N+i] = (data_arrival[0]-'0')*1000+(data_arrival[1]-'0')*100 + (data_arrival[3]-'0')*10+(data_arrival[4]-'0') + Time;
			departure[N+i]=((data_departure[0]-'0')*10+(data_departure[1]-'0'))*60 + (data_departure[3]-'0')*10+(data_departure[4]-'0');
			arrival[N+i] = ((data_arrival[0]-'0')*10+(data_arrival[1]-'0'))*60 + (data_arrival[3]-'0')*10+(data_arrival[4]-'0') + Time;
			where[N+i]=2;
		}

		for(i=1;i<M+N;i++){
			for(j=M+N-1;j>=i;j--){
				if(departure[j] > departure[j+1]){
					swap(departure[j],departure[j+1]);
					swap(arrival[j],arrival[j+1]);
					swap(where[j],where[j+1]);
				}
				else if(departure[j] == departure[j+1]){
					if(arrival[j] > arrival[j+1]){
						swap(arrival[j],arrival[j+1]);
						swap(where[j],where[j+1]);
					}
				}
			}
		}

		process();

		fprintf(fout,"Case #%d: %d %d\n",test,cnt[0],cnt[1]);
		printf("Case #%d: %d %d\n",test,cnt[0],cnt[1]);
	}

	return 0;
}