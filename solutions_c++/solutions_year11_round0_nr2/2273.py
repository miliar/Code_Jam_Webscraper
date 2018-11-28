#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;

int T;
int C, D;
char comb[40][5], oppo[40][5], invok[105];
bool contains(vector<char> &v, char c)
{
	int i;
	int n = v.size();
	for(i=0;i<n;i++) if(v[i] == c) return true;
	return false;
}
int main()
{
	freopen("largeinput.txt", "r", stdin);
	freopen("largeoutput.txt", "w", stdout);
	vector<char> v;

	int i, j, flag;
	char a ,b;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		printf("Case #%d: [", t);
		scanf("%d", &C);
		for(i=1;i<=C;i++) scanf("%s",comb[i]);
		scanf("%d", &D);
		for(i=1;i<=D;i++) scanf("%s",oppo[i]);
		
		int l;
		scanf("%d %s",&l, invok);
		v.clear();

		for(i=0;i<l;i++)
		{
			v.push_back(invok[i]);
			// comb
			while(v.size() >= 2)
			{
				a = v.back();
				b = v[v.size()-2];
				flag = 0;
				for(j=1;j<=C;j++)
				{
					if((comb[j][0] == a && comb[j][1] == b) || (comb[j][0] == b && comb[j][1] == a)){
						flag = 1;
						v.pop_back(); v.pop_back();
						v.push_back(comb[j][2]);

						if(v.size() < 2) break;
						a = v.back();
						b = v[v.size()-2];
					}
				}
				if(!flag) break;
			}

			// clear
			for(j=1;j<=D;j++){
				if(contains(v, oppo[j][0]) && contains(v, oppo[j][1])){
					v.clear();
					break;
				}
			}
		}
		for(i=0;i<v.size();i++){
			if(i != 0) printf(", ");
			printf("%c", v[i]);
		}
		printf("]\n");
		
	}
	return 0;
}