#include <iostream>

using namespace std;
typedef long long llong;

int n;
int c;
int d;
int	cl[26][26];
int cv[26][26];
int mark[26];
char s[101];
int sk[100];
int sp;

int main(){

	int NN;cin>>NN;
	for(int MM=1;MM<=NN;MM++){
		memset(cl,0,sizeof(cl));
		memset(cv,-1,sizeof(cv));

		cin>>c;
		for(int i=0;i<c;i++) {
			cin>>s;
			cv[s[0]-'A'][s[1]-'A']=s[2]-'A';
			cv[s[1]-'A'][s[0]-'A']=s[2]-'A';
		}

		cin>>d;
		for(int i=0;i<d;i++) {
			cin>>s;
			cl[s[0]-'A'][s[1]-'A']=1;
			cl[s[1]-'A'][s[0]-'A']=1;
		}

		cin>>n;
		cin>>s;

		sp=0;
		for(int l=0;l<n;l++) {
			int cc=s[l]-'A';
			if(sp>0&&cv[cc][sk[sp-1]]+1)
				sk[sp-1]=cv[cc][sk[sp-1]];
			else {
				int cleared=0;
				for(int i=0;i<sp;i++)
					if(cl[sk[i]][cc]){
						sp=0;
						cleared=1;
						break;
					}
				if (!cleared) {
					sk[sp++]=cc;
				}
			}
		}

		cout<<"Case #"<<MM<<": [";
		for(int i=0;i<sp;i++)
			cout<<(i?", ":"")<<(char)('A'+sk[i]);
		cout<<"]"<<endl;
	}
	return 0;
}