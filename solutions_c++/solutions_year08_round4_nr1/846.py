/*Author Gaurav Agarwal */
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
#include<complex>
using namespace std;

#define Debug 0
#define LET(x,a)        __typeof(a) x(a)
#define IFOR(i,a,b)     for(LET(i,a);i!=(b);++i)
#define EACH(it,v)      IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)      for(int i=(int)(a) ; i < (int)(b);++i)
#define FORD(i,a,b)     for(int i=(a);i>=(b);--i)
#define REP(i,n)        FOR(i,0,n)
#define SZ              size()
#define PB              push_back
#define PF              push_front
#define PRINT(x)        cout<<#x<<" = "<<x<<endl
#define PRINTI(x,n)     REP(i,n) cout<<(x)[i]<<" ";cout<<endl
#define PRINTIJ(x,m,n)  for(__typeof(m) i=0;i<m;++i,cout<<"\n") REP(j,n) cout<<(x)[i][j]<<" "
#define PRESENT(c,x)    ((c).find(x) != (c).end())
#define CPRESENT(c,x)   (find(c.begin(),c.end(),x) != (c).end())
int ans1,m;
int rec(int v,int kk)
{
	//      cout<<v<<" "<<kk<<" "<<(m-1)/2<<endl;
	        int i,j;
		        if(v>(m-1)/2)
				        {
						                if(kk==val[v])
									                {
												                        ans[v][kk]=0;
															                        return 0;
																		                }
								                else
											                {
														                //      cout<<"{"<<kk<<" "<<val[v]<<"}"<<endl;
														                        ans[v][kk]=INF;
																	                        return INF-1;
																				                }
										        }
			        //cout<<"haha"<<endl;
			        int swa=0;
				        for(i=0;i<2;++i)
						                for(j=0;j<2;++j)
									                {
												                        if(ans[2*v][i]==INF)ans[2*v][i]=rec(2*v,i);
															                        if(ans[2*v+1][j]==INF)ans[2*v+1][j]=rec(2*v+1,j);
																		                }
					        for(i=0;i<2;++i)
							                for(j=0;j<2;++j)
										                {
													                        if(ans[2*v][i]==INF||ans[2*v+1][j]==INF)continue;
																                        if(g[v]==0)
																				                        {

																								                                if(((i)||(j))==kk)ans[v][kk]<?=ans[2*v][i]+ans[2*v+1][j];
																												                                else if(change[v]&&(((i)&&(j))==kk))ans[v][kk]<?=ans[2*v][i]+ans[2*v+1][j]+1;
																																                        }
																			                        else
																							                        {
																											                                if(((i)&&(j))==kk)ans[v][kk]<?=ans[2*v][i]+ans[2*v+1][j];
																															                                else if(change[v]&&(((i)||(j))==kk))ans[v][kk]<?=ans[2*v][i]+ans[2*v+1][j]+1;

																																			                        }
																						                }
						//      cout<<ans[v][kk]<<" "<<v<<" "<<kk<<endl;
						        return ans[v][kk];

}
int main(){
	        int t;cin>>t;
		        FOR(cas,1,t+1)
				        {
						int v;
						scanf("%d%d",&m,&v);
						memset(g,-1,sizeof(g));
						for(int i=1;i<=(m-1)/2;++i)
						{
							        scanf("%d%d",&g[i],&change[i]);

						}
						for(int i=(m-1)/2+1;i<=m;++i)
						{
							        scanf("%d",&val[i]);
						}
						for(int i=0;i<20000;++i)ans[i][0]=INF,ans[i][1]=INF;
						ans1=0;
						//cout<<v<<endl;
						rec(1,v);
						//REP(i,m+1)cout<<g[i]endl;
						if(ans[1][v]>INF-2)cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE\n";
						else
							cout<<"Case #"<<cas<<": "<<ans[1][v]<<endl;
						        }
			        return 0;
}

