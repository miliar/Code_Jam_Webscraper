#include<iostream>

using namespace std;

int comb[26][26];
bool opp[26][26];

int main(){
	int cs,t,p;
	char str[200];
	char ans[200];
	cin>>cs;
	freopen("B.out","w",stdout);
	for(int css=1;css<=cs;css++){
		memset(opp, 0, sizeof(opp));
		memset(comb,-1,sizeof(comb));
		cin>>t;
		for (int i=0;i<t;i++)
		{
			scanf("%s",str);
			comb[str[0]-'A'][str[1]-'A'] = comb[str[1]-'A'][str[0]-'A'] = str[2]-'A';
		}
		cin>>t;
		for (int i=0;i<t;i++)
		{
			scanf("%s",str);
			opp[str[0]-'A'][str[1]-'A'] = opp[str[1]-'A'][str[0]-'A'] = true;
		}
		int N;
		cin>>N;
		p = 0;
		for(int i=0;i<N;i++){
			char c;
			cin>>c;
			c -= 'A';
			ans[p++] = c;
			while(p>=2 && comb[ans[p-1]][ans[p-2]]!=-1)
			{
				ans[p-2] = comb[ans[p-1]][ans[p-2]];
				p--;
			}
			for(int j=0;j<p-1;j++)
			{
				if(opp[ans[p-1]][ans[j]]==true) p = 0;
			}
		}

		printf("Case #%d: [", css);
		for(int i=0;i<p;i++)
		{
			printf("%c", ans[i]+'A');
			if(i!=p-1) cout<<", ";
			else cout<<"]\n";
		}
		if(p==0) cout<<"]\n";
	}
	return 0;
}