#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <set>

#define rei(i,a,b) for(int i=a;i<b;i++)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define pb(a,x) a.push_back(x)
#define sort(v) sort(v.begin(),v.end())

using namespace std;

int main()
{
	freopen("C-small-attempt0 (1).in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	rei(t,0,T){
		int As,Ab,Bs,Bb;
		scanf("%d%d%d%d",&As,&Ab,&Bs,&Bb);
		int ret=0;
		ree(A,As,Ab){
			ree(B,Bs,Bb){
				int L,S;
				L=max(A,B);
				S=min(A,B);
				rei(i,0,30){
					L=L-(max(1,(int)(L/S)-1))*S;
					swap(L,S);
					if(S<=0){
						if(i%2)
							ret++;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",t+1,ret);
	}
	return 0;
}
