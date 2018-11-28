#include <iostream>
#include <map>
#include <vector>
#include <queue>
using namespace std;

int n;

typedef struct {
	vector<int> v;
	int lvl;
} data;

bool valid(vector<int> a){
	int i;
	
	for (i=0;i<n;i++){
		if (a[i]>i) break;
	}	
	
	return i==n;
}

int main(){
	int tc;
	
	scanf("%d",&tc);
	for (int test=1;test <= tc;test++){
	
		int i,j;
		string str;
		
		map<vector<int>,bool> m;
		vector<int> baca;
		scanf("%d",&n);
		for (i=0;i<n;i++){
			cin >> str;
			for (j=str.length()-1;j>0 && str[j]!='1';j--);
			baca.push_back(j);
		}
		
		data lala;
		lala.v = baca;
		lala.lvl = 0;
		
		queue<data> q;
		
		q.push(lala);
		
		while (1){
			data front = q.front();
			q.pop();
			
			if (valid(front.v)){
				
				printf("Case #%d: %d\n",test,front.lvl);
				break;
			}
			
			for (i=0;i<n-1;i++){
				data push = front;
				push.lvl++;
				int temp=push.v[i];
				push.v[i]=push.v[i+1];
				push.v[i+1]=temp;
				
				if (!m[push.v]){
					m[push.v]=1;
					q.push(push);	
				}
			}
		}
		
	}
	
	return 0;	
}
