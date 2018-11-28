#include <iostream> 
#include <cmath> 
using namespace std;

void decode(int v, char* cc,int n) {
	int i;
	for(i=0;i<n;i++) {
		cc[i]=v%10;
		v/=10;
	}
}

int encode(char* cc, int n) {
	int ret = 0;
	int i;
	for(i=n-1;i>=0;i--) {
		ret=ret*10+cc[i];
	}
	return ret;
}

const int P=403201;
int hash[P];
int que[P];
int dep[P];

void insert(int k){ 
	int key=k%P;
	while(hash[key]!=-1) {
		key=(key+1)%P;
	}
	hash[key]=k;
}

bool find(int k) {
	int key=k%P;
	while(hash[key]!=-1) {
		if (hash[key]==k) return true;
		key=(key+1)%P;
	}
	return false;
}

bool check(char* cc, int* tar, int n) {
	for(int i=0;i<n;i++) {
		if (i<tar[cc[i]]) return false;
	}
	return true;
}

int main() 
{ 
	int TC, T;
	int i,j;

	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&TC);
	for(T = 1; T <= TC; T++) {
		memset(hash,-1,sizeof(hash));
		int n;
		int tar[100];
		scanf("%d",&n);
		for(i=0;i<n;i++) {
			char mat[100];
			scanf("%s", mat);
			int min = 0;
			for(j=0;j<n;j++) {
				if (mat[j]=='1') min=j;
			}
			tar[i]=min;
		}

		int ans=0;
		bool flag=false;
		char cc[200];
		que[0]=76543210;
		dep[0]=0;
		insert(que[0]);		
		decode(que[0],cc,n);
		if (check(cc, tar, n)) {
			flag=true;
		}

		for(int l=0,r=1;l<r && flag==false;l++) {
			int v=que[l];
			decode(v, cc, n);
			for(i=0;i<n-1;i++) {
				char tmp=cc[i];
				cc[i]=cc[i+1];
				cc[i+1]=tmp;
				if (check(cc, tar, n)) {
					ans=dep[l]+1;
					flag=true;
					break;
				}

				int u=encode(cc, n);
				if (find(u) == false) {
					insert(u);
					dep[r]=dep[l]+1;
					que[r]=u;
					r++;
				}
				cc[i+1]=cc[i];
				cc[i]=tmp;
			}
		}
		printf("Case %d: %d\n", T, ans);
	}
    return 0; 
}