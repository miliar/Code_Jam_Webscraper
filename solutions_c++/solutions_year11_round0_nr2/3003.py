#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>

using namespace std;

#define CLR(a) memset(a,0,sizeof(a))
#define F(i,a,b) for(i=a;i<=b;++i)

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,C,D,N,cs=0;
	int i,k;
	string S;
	char stk[200],ch,old; int top;

	bool op[50][50];char fr[50][50];

	cin >> T;

	while(T--){

		CLR(fr); cin >> C;
		F(i,1,C){
			cin >> S;
			fr[S[0]-'A'][S[1]-'A'] = fr[S[1]-'A'][S[0]-'A'] = S[2];
		}

		CLR(op); cin >> D;
		F(i,1,D){
			cin >> S;
			op[S[0]-'A'][S[1]-'A'] = op[S[1]-'A'][S[0]-'A'] = true;
		}

		cin >> N >> S; top=0;
		F(i,0,N-1){
			ch = S[i];
			if(top>0){
				old = fr[stk[top-1]-'A'][ch-'A'];
				if(old!=0){
					stk[top-1] = old;
					continue;
				}
			}

			bool flag = false;
			F(k,0,top-1)
				if(op[stk[k]-'A'][ch-'A']){
					flag=true;
					break;
				}
			stk[top++]=ch;
			if(flag) top=0;
		}

		stk[top]=0;
		
		printf("Case #%d: [",++cs);
		F(i,0,top-1){
			if(i) printf(", ");
			printf("%c",stk[i]);
		}printf("]\n");
	}

	return 0;
}