//============================================================================
// Name        : B.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

/*#include <iostream>
#define MAXN 100
using namespace std;


bool canbe[MAXN];
int v[MAXN];
int locat[MAXN];
int main()
{

    freopen("B-small-attempt1.in","r",stdin);
    freopen("BSout.txt","w",stdout);
    int ca,n,k,b,t;
    scanf("%d",&ca);
    int cs=1;
    while(ca--)
    {
        scanf("%d%d%d%d",&n,&k,&b,&t);
        for(int i=0;i<n;i++)
                    scanf("%d",&locat[i]);
                for(int i=0;i<n;i++)
                    scanf("%d",&v[i]);
                for(int i=0;i<n;i++)
                {
                    if(locat[i] + v[i]*t>=b)
                        canbe[i]=true;
                    else
                        canbe[i]=false;
                }
                int ans=0;
                for(int i=n-1;i>=0 && k;i--)
                {
                    if(canbe[i])
                        k--;
                    else
                    {
                        for(int j=i-1;j>=0;j--)
                            if(canbe[j])
                            {
                                canbe[j]=false;
                                canbe[i]=true;
                                  ans+=i-j;
                                  k--;
                                  break;

                              }
                      }
                  }
                  printf("Case #%d: ",cs++);

                  if(!k)
                      printf("%d\n",ans);
                  else
                      printf("IMPOSSIBLE\n");
              }


          }

*/
#include <iostream>
using namespace std;
#define MAXN 52

int N,K,B,T,x[MAXN],v[MAXN],outp;
bool used[MAXN];

int main() {
	int cas,cnt=0,i,j,jum;
	freopen("B-large.in", "r", stdin);
	FILE *out;
	out = fopen("output.txt", "w");
	scanf("%d", &cas);
	while(cas--){
		scanf("%d%d%d%d", &N, &K, &B, &T);
		for(i = 0; i < N; ++i)
			scanf("%d", &x[i]);
		for(i = 0; i < N; ++i)
			scanf("%d", &v[i]);
		outp = 0;
		for(i = 0; i < N; ++i){
			x[i] += (v[i]*T);
			if(x[i] >= B)
				used[i] = true;
			else
				used[i] = false;
		}
		for(j = N-1; j >= 0; --j){
			if(used[j]){
				--K;
				if(!K)
					break;
			}
			else{
				jum = 0;
				for(i = j-1; i >= 0; --i){
					if(used[i]){
						used[j] = true;
						used[i] = false;
						outp += (j-i);
						--K;
						break;
					}
				}
			}
			if(!K)
				break;
		}
		if(K){
			fprintf(out, "Case #%d: IMPOSSIBLE\n", ++cnt);
			continue;
		}
		fprintf(out, "Case #%d: %d\n", ++cnt, outp);
	}
	fclose(out);
	return 0;
}

