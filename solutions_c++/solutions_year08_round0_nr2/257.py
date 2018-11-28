#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;


#define Z (24*60)
vector<int> A[Z], B[Z];



int getMin(char s[]){
	return  ( (s[0]-'0')*10 + (s[1]-'0') ) * 60 +
		( s[3]-'0') * 10 + (s[4]-'0');
}

void show(){
	int i;
	for(i = 0; i<25; ++i){
	//	cout<<i<<": "<<A[i]<<" "<<B[i]<<endl;
	}
	cin>>i;
}

void solve(int c){
	int T, NA, NB, i;
	scanf("%d",&T);
	scanf("%d%d",&NA, &NB);
	

	for(i=0;i<Z;++i){
		A[i].clear();
		B[i].clear();
	}

	int RA = 0;
	int RB = 0;

	char s1[100], s2[100];
	for(i=0; i<NA; ++i){
		scanf("%s%s",&s1, &s2);
		int min1 = getMin(s1);
		int min2 = getMin(s2);
		
		A[min1].push_back(min2+T);
	}

	for(i=0; i<NB; ++i){
		scanf("%s%s",&s1,&s2);
		int min1 = getMin(s1);
		int min2 = getMin(s2);

		B[min1].push_back(min2+T);
	}

	while(NA + NB){
		//cout<<NA<<" "<<NB<<" "<<endl;
		//show();
		int side;

		for(i=0;i<Z;++i){
			if(A[i].size()>0){
				side = 0;
				break;
			}
			if(B[i].size()>0){
				side = 1;
				break;
			}
		}
		//cout<<i<<endl;
		if(side == 0)RA++;
		else RB++;

		int nextPos;
		while(i<Z){
			if(side == 0){
				if(A[i].size() > 0){
					nextPos = A[i][A[i].size()-1]; 
					A[i].pop_back();

					i = nextPos;
					side = 1;

					NA--;
				}
				else{
					i++;
				}
			}
			else{
				if(B[i].size() > 0){
					nextPos = B[i][B[i].size()-1];
					B[i].pop_back();

					i = nextPos;
					side = 0;

					NB--;
				}
				else{
					i++;
				}
			}
		}
	}

	printf("Case #%d: %d %d\n",c,RA,RB);
}

int main (void){
	int N;
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&N);
	for(int t=1; t<=N; ++t){
		solve(t);
	}

	return 0;
}