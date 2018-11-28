#include <iostream>
#include <vector>

using namespace std;
void getans(int st,int n);
vector<int> vp;
int ans;
int main(){
	int i,j,k;
	int x,y,z;
	int T,p,t;
	
	cin>>T;
	t = 1;
	while(T--){
		cin>>p;
		vp.clear();
			
		for(i=0;i<(1<<p);i++){
			cin>>x;
			vp.push_back(p-x);
		}
		
		for(i=p-1;i>=0;i--){
			for(j=0;j<(1<<i);j++)
				cin>>x;
		}
		ans = 0;
		getans(0,1<<p);
		printf("Case #%d: %d\n",t,ans);
		t++;
	}
	return 0;
}

void getans(int st,int n)
{
	int i,j,k;
	bool flag;

	if(n>0){
		k = st;
		flag = false;
		for(i=0;i<n;i++){
			if(vp[st+i] > 0)
				flag = true;
		}
		if(flag){
			ans++;
			for(i=0;i<n;i++){
				if(vp[st+i] > 0)
					vp[st+i]--;
			}
			getans(st,n/2);
			getans(st + n/2,n/2);
		}
	}
}
	
	