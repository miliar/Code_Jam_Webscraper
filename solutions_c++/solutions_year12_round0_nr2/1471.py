#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int data[101];


int main()
{
	//freopen("myresult.txt","w+",stdout);
	int T;
	scanf("%d",&T);
	for (int i(1); i<=T; ++i) {
		int N,S,P;
		scanf("%d%d%d",&N,&S,&P);
		int value;
		int cnt = 0;
		for (int j(0); j<N; ++j) {
			scanf("%d",&value);
			if (value == 0) {
				if (value >= P) {
					++cnt;	
				}
				continue;
			}
			if (value%3 == 0) {
				if (value/3 >= P) {
					++cnt;	
				}	else {
					if (S && value/3 + 1 >= P) {
						++cnt;
						--S;	
					}	
				}
			} else {
				if ((value - 1)%3 == 0) {
					if ((value - 1)/3 + 1 >= P) {
						++cnt;	
					}
				}	else {
					if ((value + 1)%3 == 0) {
						if ((value + 1)/3 >= P) {
							++cnt;	
						}	else {
							if (S && (value + 1)/3 + 1 >= P) {
								--S;
								++cnt;
							}	
						}
					}	
				}
			}
		}
		cout<<"Case #"<<i<<": "<<cnt<<endl;	
	}
	return 0;	
}
