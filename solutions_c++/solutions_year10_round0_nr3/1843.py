#include <fstream>
using namespace std;
struct TMP{
	int num;
	int next;
};

int main()
{
	int t,r,k,n;
	int g[1001];
	TMP next[1001];
	unsigned long long ret;
	ifstream in("C-large.in");
	ofstream out("result.txt");
	in>>t;
	for (int i=0;i<t;i++){
		ret=0;
		in>>r>>k>>n;
		for (int j=0;j<n;j++){
			in>>g[j];
			next[j].next=-1;
		}

		int idx=0,pos;
		do{
			next[idx].num=0;
			for (int x=0;x<n;x++){
				pos=(idx+x)%n;
				next[idx].num+=g[pos];
				if (next[idx].num>k){
					break;
				}
			}
			if (next[idx].num<=k){
				pos=idx;
			}
			else{
				next[idx].num-=g[pos];
			}
			next[idx].next=pos;
			idx=pos;
		}while (next[idx].next==-1);

		unsigned long long cycle_ret=0;
		int cycle_len=0;
		pos=idx;
		do{
			cycle_ret+=next[pos].num;
			pos=next[pos].next;
			cycle_len++;
		}while (pos!=idx);

		int round=0;
		for (pos=0;pos!=idx&&round<r;pos=next[pos].next){
			ret+=next[pos].num;
			round++;
		}

		int cycles=(r-1-round)/cycle_len;
		ret+=cycles*cycle_ret;
		round+=cycles*cycle_len;

		pos=idx;
		for (;round<r;round++){
			ret+=next[pos].num;
			pos=next[pos].next;
		}

		out<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	in.close();
	out.close();
	return 0;
}