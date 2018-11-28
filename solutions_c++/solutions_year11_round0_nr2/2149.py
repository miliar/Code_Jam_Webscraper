#include<iostream>
#include<string>
#include<cstdlib>
#include<cstring>
using namespace std;

int com[30][30];
int opp[30][30];
int T;

int main(){
	cin >> T;
	for(int t=1;t<=T;t++){
		int C,D,N;
		memset(com,0,900*sizeof(int));
		memset(opp,0,900*sizeof(int));
		cin >> C;
		for(int i=0;i<C;i++){
			char ch1,ch2,ch3;
			int c1,c2,c3;
			cin >> ch1 >> ch2 >> ch3;
			c1 = ch1-'A'+1; c2 = ch2-'A'+1; c3 = ch3-'A'+1;
			com[c1][c2] = com[c2][c1]=c3;
		}
		cin >> D;
		for(int i=0;i<D;i++){
			char ch1,ch2;
			int c1,c2;
			cin >> ch1 >> ch2;
			c1 = ch1-'A'+1; c2=ch2-'A'+1;
			opp[c1][c2]=opp[c2][c1]=1;
		}
		cin >> N;
		int ar[120],cnt=0;
		for(int i=0;i<N;i++){
			char ch;
			int c;
			cin >> ch; c=ch-'A'+1;
			if(cnt==0)
				ar[cnt++]=c;
			else if(com[ar[cnt-1]][c])
				ar[cnt-1] = com[ar[cnt-1]][c];
			else{
				bool cont=1;
				for(int j=0;j<cnt;j++)
					if(opp[ar[j]][c]){
						cnt=0;
						cont=false;
						break;
					}
				if(cont)
					ar[cnt++]=c;
			}
		}
		cout << "Case #" << t << ": [";
		for(int i=0;i<cnt;i++){
			cout << (char)(ar[i]+'A'-1);
			if(i<cnt-1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
}
