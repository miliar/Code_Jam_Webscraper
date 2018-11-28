#include <iostream>
#include <cstdio>
#define M 110
using namespace std;
int b[M];
int o[M];
int order[M*2];
int main()
{
	int t,cas = 0;
	freopen("./a.in","r",stdin);
	freopen("./aa.out","w",stdout);
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		b[0] = o[0] = order[0] = 0;
		while(n--){
			char c;int p;
			cin>>c>>p;
			//cout<<c<<" "<<p<<endl;
			if(c == 'B'){
				b[++b[0]] = p;
				order[++order[0]] = 0;
			}
			else{
				o[++o[0]] = p;
				order[++order[0]] = 1;
			}
		}
		int p0 = 1,p1 = 1;
		int s0 = 1,s1 = 1;
		int ans = 0;
		for(int i = 1; i <= order[0];++i){
			//cout<<"***"<<ans<<"  "<<s0<<"***"<<endl;
			if(order[i]){
				int load = o[p1++] - s1;
				if(load < 0)
					load = -load;
				++load;
				ans += load;
				s1 = o[p1-1];
				if(b[p0] > s0){
					s0 += load;
					if(s0 > b[p0])
						s0 = b[p0];
				}
				else{
					s0 -= load;
					if(s0 < b[p0])
						s0 = b[p0];
				}
			}
			else{
				int load = b[p0++] - s0;
				if(load < 0)
					load = -load;
				++load;
				ans += load;
				s0 = b[p0-1];
				if(o[p1] > s1){
					s1 += load;
					if(s1 > o[p1])
						s1 = o[p1];
				}
				else{
					s1 -= load;
					if(s1 < o[p1])
						s1 = o[p1];
				}
			}
		}
		cout<<"Case #"<<++cas<<": ";
		cout<<ans<<endl;
	}
	return 0;
}

