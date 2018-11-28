#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
using namespace std;

int main(){
	int T; scanf("%d",&T);
	for (int tc = 1; tc <= T; tc += 1) {
		map<int,char> ganti;
		int hapus[27]={0};
		int c; scanf("%d",&c);
		for (int i = 0; i < c; i += 1) {
			char temp[4]; scanf("%s",temp);
			ganti[(1<<(temp[0]-'A'))+(1<<(temp[1]-'A'))]=temp[2];
		}
		int d; scanf("%d",&d);
		for (int i = 0; i < d; i += 1) {
			char temp[3]; scanf("%s",temp);
			hapus[temp[0]-'A'+1]=temp[1]-'A'+1;
			hapus[temp[1]-'A'+1]=temp[0]-'A'+1;
		}
		int n; scanf("%d",&n);
		char kata[n+1]; scanf("%s",kata);
		int ada[27]={0};
		vector<char> hasil;
		for (int i = 0; i < n; i += 1) {
			if(hasil.size()){
				const int x=(1<<(hasil[hasil.size()-1]-'A'))+(1<<(kata[i]-'A'));
				if(ganti.count(x)){
					ada[hasil[hasil.size()-1]-'A'+1]--;
					ada[ganti[x]-'A'+1]++;
					hasil[hasil.size()-1]=ganti[x];
				} else if(ada[hapus[kata[i]-'A'+1]]) {
					hasil.clear();
					memset(ada,0,sizeof(ada));
				} else {
					hasil.push_back(kata[i]);
					ada[kata[i]-'A'+1]++;
				}
			} else{
				hasil.push_back(kata[i]);
				ada[kata[i]-'A'+1]++;
			}
		}
		printf("Case #%d: [",tc);
		for (int i = 0; i < hasil.size(); i += 1) {
			printf("%c",hasil[i]);
			if(i<hasil.size()-1) printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
