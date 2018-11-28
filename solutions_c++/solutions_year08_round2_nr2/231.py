#include<iostream>
#include<cmath>
#include<set>
using namespace std;
#define N 10000
bool flag[N + 1];
int visit[N];
int prime[40000];
int len;
set<int>kk;
bool tt[10000];
void preprocess(){
    len = 0;
    int i, j;
    for (i = 2; i <= N; i++){
        if (flag[i]) continue;
        prime[len++] = i;
        for (j = i * i; j <= N; j += i)
            flag[j] = true;
    }
}
int father[N],num[N];
void makeset(int x){
	father[x] = x;
	num[x] = 1;
}
int find(int x){
	if(father[x] == x)
		return x;
		
	return father[x] = find(father[x]);
}
void Union(int x,int y){
	int k1,k2;
	k1 = find(x);
	k2 = find(y);
	if(k1==k2)
		return ;
	if(num[k1]>num[k2]){
		father[k2] = k1;
		num[k1]+=num[k2];
	}
	else{
		father[k1] = k2;
		num[k2]+=num[k1];
	}
}
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("ans2.out","w",stdout);
	preprocess();
	
	int test;
	scanf("%d" , &test);
	int Case = 0;
	while(test--){
		int A , B , P;
		Case++;
		scanf("%d%d%d" , &A , &B , &P);
		memset(tt ,false , sizeof(tt));
		int i ,j ,biaoji  ,k;
		for(i = 0; i < len; i++){
			if(prime[i] >= P){
				biaoji = i;
				break;
			}
		}
		memset(father ,0 ,sizeof(father));
		memset(num , 0 , sizeof(num));
		for(i = A ; i<=B ; i++){
			makeset(i);
		}
		for(i = biaoji ; i < len ; i++){
			int st = (A / prime[i]);
			if(A%prime[i] !=0)
				st++;
			st *= prime[i];
			for(j = st ; j <=B ; j+=prime[i]){
				int  k1 = find(j);
				int  k2 = find(st);
				father[k1] = k2;
			}
		}
		/*for(i = A ; i <= B ; i++){
			for(j = A+1 ; j<=B ; j++){
				for(k = biaoji ; k < len ;k++){
					if(i%prime[k] == 0 &&j%prime[k] == 0){
						int st ,ed;
						st = find(i);
						ed = find(j);
						Union(st , ed);
						break;
					}
					if(prime[k] > A || prime[k] >B)
						break;
				}
			}
		}*/
		//kk.clear();
		int count = 0;
		for(i = A ; i <= B ; i++){
			if(i == father[i])
				count++;
			
		}
		printf("Case #%d: %d\n" , Case , count);
	}
	return 0;
}