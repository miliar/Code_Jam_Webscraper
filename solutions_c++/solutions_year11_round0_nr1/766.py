#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <hash_map>

using namespace std;
const int MNAX=100;

void go(int* a,int& curA,int curAN){
	if (curA<a[curAN+1]) ++curA;
	else --curA;
}

void push(int& curAN){
	++curAN;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int test;
	cin>>test;
	for (int t=1;t<=test;++t){
		int a[MNAX+2], b[MNAX+2];
		int ai[MNAX+2], bi[MNAX+2];
		int n,na=0,nb=0,ans = 0;
		int i,j;
		cin>>n;
		for (i=1;i<=n;++i){
			char ch;int k;
			cin>>ch>>k;
			if (ch=='O'){
				++na;
				a[na] = k;
				ai[na] = i;
			}
			else{
				++nb;
				b[nb] = k;
				bi[nb] = i;
			}
		}

		int curA=1,curB=1;
		int curAN=0,curBN=0;
		while (curAN!=na || curBN!=nb){
			++ans;
			if (curAN!=na && curBN!=nb){
			
				if (a[curAN+1]==curA){
					if (ai[curAN+1]<bi[curBN+1]){
						push(curAN);
						if (b[curBN+1]!=curB){
							go(b,curB,curBN);
						}
					}
					else{
						if (b[curBN+1]==curB){
							push(curBN);
						}
						else{
							go(b,curB,curBN);
						}
					}
				}
				else{
					go(a,curA,curAN);
					if (b[curBN+1]==curB){
						if (bi[curBN+1]<ai[curAN+1]){
							push(curBN);
						}
					}
					else{
						go(b,curB,curBN);
					}
				}
			}
			else if (curAN!=na){
				if (a[curAN+1]==curA){
					push(curAN);
				}
				else {
					go(a,curA,curAN);
				}
			}
			else{			
				if (b[curBN+1]==curB){
					push(curBN);
				}
				else {
					go(b,curB,curBN);
				}
			}
		}

		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
