#include <iostream>
using namespace std;

int tn,n,q;
int minim;
int keluar[110];
bool ever[11000];
int res=0;

void dfs(int lvl){
	if (lvl==q){
		minim=min(minim,res);
		return;
	}
	
	int i,j;
	int tambah=0;
	
	for (i=0;i<q;i++){
		if (ever[keluar[i]]) continue;
		//printf("debug %d %d\n",keluar[i],lvl);
		tambah=0;
		for (j=keluar[i]-1;j>=0 && !ever[j];j--)
		     tambah++;
		for (j=keluar[i]+1;j<n && !ever[j];j++)
		     tambah++;

		ever[keluar[i]]=1;
		res+=tambah;
		dfs(lvl+1);
		res-=tambah;
		ever[keluar[i]]=false;
	}
}

int main(){
	int i;

	scanf("%d",&tn);
	for (int test=1;test<=tn;test++){
		minim=1000000;
		scanf("%d %d",&n,&q);
		for (i=0;i<n;i++){
		    ever[i]=false;
		}
		//puts("debug 1");
		for (i=0;i<q;i++){
			scanf("%d",&keluar[i]);
			keluar[i]--;
		}
		//puts("debug 2");
		res=0;
		dfs(0);
		
          printf("Case #%d: ",test);
		cout << minim << endl;
	}

	return 0;
}
