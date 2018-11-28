#include <stdio.h>
#include <memory.h>
#include <map>
using namespace std;
#define SIZE 1010

class Node{
public:
	int t[SIZE];
	int n;
	Node(int tn,int *ref){
		n = tn;
		for(int i = 0; i < n; i++){
			t[i] = ref[i];
		}
	}
	bool operator == (const Node ref) const
	{
		for(int i = 0; i < n; i++)
			if(t[i] != ref.t[i])
				return false;
		return true;
	}
	bool operator < (const Node ref) const
	{
		for(int i = 0; i < n; i++)
			if(t[i] < ref.t[i])
				return true;
		return false;
	}
	bool operator > (const Node ref){
		for(int i = 0; i < n; i++)
			if(t[i] > ref.t[i])
				return true;
		return false;
	}
	Node & operator = (const Node &ref)
	{
		for(int i = 0; i < n; i++)
			t[i] = ref.t[i];
	}
};
__int64 cnt[SIZE];
int d[SIZE*SIZE*3];
int main()
{
	int T,no,i,r,k,n,it;
	int font;
	freopen("E:\\C-small-attempt2.in","r",stdin);
	freopen("E:\\C-small-attempt2.out","w",stdout);
	scanf("%d",&T);
	no = 0;
	while(T--){
		map<Node,int> mp;
		no++;
		memset(cnt,0,sizeof(cnt));
		scanf("%d%d%d",&r,&k,&n);
		int sum = 0;
		for(i = 0; i < n; i++)
		{
			scanf("%d",&d[i]);
			sum += d[i];
		}
		printf("Case #%d: ",no);
		if(sum <= k){
			printf("%I64d\n",(__int64)r*sum);
			continue;
		}
		font = 0;
		__int64 ans = 0;
		Node fin(n,d);
		for(it = 1; it <= r; it++){
			Node tn(n,&(d[font]));
			if(mp[tn] != 0){
				int tnum = it-1;
				int cir = it - mp[tn];
				int aa = mp[tn]-1;
				int cntt = cnt[tnum] - cnt[aa];
				__int64 tmp = (r-tnum)/cir;
				ans += tmp*cntt;
				tmp = (r-tnum)%cir;
				if(tmp != 0){
					int tt = mp[tn]+tmp-1;
					ans += cnt[tt] - cnt[aa];
				}
				break;
			}
			else 
				mp[tn] = it;
			__int64 num = 0;
			int *p;
			int tk = k;
			for(i = 0,p = &(d[font]); i < n; i++,p++){
				if(tk >= *p)
				{
					tk -= *p;
					num += *p;
				}
				else break;
			}
			ans += num;
			cnt[it] = ans;
			int nf = font+i;
			for(int i = font; i < nf; i++){
				d[i+n] = d[i];
			}
			font = nf;
		}
		printf("%I64d\n",ans);
	}
	return 0;
}